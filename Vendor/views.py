from django.shortcuts import render,redirect
from .models import Regisvendor,ProductDetails
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def home(request):
    #if request.method == 'POST':
        #return render(request, 'registervendor.html')

    return render(request, 'home.html')

def registervendor(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,password=password)
        mobileno = request.POST.get('mobileno')
        address = request.POST.get('address')
        gstno = request.POST.get('gstno')
        adhar = request.POST.get('adhar')
        vendor = Regisvendor( mobileno=mobileno, address=address, gstno=gstno, adhar=adhar, user=user)
        vendor.save()
        print(user)
        return redirect(loginvendor)

    return render(request, 'registervendor.html' )

def loginvendor(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        shopname = request.POST.get('shopname')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(dashboard, ven_id=shopname)

        else:
            return HttpResponse("Your account was inactive.")
    else:
        return render(request, 'loginvendor.html')


@login_required(login_url='/Vendor/signin')
def addproduct(request,ven_id):
    if request.method == 'POST':

        prod_tittle = request.POST.get('prod_tittle')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        imag=request.FILES['imag']


        product = ProductDetails(prod_tittle=prod_tittle, description=description, category=category, price=price, stock=stock,imag=imag,ven_id=Regisvendor.objects.get(ven_id=ven_id))


        product.save()
        return redirect(dashboard, ven_id=ven_id)


    return render(request, 'addproduct.html')


@login_required(login_url='/Vendor/signin')
def dashboard(request, ven_id):
    ab=Regisvendor.objects.get(ven_id=ven_id)
    obj=ProductDetails.objects.filter(ven_id=ven_id)
    return render(request,'dashboard.html',{'obj':obj, 'ab':ab})
def logout(request):
    auth.logout(request)
    return redirect(loginvendor)