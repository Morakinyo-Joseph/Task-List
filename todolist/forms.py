from django import forms


class CreateNewTask(forms.Form):
    name = forms.CharField(label='Name', max_length=250)
    Are_you_sure = forms.BooleanField(required=True)