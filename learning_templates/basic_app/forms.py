from django import forms
class NameForm(forms.Form):
    name_field=forms.CharField(max_length=20)
    # class Meta:
    #     model=NameModel
    #     fields="__all__"