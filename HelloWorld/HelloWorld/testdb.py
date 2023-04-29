from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth
from TestModel.models import User,BlogType,TTag,TBlog
from datetime import datetime


# 数据库操作
def testdb(request):
    if request.method == 'POST':
        username = request.POST.get('username')#123
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            passworddb = User.objects.get(username=username)
            pw = passworddb.password
            if password == pw:
                rep = redirect("/index/")
                rep.set_cookie("is_login",True)
                request.session['user1'] = username
                return rep
            else:
                return render(request, 'login.html', {"error": "用户名不存在或密码错误"})
        else:
            return render(request, 'login.html', {"error": "用户名不存在或密码错误"})
    return render(request, 'login.html')


def index(request):
        status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
        if not status:
            return redirect('/login/')
        username = request.session.get('user1')
        UserID=User.objects.filter(username=username).first().id
        details = TBlog.objects.filter(id=UserID).all()
        temp = []
        for detail in details:
            temp.append(detail.blog_title)
            temp.append(detail.blog_content)
        return render(request, "index.html",{'m':username,'details':temp})


def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists(): 
            return render(request, 'sign.html', {"error": "用户名重复"})
        passwordin = request.POST.get('password')
        phone = request.POST.get('phone')
        if username and passwordin:
            s = User(username=username, password=passwordin,phone= phone,register_time=datetime.now())
            s.save()
            return render(request, 'login.html', {"error": "注册成功请重新登录哦"})
        else:
            return render(request, 'sign.html', {"error": "请注册"})
    return render(request, 'sign.html')

def rtin(request):
    if request.method == 'POST':
        return render(request, 'login.html')

def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    request.session.flush() # 删除一条记录包括(session_key session_data expire_date)三个字段
    return rep # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面
def upload(request):
    if request.method == 'POST':
        username = request.session.get('user1')
        blog_title = request.POST.get('blog_title')
        blog_content = request.POST.get('blog_content')
        type_name = request.POST.get('type')
        type_id = BlogType.objects.filter(type_name=type_name).first().type_id
        id = User.objects.filter(username = username).first()
        s = TBlog(id=id,type_id=type_id,blog_title=blog_title,blog_content=blog_content,blog_status=1,create_time=datetime.now())
        s.save()
        return redirect('/index/')

def ShowBlogDetail(request):
    return 