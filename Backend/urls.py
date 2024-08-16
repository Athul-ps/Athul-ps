from django.urls import path
from Backend import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addcat/',views.addcat,name="addcat"),
    path('cat_save/',views.cat_save,name="cat_save"),
    path('cat_display/',views.cat_display,name="cat_display"),
    path('edit_cat/<int:c_id>/',views.edit_cat,name="edit_cat"),
    path('cat_update/<int:c_id>/',views.cat_update,name="cat_update"),
    path('cat_delete/<int:c_id>/',views.cat_delete,name="cat_delete"),


    path('Addprod/',views.Addprod,name="Addprod"),
    path('prodsave/',views.prodsave,name="prodsave"),
    path('prodispaly/',views.prodispaly,name="prodispaly"),
    path('proedit/<int:p_id>/',views.proedit,name="proedit"),
    path('proupdate/<int:p_id>/',views.proupdate,name="proupdate"),
    path('prodelete/<int:p_id>/',views.prodelete,name="prodelete"),


    path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),


    path('dispaly_contact/',views.dispaly_contact,name="dispaly_contact"),
    path('delete_contact/<int:c_id>/',views.delete_contact,name="delete_contact"),
]