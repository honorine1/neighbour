from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import User,Profile,Post
from .forms import ProfileForm,PostForm

# Create your views here.

def index(request):
    return render(request, 'neighbour/index.html')

def profile(request,user_id ):

    current_user = request.user.username
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('index')

    else:
        form = ProfileForm()

    user=User.objects.all()

    # proImage = Projects.objects.filter(user__username=current_user)


    profile = Profile.objects.filter(user__username = current_user)

    return render(request,"neighbour/profile.html",{"user":user,"profile":profile})

@login_required(login_url='/accounts/login/')
def update_profile(request):

    current_user=request.user
    if request.method =='POST':
        if Profile.objects.filter(user_id=current_user).exists():
            form = ProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
        else:
            form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
          profile=form.save(commit=False)
          profile.user=current_user
          profile.save()
          return redirect('profile',current_user.id)
    else:

        if Profile.objects.filter(user_id = current_user).exists():
           form=ProfileForm(instance =Profile.objects.get(user_id=current_user))
        else:
            form=ProfileForm()

    return render(request,'neighbour/profile_form.html',{"form":form}) 

