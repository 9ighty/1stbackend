from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def index(request):
    return  render(request,'home.html',
                   {'name':'Jieun'})

def infor(request):
    # query data from model
    data = Post.objects.all()
    return render(request, 'infor.html', {'posts': data})


def home_(request):
    return  render(request, 'home.html')

def createform(request):
    return  render(request, 'form.html')

def loginform(request):
    return  render(request, 'login.html')

def login(request):
    username = request.POST['username']  # ในวงเล็บเป็น name ของ html 1
    password = request.POST['password']
    #login check userกับpass ใน database ว่าตรงกันไหม
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('/home')
    else:
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginform')


def addusers(request):
    username = request.POST['username']  # ในวงเล็บเป็น name ของ html 1
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username = username).exists():
            messages.info(request,'Username already exists')
            return redirect('/form')
        elif User.objects.filter(email = email).exists():
            messages.info(request,'Email already exists')
            return redirect('/form')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
            user.save()
            return redirect('/home')
    else:
        messages.info(request, 'Password not match !!')
        return redirect('/form')

    return render(requset, 'result.html')