from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product/<str:pk>',views.review, name='product'),
    path('category/',views.category, name='category'),
    path('category/<str:foo>/',views.category_page, name='category_page'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('sign-up/',views.register, name='register'),
    path('update_user/',views.update_user, name='update_user'),
]