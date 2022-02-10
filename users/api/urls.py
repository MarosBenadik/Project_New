from django.urls import path
from django.views import View
from .views import CategoryList, SingleCategory, GetAllPhotos, UserView, ServicesView, GetUser, RegisterAPI, LoginAPI, WorkingHoursView



urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/category/<int:pk>/', SingleCategory.as_view()),
    path('all/', UserView.as_view()),
    path('user/<int:pk>/', GetUser.as_view()),
    path('user/<int:pk>/photos/', GetAllPhotos.as_view()),
    path('user/<int:pk>/working-hours/', WorkingHoursView.as_view()),
    path('categories/services/', ServicesView.as_view()),
    path('create-user/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),

]