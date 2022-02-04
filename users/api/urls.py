from django.urls import path
from django.views import View
from .views import CategoryList, SingleCategory, UserView, ServicesView, GetUser, CreateUser



urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/category/<int:pk>/', SingleCategory.as_view()),
    path('all/', UserView.as_view()),
    path('user/<int:pk>/', GetUser.as_view()),
    path('categories/services/', ServicesView.as_view()),
    path('create-user/', CreateUser.as_view()),
]