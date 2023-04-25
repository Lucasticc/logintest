from django.db import models
from django.shortcuts import render,redirect
from logintest.models import Userinfo

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = Userinfo.objects.filter(username=username, password=password).first()
    username = Userinfo.objects.filter(username = username).first()
    username = username.username

    if not user_obj:
        return redirect("/login/")
    else:
        rep = redirect("/index/")
        rep.set_cookie('is_login',True)
        request.session['user1'] = username 

        return rep
       
def index(request):
    # print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    # status = request.session.get('is_login')
    username = request.session.get('user1')
    # username = request.COOKIES.get('USER')

    if not status:
        return redirect('/login/')
    return render(request, "index.html",{'m':username})


def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    request.session.flush() # 删除一条记录包括(session_key session_data expire_date)三个字段
    return rep # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面
   
def order(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, "order.html")    