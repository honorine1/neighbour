from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import User,Profile,Post
from .forms import ProfileForm,PostForm

# Create your views here.

def index(request):
    current_user = request.user
    images= Post.objects.all().order_by("posted_date")
    profile= Profile.objects.all()
    
    return render(request,'neighbour/index.html',{"images":images,"profile":profile})

    # return render(request, 'neighbour/index.html')

@login_required(login_url='/accounts/login/')
def viewProject_details(request):
    current_user = request.user
    image= Post.objects.all().order_by("posted_date")
    
    profile= Profile.objects.all()
    
    return render(request,'neighbour/post.html',{"images":image,"profile":profile})


@login_required(login_url='/accounts/login/')
def project_posts(request, post_id):
    try:
        posts = Post.objects.all().order_by('posted_date')
       
    except DoesNotExist:
        raise Http404()
    return render(request,"neighbour/post_post.html", {"posts":posts})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.user = current_user
            projects.save()
            return redirect('index')

    else:
        form = PostForm()
    return render(request, 'neighbour/post_form.html', {"form": form})


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

    post = Post.objects.filter(user__username=current_user)


    profile = Profile.objects.filter(user__username = current_user)

    return render(request,"neighbour/profile.html",{"user":user,"profile":profile,"post":post})

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

