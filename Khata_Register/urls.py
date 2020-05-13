
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls',namespace='khata')),
    path('users/',include('user_app.urls')),
    path('',include('customer_app.urls',namespace='customer')),
    path('about/',views.about,name='about'),
    path('previous_url',views.previous_url,name='previous_url'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
