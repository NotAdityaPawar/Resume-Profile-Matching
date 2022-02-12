from django.urls import path

from .views import JobListView, JobDetailView,SignUp
urlpatterns = [
    path('',JobListView.as_view(),name = 'job_list'),
    path('<int:pk>',JobDetailView.as_view(),name = 'job_detail'),
    path('register',SignUp.as_view(),name ='register')
]