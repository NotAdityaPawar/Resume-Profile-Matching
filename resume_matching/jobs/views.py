from django.shortcuts import render

from .models import Job
from django.views import generic

from django.urls import reverse_lazy

from .forms import RegistrationForm


class JobListView (generic.ListView):
    model = Job
    template_name = 'joblist.html'
    context_object_name = 'jobs'
    ordering = ["-id"]


class JobDetailView(generic.DetailView):
    model = Job
    template_name = 'jobdetail.html'


class SignUp(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

