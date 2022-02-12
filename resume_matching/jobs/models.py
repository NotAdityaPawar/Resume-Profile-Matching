from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img  = models.ImageField(blank = True,null = True)
    location = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User,on_delete = models.CASCADE,default = '1',null = True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('job_detail',kwargs={'pk':self.pk})

class Candidate(models.Model):
    name = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.name