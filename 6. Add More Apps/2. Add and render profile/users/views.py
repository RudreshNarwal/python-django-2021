from django.shortcuts import render
from .models import Profile


# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkill = profile.skill_set.exclude(description__exact="")
    otherSkill = profile.skill_set.filter(description__exact="")

    context = {'profile': profile, 'topSkill': topSkill, 'otherSkill': otherSkill}
    return render(request, 'users/user-profile.html', context)
