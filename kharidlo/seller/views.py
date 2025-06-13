from django.shortcuts import render
from seller.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'seller/seller_home.html')

def seller_register(request):
    if request.method == 'POST' and request.FILES:
        seller_user_object = SellerForm(request.POST)
        seller_profile_object = SellerProfileForm(request.POST, request.FILES)
        if seller_user_object.is_valid() and seller_profile_object.is_valid():
            MUFDO = seller_user_object.save(commit=False)
            MPFDO = seller_profile_object.save(commit=False)
            MUFDO.set_password(seller_user_object.cleaned_data.get('password'))
            MUFDO.is_staff = True
            MUFDO.save()
            MPFDO.user=MUFDO
            MPFDO.save()
            return HttpResponseRedirect(reverse('seller_login'))
        messages.error(request, 'invalid data')
    empty_seller_form= SellerForm()
    empty_seller_profile_form = SellerProfileForm()
    d = {'empty_seller_form': empty_seller_form, 'empty_seller_profile_form': empty_seller_profile_form}
    return render(request, 'seller/seller_register.html', d)

def seller_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO:
            if AUO.is_active:
                if AUO.is_staff:
                    login(request, AUO)
                    request.session['username'] = un
                    return HttpResponseRedirect(reverse('seller_home'))
                messages.error(request, 'You Are not a seller please login as a customer')
                return render(request, 'seller/seller_login.html')
            messages.error(request, 'Your Credentials are Blocked.....')
            return render(request, 'seller/seller_login.html')
        messages.error(request, 'invalid Credentials')
    return render(request, 'seller/seller_login.html')

def seller_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('seller_home'))


def add_product(request):
    if request.method == 'POST' and request.FILES:
        PFDO = ProductForm(request.POST, request.FILES)
        if PFDO.is_valid():
            un = request.session.get('username')
            seller = User.objects.get(username=un)
            MPFDO = PFDO.save(commit=False)
            MPFDO.seller=seller
            MPFDO.save()
            messages.info(request, 'Product Added Successfully')
            return HttpResponseRedirect(reverse('my_products'))
        messages.error(request, 'invalid data')
    EPFO = ProductForm()
    d = {'EPFO': EPFO}
    return render(request, 'seller/add_product.html', d)

def my_products(request):
    return render(request, 'seller/my_products.html')


def search(request):
    if request.method == 'POST':
        pid = request.POST.get('product')
        product = Product.objects.get(pid=pid)
        return render(request, 'seller/seller_search.html', {'product': product})
    return HttpResponseRedirect(reverse('seller_login'))


def update_item(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        pname = request.POST.get('pname')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        stock = request.POST.get('stock')
        discount = request.POST.get('discount')
        product.pname = pname
        product.desc = desc
        product.price = price
        product.category = category
        product.brand = brand
        product.stock = stock
        product.discount = discount
        product.save()
        return HttpResponseRedirect(reverse('my_products'))        
    return render(request, 'seller/update_item.html', {'product': product})       