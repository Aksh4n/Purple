from django.db import models

# Create your models here.
class Honor(models.Model):
    subject = models.CharField(max_length=200)
    img = models.ImageField()


    def __str__(self):

        return self.subject  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url            
class Project(models.Model):
    subject = models.CharField(max_length=200)
    img = models.ImageField()


    def __str__(self):

        return self.subject  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
class Video(models.Model):
    subject = models.CharField(max_length=200)
    img = models.FileField()


    def __str__(self):

        return self.subject  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


class Blok(models.Model):
    subject = models.CharField(max_length=200)
    img = models.ImageField()


    def __str__(self):

        return self.subject  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
class Foam(models.Model):
    subject = models.CharField(max_length=200)
    img = models.ImageField()


    def __str__(self):

        return self.subject  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
class Tirche(models.Model):
    subject = models.CharField(max_length=200)
    img = models.ImageField()


    def __str__(self):

        return self.subject  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
