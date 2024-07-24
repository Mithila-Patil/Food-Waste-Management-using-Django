from django import forms
from .models import ProjectRegister, ProjectRegister1, ProjectRegister11

class DonorForm(forms.ModelForm):
    class Meta:
        model = ProjectRegister
        fields = ('user_id', 'city', 'password')

class ReceiverForm(forms.ModelForm):
    class Meta:
        model = ProjectRegister1
        fields = ('user_id', 'city', 'password')

class DonorRegistrationForm(forms.ModelForm):
    class Meta:
        model = ProjectRegister11
        fields = ('name', 'city', 'phone', 'adderess', 'food_info', 'quantity', 'pick_up_date')
