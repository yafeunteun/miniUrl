# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
import random
import string

class MiniUrl(models.Model):
    urlLong = models.URLField(unique=True, verbose_name='URL à réduire') # url longue
    code = models.CharField(max_length=10, unique=True)
    dateCreation = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de creation")
    pseudo = models.CharField(max_length=45, null=True) # optionnel
    nbAccess = models.IntegerField(default=0) # nombre d'acces ie de redirections

    def generer(self, nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
        return ''.join(aleatoire)

    def full_clean(self, exclude=None, validate_unique=True):
        print('full_clean called')
        self.code = self.generer(10)

