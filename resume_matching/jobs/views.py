from django.shortcuts import render

from .models import Job
from django.views import generic

from django.urls import reverse_lazy

from .forms import RegistrationForm, AddJob

from django.http import HttpResponse
from django.shortcuts import render


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from jobs.customFunctions import *


class JobListView (generic.ListView):
    model = Job
    template_name = 'joblist.html'
    context_object_name = 'jobs'
    ordering = ["-id"]


class JobDetailView(generic.DetailView):
    model = Job
    template_name = 'jobdetail.html'

class JobDelete(generic.DeleteView):
    model = Job
    success_url = reverse_lazy('job_list')
    template_name = 'delete_job.html'



class SignUp(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        print("----------------------------")
        print(self.object.data)
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

class JobRegister(generic.CreateView):
    form_class = AddJob
    success_url = reverse_lazy('job_list')
    template_name = 'addjob.html'

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()

        if self.request.method == "POST":
            print("-------------------------------")
            print(form_kwargs)
            form_kwargs['data']._mutable=True
            form_kwargs['data']['posted_by'] = str(self.request.user.id)

        return form_kwargs






def AboutPage(request):
    return render(request,"about.html",{})


def ResumeMatch(request):
    return render(request,"resume.html",{})

def ShowResult(request):
    print(request)
    jd = request.POST['jd']
    resume = request.POST['resume']
    print(resume)

    file =  request.FILES['file'] if request.FILES['file'] else False

    jd = cleanText(jd)
    resume = cleanText(resume)

    text = [resume,jd]



    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)

    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2)

    context = {"data":matchPercentage}
    print("------------------------------------------------------------")
    print(matchPercentage)


    return render(request, "result.html",context)
