from django.shortcuts import redirect , render
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method =='POST':
        first_name =request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'This Username had already taken!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email had already taken!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username , first_name=first_name
                                                        ,last_name=last_name,email=email,password=password)
                    user.save()
                    messages.success(request,f'Account have created for {username}')
                    return redirect('login')
        else:
            messages.error(request,'Password Doesnot Match')
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method =='POST':
        username1 =request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username1,password=password1)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                messages.success(request,'You are now logged in !')
                return redirect('dashboard')
            else:
                messages.info(request,'Account Is Disabled!!!')
                return redirect('login')
        else:
            messages.info(request,'Invalid!!!')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')