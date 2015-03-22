from django.shortcuts import render

from mini_url.forms import MiniUrlForm


# Create your views here.

def add_mini(request):
    if request.method == 'POST' :
        form = MiniUrlForm(request.POST)

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            urlLong = form.cleaned_data['urlLong']
            pseudo = form.cleaned_data['pseudo']

            envoi = True

        else: # Si ce n'est pas du POST, c'est probablement une requête GET
            form = MiniUrlForm()  # Nous créons un formulaire vide

    return render(request, 'miniUrl/add_mini.html', locals())

