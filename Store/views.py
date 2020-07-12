from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from .forms import CartAddProductForm,OrderCreateForm
from Vendor.models import ProductDetails, Regisvendor
from .cart import Cart
from Store.forms import SignUpForm
from .models import OrderItem
from django.core.mail import send_mail



def index(request):

    ob = ProductDetails.objects.all()

    return render(request, 'index.html', {'ob': ob})



def login1(request):
    if request.method == 'POST' and request.POST.get('register') == 'sign_up' :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login1)
    elif request.method == 'POST' and request.POST.get('submit') == 'sign_in':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(user_login)
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login1.html', {})

    return render(request, 'login1.html', {'form': form})

@login_required(login_url='/Store/login1')
def user_login(request):
    ob = ProductDetails.objects.all()[2:]

    return render(request, 'user_login.html', {'ob': ob})


def product(request, id):
    product = get_object_or_404(ProductDetails, id=id)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }

    return render(request, 'product.html', context)


def logout(request):
    auth.logout(request)
    return redirect(index)




def cart_add(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object
    product = get_object_or_404(ProductDetails, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductDetails, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})

    return render(request, 'cart.html', {'cart': cart})

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()

        return render(request, 'user_login.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'create.html', {'form': form, 'cart':cart})
