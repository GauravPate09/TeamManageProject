"""
URL configuration for TeamManage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import HomeView, ListDisplayView, SubmitFormView, EditMemberView, DeleteMemberView


urlpatterns = [
     path('home/', HomeView.as_view(), name='home'),
     path('', HomeView.as_view(), name='home'),
     path('ListDisplay/', ListDisplayView.as_view(), name='list_display'),
     path('submit/', SubmitFormView.as_view(), name='submit_form'),
     path('editMember/<int:member_id>/', EditMemberView.as_view(), name='edit_member'),
     path('deleteMember/<int:member_id>/', DeleteMemberView.as_view(), name='delete_member'),


    # path('admin/', admin.site.urls),
    # path('home/', views.home),
    # path('submit/', views.submit_form),
    # path('ListDisplay/', views.listDisplay),
    # path('deleteMember/<int:member_id>/', views.deleteMember),
    # path('editMember/<int:member_id>/', views.editMember),
    # path('editMember/',views.editMember)

]
