from django.shortcuts import render

from .models import Job
from django.views import generic

from django.urls import reverse_lazy

from .forms import RegistrationForm

from django.http import HttpResponse
from django.shortcuts import render


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity




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



def AboutPage(request):
    return render(request,"about.html",{})


def ResumeMatch(request):
    return render(request,"resume.html",{})

def ShowResult(request):
    jd = request.GET['jd']
    resume = request.GET['resume']


    text = [resume,jd]

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)

    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2)

    context = {"data":matchPercentage}
    print("------------------------------------------------------------")
    print(matchPercentage)


    return render(request, "result.html",context)
