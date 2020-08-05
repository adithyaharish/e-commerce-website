from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import contact_details,Item,OrderItem,Order,Address
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm
from datetime import datetime
import datetime

class HomeView(ListView):
    model=Item
    paginate_by = 6
    template_name='blog/index.html'
    
class ItemDetailView(DetailView):
    model = Item
    template_name = 'blog/single-product.html'    
    
class CheckoutView(LoginRequiredMixin,View):
    def get(self, *args, **kwargs): 
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form=CheckoutForm()
            context={
                'form':form,
                'order':order 
                }
            return render(self.request,'blog/checkout.html',context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("/")
        
    def post(self, *args, **kwargs):
        form=CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address=form.cleaned_data.get('street_address') 
                appartment_address=form.cleaned_data.get('appartment_address') 
                state=form.cleaned_data.get('state') 
                zip=form.cleaned_data.get('zip') 
                phone=form.cleaned_data.get('phone')
                address=Address(
                    user=self.request.user,
                    phone=phone,
                    street_address=street_address,
                    appartment_address=appartment_address,
                    state=state,
                    zip=zip
                    )
                address.save() 
                order.shipping_address=address
                
                order_items = order.items.all()
                order_items.update(ordered=True)
                for item in order_items:
                    item.save()
                    
                order.ordered=True
                order.ordered_date=datetime.datetime.today().strftime('%y-%m-%d %a %H:%M:%S')
                order.phone=phone
                order.state=state
                order.appartment_address=appartment_address
                order.street_address=street_address
                order.zip=zip
                order.save()
                messages.info(self.request, "Your order is placed")
                return redirect("/")
            messages.warning(self.request," Failed checkout")
            return redirect("checkout")
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("checkout")

class MyOrders(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):  
        try:
            order = OrderItem.objects.filter(user=self.request.user, ordered=True)
            address= Order.objects.filter(user=self.request.user, ordered=True)
            context = {
                'order': order,
                'address': address
            }
            print(order)
            return render(self.request, 'blog/my_orders.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")
       

       
@login_required
def contactus(request):
         if request.method=='POST':
            a=(request.POST)
            contact_details.objects.create(name=a['name'],subject=a['subject'],message=a['message'],email=a['email'])
            messages.info(request, "You message has been added.Thankyou")
         return render(request,'blog/contact.html')
      
@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item,created= OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
    else:
        order = Order.objects.create(user=request.user,ordered_date=datetime.datetime.today().strftime('%y-%m-%d %a %H:%M:%S'))
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect("order-summary")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            
            messages.warning(request, "This item was removed from your cart.")
            return redirect("order-summary")
        else:
            messages.warning(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("product", slug=slug)

class OrderSummaryView(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):  
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'blog/cart.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)
    
def about(request):
    return render(request,'blog/about.html')



