from django.shortcuts import render
from seller.models import *
from customer.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'customer/home.html', {'products': products})

def register(request):
    if request.method == 'POST' and request.FILES:
        seller_user_object = CustomerForm(request.POST)
        seller_profile_object = CustomerProfileForm(request.POST, request.FILES)
        if seller_user_object.is_valid() and seller_profile_object.is_valid():
            MUFDO = seller_user_object.save(commit=False)
            MPFDO = seller_profile_object.save(commit=False)
            MUFDO.set_password(seller_user_object.cleaned_data.get('password'))
            MUFDO.save()
            MPFDO.user=MUFDO
            MPFDO.save()
            return HttpResponseRedirect(reverse('user_login'))
        messages.error(request, 'invalid data')

    ECFO = CustomerForm()
    EPFO = CustomerProfileForm()
    return render(request, 'customer/customer_register.html', {'ECFO': ECFO, 'EPFO': EPFO})

def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO:
            if AUO.is_active:
                login(request, AUO)
                request.session['username'] = un
                return HttpResponseRedirect(reverse('home'))        
            messages.error(request, 'Your Credentials are Blocked.....')
            return render(request, 'customer/user_login.html')
        messages.error(request, 'invalid Credentials')
    return render(request, 'customer/user_login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def add_to_cart(request, pk):
    un = request.session.get('username')
    UO = User.objects.get(username=un)
    PO = Product.objects.get(pk=pk)
    cart = Cart(user=UO, product=PO)
    cart.save()
    return HttpResponseRedirect(reverse('cart'))


def cart(request):
    return render(request, 'customer/cart.html')