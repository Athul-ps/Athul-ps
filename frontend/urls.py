from django.urls import path
from frontend import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('productfn/<catname>/',views.productfn,name="productfn"),
    path('aboutfn/',views.aboutfn,name="aboutfn"),
    path('conatcfn/',views.conatcfn,name="conatcfn"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('singelprod/<int:p_id>/',views.singelprod,name="singelprod"),
    path('userloginfn/',views.userloginfn,name="userloginfn"),
    path('save_user/',views.save_user,name="save_user"),
    path('loginuser/',views.loginuser,name="loginuser"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cart_save/',views.cart_save,name="cart_save"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('cart_delete/<int:c_id>/',views.cart_delete,name="cart_delete"),
    path('checkout/',views.checkout,name="checkout"),
    path('user_details/',views.user_details,name="user_details"),

]
