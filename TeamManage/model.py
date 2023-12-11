from django.db import models

# from django import forms
# from .models import TeamMember

# class TeamMemberForm(forms.ModelForm):
#     class Meta:
#         model = TeamMember
#         fields = ['name', 'location', 'email', 'role']

#
class TeamManage(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=20)
# Assuming  here that roles can be either 'admin' or 'non-admin' as we used radio button in frontend

# class TeamManage(models.Model):
#         name = models.CharField(max_length=100)
#         location = models.CharField(max_length=100)
#         email = models.EmailField()
#         role = models.CharField(max_length=20)

    # Assuming  here that roles can be either 'admin' or 'non-admin' as we used radio button in frontend
    #     def __str__(self):
    #         return f'{self.name}'