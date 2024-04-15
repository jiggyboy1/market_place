from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product/<str:pk>',views.review, name='product'),
    path('category/',views.category, name='category'),
    path('category/<str:foo>/',views.category_page, name='category_page'),
    
]