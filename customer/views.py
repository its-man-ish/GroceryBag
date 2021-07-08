from django.shortcuts import render
from .models import Profile
from .forms import ProfileModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.views import generic
from django.urls import reverse_lazy




class UserSignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'customer/signup.html'
    success_url = reverse_lazy('login')
    

def MyProfile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None,request.FILES or None,instance=profile)

    update= False
    if request.method =='POST':
        if form.is_valid():
            form.save()
            update = True

    context = {
        'profile': profile,
        'form': form,
        'update': update,
    }

    return render(request,'customer/myprofile.html',context)