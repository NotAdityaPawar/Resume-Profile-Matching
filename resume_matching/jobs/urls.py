from django.urls import path

from .views import JobListView, JobDetailView,SignUp,AboutPage,ResumeMatch,ShowResult,JobRegister,JobDelete
urlpatterns = [
    path('',JobListView.as_view(),name = 'job_list'),
    path('<int:pk>',JobDetailView.as_view(),name = 'job_detail'),
    path('register',SignUp.as_view(),name ='register'),
    path('about',AboutPage,name = 'about'),
    path('resume',ResumeMatch,name = 'resume'),
    path('result',ShowResult,name = 'result'),
    path('add_job',JobRegister.as_view(),name = 'add_job'),
    path('delete_job/<int:pk>',JobDelete.as_view(),name = 'delete')
]