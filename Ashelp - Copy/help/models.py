from django.db import models

from django.db import models
import datetime


class contectus(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()
    subject=models.CharField(max_length=40)
    discription=models.TextField()
    budget=models.IntegerField(default=0)

    def __str__(self):
        return self.name+"  "+self.email


class bloge(models.Model):
    heading=models.CharField(max_length=20)
    img=models.ImageField()
    details=models.TextField()
    dt=models.CharField(max_length=20)

    def __str__(self):
        return self.heading+"  "+self.dt
