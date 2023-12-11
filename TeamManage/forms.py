from django import forms

class TeamMemberForm(forms.Form):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('non-admin', 'Non-Admin'),
    )
    name=forms.CharField(max_length=20)
    location= forms.CharField(max_length=20)
    email = forms.EmailField()
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)
