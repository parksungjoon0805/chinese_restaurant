from django.shortcuts import render
from seller.models import Food
from .models import Cart
# Create your views here.

def order_detail(request, pk):
    food = Food.objects.get(pk=pk)
    context = {
        'object' : food
    }
    return render(request, 'order/order_detail.html', context)

from django.http import JsonResponse
def modify_cart(request):
    user = request.user
    food_id = request.POST['foodId']
    cart, created  = Cart.objects.get(food__id=food_id, user=user)
    cart.amount += int(request.POST['amountChange'])
    if cart.amount>0:
        cart.save()

    context = {
        'newQuantity': cart.amount,
        'totalQuantity': cart.amount,
        'message' : '성공',
        'success' : True
    }
    return JsonResponse(context)