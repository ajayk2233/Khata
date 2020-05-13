from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import QueryDict
from .models import UserForm,UserProfileChange,ProfileForm,Profile
from Khata_Register.decorators import login_check
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.contrib.auth import update_session_auth_hash

@login_check
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/signin/')
        else:
            print('Not valid')
    elif request.method == 'GET':
        form = UserForm()
    return render(request,'users/signup.html',{'form':form})

@login_check
def signin(request):
    if request.method == 'POST':
        q_string = request.META['QUERY_STRING']
        q_dict = QueryDict(q_string)
        next = q_dict.get('next') or '/'
        try:
            username = request.POST['username']
            user = auth.authenticate(username=username,password=request.POST['password'])
            auth.login(request,user)
            request.session['login_check'] = 'Successfully Logged in!'
            return redirect(next)
        except:
            return render(request, 'users/signin.html',{'message':'Username or Password is not correct'})

    return render(request, 'users/signin.html')

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/users/signin')

def edit_profile(request):
    obj = Profile.objects.get(user = request.user.id)
    print(obj.address)
    if request.method == 'POST':
        user_form = UserProfileChange(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=obj)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')
        else:
            return HttpResponse('Not Valid Error: ',profile_form.errors)
    else:
        user_form = UserProfileChange(instance=request.user)
        profile_form = ProfileForm(instance=obj)
    return render(request,'users/profile.html',{'user':request.user,'user_form':user_form,'profile_form':profile_form})