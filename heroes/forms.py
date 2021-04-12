from django import forms

from .models import Hero


# create a ModelForm
class HeroForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Hero
        fields = [
            "name",
            'alter_ego',
            'primary_ability',
            'secondary_ability',
            'catchphrase',
        ]
