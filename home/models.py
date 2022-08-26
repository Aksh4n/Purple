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