from django.urls import path
from . import views
app_name = 'customer'
urlpatterns = [
    path('',views.show_customer,name='show_customer'),
    path('<int:id>/',views.show_customer,name='show_customer'),
    path('add_customer/',views.Add_Customer.as_view(),name='add_customer'),
    path('update_customer/<int:pk>/',views.Update_Customer.as_view(),name='update_customer'),
    path('delete_customer/<int:pk>/',views.Delete_Customer.as_view(),name='delete_customer'),
]
