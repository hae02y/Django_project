from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Gsuser
from .forms import LoginForm

def home(request):
    user_id = request.session.get('user')

    if user_id:
        gsuser = Gsuser.objects.get(pk = user_id )
        return HttpResponse(gsuser.username)

    return HttpResponse('home(login please)')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request,'login.html', {'form': form })
    

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail',None)
        password = request.POST.get('password', None)
        re_pass = request.POST.get('re-pass', None)

        res_data = {}

        if not (username and useremail and password and re_pass):
            res_data['error'] = '모든 값을 입력해주세요.'

        elif password != re_pass:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            gsuser = Gsuser(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )

            gsuser.save()

        return render(request, 'register.html', res_data)