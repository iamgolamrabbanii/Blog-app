from django.db import models

# Create your models here.
class profileInformations(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=1000)
    profilePic = models.ImageField(upload_to='uploads/', blank=True, null = True)
    
    def __str__(self):
        return self.username

class userPost(models.Model):
    theUser = models.CharField(max_length=150)
    title = models.CharField(max_length=50)
    description = models.TextField()

    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title