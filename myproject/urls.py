from django.contrib import admin
from django.urls import path
from comments import views
from django.conf.urls.static import static 
from comments.views import shop_view, trener_view, cart_view
from django.conf import settings

urlpatterns = [     
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('shop/', shop_view, name='shop'),
    path('trener/', trener_view, name='trener'),
    
    path('cart/', cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('change-quantity/<int:item_id>/', views.change_quantity, name='change_quantity'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)