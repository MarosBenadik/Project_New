from django.urls import path
from django.views import View
from .views import Dashboard, Register, ProfileView, ProfileEditView



urlpatterns = [

    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('register/', Register.as_view(), name="register"),
    path('profile/<str:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
]