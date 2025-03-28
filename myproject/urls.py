from django.contrib import admin
from django.urls import path
from comments import views
from django.conf.urls.static import static 
from comments.views import shop_view
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('shop/', shop_view, name='shop'),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)