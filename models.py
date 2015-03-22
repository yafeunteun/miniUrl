from django.db import models

# Create your models here.


class MiniUrl(models.Model):
    urlLong = models.URLField(unique=True) # url longue
    code = models.CharField(max_length=45, unique=True)
    dateCreation = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de creation")
    pseudo = models.CharField(max_length=45, null=True) # optionnel
    nbAccess = models.IntegerField(default=0) # nombre d'acces ie de redirections
