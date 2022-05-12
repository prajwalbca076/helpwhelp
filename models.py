from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=10)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

class Whelp(models.Model):
    whelp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    password = models.CharField(max_length=20)

class Post(models.Model):
    post_id = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    whelps = models.ForeignKey(Whelp, on_delete=models.CASCADE)
    age = models.IntegerField()
    posted_on = models.DateField()
    status = models.BooleanField(default=False)

def __str__(self):
    return self.username