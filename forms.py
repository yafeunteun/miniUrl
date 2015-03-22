from django.forms import forms

from models import MiniUrl


class MiniUrlForm(forms.ModelForm):
    class Meta:
        model = MiniUrl
        fields = ['urlLong', 'pseudo']




