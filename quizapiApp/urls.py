from django.urls import path
from . import views

urlpatterns = [

    path('quiz_register', views.quizRegisterAPIView.as_view(), name='quiz_register'),

    path('get_quiz', views.get_quizAPIView.as_view(), name='get_quiz'),
    path('delete_quiz/<int:id>', views.delete_quizAPIView.as_view(), name='delete_quiz'),
    path('update_quiz/<int:id>', views.update_quizAPIView.as_view(), name='update_quiz'),
    path('single_quiz/<int:id>', views.SingleQuizAPIView.as_view(), name='single_quiz'),

]