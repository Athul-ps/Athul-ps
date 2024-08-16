from django.shortcuts import render,redirect
from Backend.models import prod_db,cat_db
from frontend.models import contact_db,reg_db,Cart_db,checkout_db
from django.contrib import messages

# Create your views here.

def homepage(request):
    pro = prod_db.objects.all()
    cat = cat_db.objects.all()
    return render(request,"Homepage.html",{'pro':pro,'cat':cat })

def productfn(request,catname):
    pro = prod_db.objects.filter(Cname=catname)
    cat = cat_db.objects.all()
    return render(request,"product.html",{'pro':pro,'cat':cat } )

def aboutfn(request):
    cat = cat_db.objects.all()
    return render(request,"about.html",{'cat':cat })

def conatcfn(req):
    cat = cat_db.objects.all()
    return render(req,"contact.html",{'cat':cat })

def singelprod(request,p_id):
    pro = prod_db.objects.get(id=p_id)
    return render(request,"singleproduct.html", {'pro':pro})

def save_contact(request):
    if request.method == "POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('msg')
        obj = contact_db(Name=a,Email=b,Msg=c)
        obj.save()
        return redirect(conatcfn)

def userloginfn(req):
    return render(req,"userlogin.html")

def save_user(request):
    if request.method == "POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('pass')
        obj = reg_db(Name=a,Email=b,Password=c)
        obj.save()
        messages.success(request, "User registration successful")
        return redirect(userloginfn)

def loginuser(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('password')
        if reg_db.objects.filter(Name=un,Password=pwd).exists():
            request.session['Name']=un
            request.session['Password']=pwd
            messages.success(request,"Welcome")
            return redirect(homepage)
        else:
            messages.error(request, "login failed")
            return redirect(userloginfn)
    else:
        messages.error(request, "login failed")
        return redirect(userloginfn)

def userlogout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(userloginfn)

def cart_save(request):
    if request.method == "POST":
        a=request.POST.get('name')
        b=request.POST.get('pname')
        c=request.POST.get('qty')
        d=request.POST.get('price')
        e=request.POST.get('total')
        obj = Cart_db(username=a,proname=b,Qty=c,price=d,totalprice=e)
        obj.save()
        messages.success(request, "item added to cart")
        return redirect(homepage)

def cartpage(request):
    cat = cat_db.objects.all()
    data = Cart_db.objects.filter(username=request.session['Name'])
    total_price = 0
    for i in data:
        total_price = total_price+i.totalprice
    return render(request,"cart.html",{'cat':cat,'data':data, 'total_price':total_price})

def cart_delete(request,c_id):
    x = Cart_db.objects.filter(id=c_id)
    x.delete()
    return redirect(cartpage)

def checkout(request):
    cat = cat_db.objects.all()
    data = Cart_db.objects.filter(username=request.session['Name'])
    total_price = 0
    for i in data:
        total_price = total_price + i.totalprice
    return render(request,"checkout.html",{'cat':cat,'data':data,'total_price':total_price})

def user_details(request):
    if request.method == "POST":
        a=request.POST.get('fname')
        b=request.POST.get('lname')
        c=request.POST.get('addr')
        d=request.POST.get('town')
        e=request.POST.get('country')
        f=request.POST.get('code')
        g=request.POST.get('mobile')
        h=request.POST.get('emailadd')
        obj = checkout_db(Fname=a,Lname=b,Addr=c,Town=d,Country=e,passcode=f,Mobile=g,Email=h)
        obj.save()
        return redirect(checkout)


