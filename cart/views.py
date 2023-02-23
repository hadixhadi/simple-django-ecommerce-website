from django.shortcuts import render


from store.models import Product

from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def cart_summary(request):

  

    return render(request, 'cart/cart-summary.html')





