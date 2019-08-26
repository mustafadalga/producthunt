from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if username=="" or password1=="" or password2=="":
            messages.error(request,'Lütfen boş alan bırakmayınız!')
            return render(request, 'accounts/signup.html')
        else:
            if request.POST['password1'] != request.POST['password2']:
                messages.error(request, 'Parolalar eşleşmiyor!')
                return render(request, 'accounts/signup.html', )
            else:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    messages.error(request, 'Böyle bir kullanıcı adı zaten kullanılıyor!')
                    return render(request, 'accounts/signup.html')
                except User.DoesNotExist:
                    user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                    messages.success(request,'Başarıyla kayıt oldunuz.Giriş yapabilirsiniz')
                    return redirect('home')
    else:
        return render(request,'accounts/signup.html')


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Hoşgeldin '+str(request.user))
            return redirect('home')
        else:
            messages.error(request,'Giriş bilgileriniz hatalı!')
            return render(request, 'accounts/login.html')

    else:
        return render(request,'accounts/login.html')


def logout(request):
    auth.logout(request)
    return  redirect('home')
