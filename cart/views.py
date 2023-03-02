from django.shortcuts import render,HttpResponse
from store.models import Product
from django.http import JsonResponse
from . import cart

def cart_summary(request):

  

    return render(request, 'cart/cart-summary.html')



def cart_add(request):
    
    if request.POST.get('action')=='post':

        product_id=int(request.POST.get('product_id'))
        this_product_qty=int(request.POST.get('product_quantity'))

        this_product=Product.objects.filter(id=product_id).get()
        this_cart=cart.Cart(request)
        this_cart.add(product=this_product,product_qty=this_product_qty)
        
        cart_qty=cart.Cart(request)
         
        return JsonResponse({
            'qty':cart_qty.__len__()
        })


