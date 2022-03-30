from django.urls import path
from django.views import View
from .views import CategoryList, SingleCategory, UserView, ServicesView, GetUser, CreateUser



urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/category/<int:pk>/', SingleCategory.as_view(), name='category'),
    path('all/', UserView.as_view(), name='users'),
    path('user/<int:pk>/', GetUser.as_view(), name='user'),
    path('categories/services/', ServicesView.as_view(), name='services'),
    path('create-user/', CreateUser.as_view(), name='createUser'),
]