from django.shortcuts import render,redirect
from Backend.models import cat_db,prod_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from frontend.models import contact_db
from django.contrib import messages

# Create your views here.


def indexpage(req):
    return render(req,"index.html")

def addcat(req):
    return render(req,"Addcategory.html")

def cat_save(req):
    if req.method == "POST":
        a=req.POST.get('name')
        b=req.POST.get('desc')
        c=req.FILES['imge']
        obj = cat_db(Name=a,Desc=b,Imge=c)
        obj.save()
        messages.success(req,"Category saved successfully")
        return redirect(addcat)

def cat_display(req):
    cat = cat_db.objects.all()
    return render(req,"catdisplay.html",{'cat':cat})

def edit_cat(req,c_id):
    cat = cat_db.objects.get(id=c_id)
    return render(req,"catedit.html",{'cat':cat})

def cat_update(req,c_id):
    if req.method == "POST":
        a = req.POST.get('name')
        b = req.POST.get('desc')
        try:
            img = req.FILES['imge']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = cat_db.objects.get(id=c_id).Imge
        cat_db.objects.filter(id=c_id).update(Name=a,Desc=b,Imge=file)
        return redirect(cat_display)

def cat_delete(req,c_id):
    cat = cat_db.objects.filter(id=c_id)
    cat.delete()
    messages.error(req, "Category saved successfully")
    return redirect(cat_display)

#              product

def Addprod(req):
    prod = cat_db.objects.all()
    return render(req,"Addproduct.html",{'prod':prod})

def prodsave(req):
    if req.method == "POST":
        a=req.POST.get('cname')
        b=req.POST.get('pname')
        c=req.POST.get('price')
        d=req.POST.get('desc')
        e=req.FILES['imges']
        obj = prod_db(Cname=a,Pname=b,Price=c,Descp=d,Imges=e)
        obj.save()
        messages.success(req, "Category saved successfully")
        return redirect(Addprod)

def prodispaly(req):
    prod = prod_db.objects.all()
    return render(req,"proddisplay.html",{'prod':prod})

def proedit(req,p_id):
    cat = cat_db.objects.all()
    prod = prod_db.objects.get(id=p_id)
    return render(req,"prodedit.html",{'cat':cat,'prod':prod})

def proupdate(req,p_id):
    if req.method == "POST":
        a=req.POST.get('cname')
        b=req.POST.get('pname')
        c=req.POST.get('price')
        d=req.POST.get('desc')
        try:
            img = req.FILES['imges']
            fs =  FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = prod_db.objects.get(id=p_id).Imges
        prod_db.objects.filter(id=p_id).update(Cname=a,Pname=b,Price=c,Descp=d,Imges=file)
        return redirect(prodispaly)

def prodelete(req,p_id):
    prod = prod_db.objects.filter(id=p_id)
    prod.delete()
    return redirect(prodispaly)

def admin_login_page(req):
    return render(req,"Admin_login.html")

def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('password')

        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                messages.success(request,"Welcome")
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(indexpage)
            else:
                messages.error(request, "Login failed")
                return redirect(admin_login_page)
        else:
            messages.error(request, "Login failed")
            return redirect(admin_login_page)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

def dispaly_contact(req):
    con = contact_db.objects.all()
    return render(req,"dispaly_contact.html",{'con':con})

def delete_contact(request,c_id):
    con = contact_db.objects.filter(id=c_id)
    con.delete()
    return redirect(dispaly_contact)







