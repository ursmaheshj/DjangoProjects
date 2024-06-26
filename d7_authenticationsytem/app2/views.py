from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from app2.forms import MyUserChangeForm,MyAdminUserChangeForm
from django.contrib.auth.models import User


# Create your views here.
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request,request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'User has been logged in!!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request,'app2/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')
    
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                users = User.objects.all()
                fm = MyAdminUserChangeForm(request.POST,instance=request.user)
            else:
                users = None
                fm = MyUserChangeForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'User details successfully updated!!')
        else:
            if request.user.is_superuser == True:
                users = User.objects.all()
                fm = MyAdminUserChangeForm(instance=request.user)
            else:
                users = None
                fm = MyUserChangeForm(instance=request.user)
        return render(request,'app2/profile.html',{'name':request.user,'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/login/')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def changepassold(request):
    if request.user.is_authenticated:
        fm = PasswordChangeForm(request.user)
        if request.method == 'POST':
            fm = PasswordChangeForm(request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'User password changed!!')
                return HttpResponseRedirect('/profile/')
        return render(request,'app2/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def changepass(request):
    if request.user.is_authenticated:
        fm = SetPasswordForm(request.user)
        if request.method == 'POST':
            fm = SetPasswordForm(request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'User password changed!!')
                return HttpResponseRedirect('/profile/')
        return render(request,'app2/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def userdetail(request,id):
    if request.user.is_authenticated:
        user = User.objects.get(id=id)
        fm = MyAdminUserChangeForm(instance=user)
        return render(request,'app2/userdetail.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')