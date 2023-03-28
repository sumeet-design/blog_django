from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(null= False, max_length= 150)
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    body = models.TextField(null=False)


    def __str__(self):
        return self.title
