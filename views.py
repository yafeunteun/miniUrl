# -*- coding: utf8 -*-
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.core.exceptions import ValidationError

from mini_url.forms import MiniUrlForm
from mini_url.models import MiniUrl

def accueil(request):
    urls = MiniUrl.objects.order_by('-nbAccess')
    return render(request, 'mini_url/accueil.html', {'url_all' : urls})




def redir(request, code):
   url = get_object_or_404(MiniUrl, code=code)
   currentAccessCount = url.nbAccess
   url.nbAccess = currentAccessCount + 1
   url.save()
   return redirect(url.urlLong)





def add_mini(request):
    if request.method == 'POST' :
        form = MiniUrlForm(request.POST)

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            urlLong = form.cleaned_data['urlLong']
            pseudo = form.cleaned_data['pseudo']

            try:
                form.full_clean()
            except ValidationError as e:
                # Do something based on the errors contained in e.message_dict.
                # Display them to a user, or handle them programmatically.
                pass

            form.save()
            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = MiniUrlForm()  # Nous créons un formulaire vide

    return render(request, 'mini_url/add_mini.html', locals())





