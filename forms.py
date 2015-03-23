from django.forms import ModelForm

from models import MiniUrl


class MiniUrlForm(ModelForm):
    class Meta:
        model = MiniUrl
        fields = ['urlLong', 'pseudo']




