from django.db import models

# Create your models here.


class MiniUrl(models.Model):
    urlLong = models.UrlField(unique=True) # url longue
    code = models.CharField(unique=True) # code de l'url minifiée
    dateCreation = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de création")
    pseudo = models.CharField(null=True) # optionnel
    nbAccess = models.IntegerField(default=0) # nombre d'accès ie de redirections
