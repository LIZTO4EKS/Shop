from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from .forms import CommentForm
from .models import Comment, Product, Trainer, CartItem
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import uuid
import random

def home(request):
    is_admin = request.user.is_authenticated and request.user.groups.filter(name='администраторы').exists()
    comments = Comment.objects.all().order_by('-created_at') if request.user.is_authenticated else []
    form = CommentForm() if request.user.is_authenticated else None
    extra_content = "Административный контент" if is_admin else ""
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('home')
    
    return render(request, 'comments/home.html', {
        'form': form,
        'comments': comments,
        'extra_content': extra_content
    })




@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})


@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {
        'items': cart_items,
        'total': total,
    })


def change_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    
    # Обработка действий для изменения количества
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()
    
    return redirect('cart')  # Перенаправление обратно в корзину


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()  # Удаляем товар из корзины
    return redirect('cart')  # Перенаправляем обратно на страницу корзины





    

def shop_view(request):
    products = Product.objects.all()
    return render(request, 'comments/shop.html', {'products': products})



def trener_view(request):
    trainers = Trainer.objects.all()  # Получаем всех тренеров из базы
    return render(request, 'comments/trener.html', {'trainers': trainers})




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})





def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
