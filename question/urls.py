from django.urls import path
from .views import Questions, QuestionView, CreateQuestion, UpdateQuestion, DeleteQuestion, DeleteMesage

urlpatterns = [
    path('', Questions.as_view(), name='home'),
    path('question/<str:pk>/', QuestionView.as_view(), name='question'),
    path('create-questin/', CreateQuestion.as_view(), name="create-question"),
    path('update-questin/<str:pk>/', UpdateQuestion.as_view(), name="update-question"),
    path('delete-question/<str:pk>/', DeleteQuestion.as_view(), name="delete-question"),
    path('delete-message/<str:pk>/', DeleteMesage.as_view(), name="delete-message"),
]