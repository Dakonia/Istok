from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('', index, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('profile/<str:username>/order_history/', order_history, name='order_history'),
    path('profile/<str:username>/favorites/', favorites, name='favorites'),
    path('profile/<str:username>/bonus_program/', bonus_program, name='bonus_program'),
    path('company/', company, name='company'),
    path('', category_list, name='category_list'),
    path('category/<str:category_name>/', category_detail, name='category_detail'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
