from django.urls import path
from . import views
app_name = 'khata'
urlpatterns = [
    path('<int:id>/<str:name>/',views.show_account,name='account'),
    path('gave/',views.Gave.as_view(),name='gave'),
    path('update_gave/<int:pk>/<int:cust_id>/',views.Update_Gave.as_view(),name='update_gave'),
    path('got/',views.Got.as_view(),name='got'),
    path('update_got/<int:pk>/<int:cust_id>/',views.Update_Got.as_view(),name='update_got'),
    path('delete_account/<int:pk>/',views.Delete_Account.as_view(),name='delete_account'),

]
