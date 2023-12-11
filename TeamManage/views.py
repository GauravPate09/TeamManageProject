from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .model import TeamManage
from django.shortcuts import render
from .forms import TeamMemberForm

# using form to add member and for this  path('add/', views.add_member),


class HomeView(View):
    def get(self,request):
        if request.method == 'POST':
            form = TeamMemberForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = TeamMemberForm()
        return render(request, 'index.html', {'form': form})

class ListDisplayView(View):
    def get(self, request):
        team_members = TeamManage.objects.all()
        return render(request, 'display.html', {'team_members': team_members})
#
class SubmitFormView(View):
    def get(self, request):
        team_members = TeamManage.objects.all()
        return render(request, 'display.html', {'team_members': team_members})

    # Handling form submission via POST method getting all the fields name,location,email,role
    def post(self, request):
        name = request.POST.get('name')
        location = request.POST.get('location')
        email = request.POST.get('email')
        role = request.POST.get('role')

        TeamManage.objects.create(
            name=name,
            location=location,
            email=email,
            role=role
        )
        return redirect('/ListDisplay/')
#
class EditMemberView(View):
    # for editing not using django form methods
    def get(self, request, member_id):
        team_member = TeamManage.objects.get(pk=member_id)
        return render(request, 'update.html', {'team_member': team_member})

    def post(self, request, member_id):
        member = TeamManage.objects.get(pk=member_id)
        member.name = request.POST.get('name')
        member.location = request.POST.get('location')
        member.email = request.POST.get('email')
        member.role = request.POST.get('role')
        member.save()
        return redirect('/ListDisplay/')

# View for deleting a team member.
class DeleteMemberView(View):
    def get(self, request, member_id):
        member = TeamManage.objects.get(pk=member_id)
        member.delete()
        return redirect('/ListDisplay/')