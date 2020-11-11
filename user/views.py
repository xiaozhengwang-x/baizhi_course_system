import random,string
import traceback
import hashlib
import uuid

from django.core.mail import send_mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.contrib.auth import settings
from django.db import transaction
from django.shortcuts import render,HttpResponse,redirect

from user.captcha.image import ImageCaptcha
from user.models import TUser
# Create your views here.
#注册
def register(request):
    return render(request,'user/register.html')


def register_logic(request):
    try:
        username=request.POST.get('user_name')
        password=request.POST.get('pwd')
        salt=str(uuid.uuid4())
        sha=hashlib.md5()
        sha.update((password+salt).encode())
        pwd=sha.hexdigest()
        print(pwd,11111)
        password1=request.POST.get('cpwd')
        email=request.POST.get('email')
        captcha=request.POST.get('captcha')
        if captcha.lower()==request.session.get("code").lower():
                user= TUser.objects.create(username=username,password=pwd,email=email,salt=salt,)
                if user:
                    ser = Serializer(settings.SECRET_KEY, expires_in=120)
                    result = ser.dumps({'id':user.id})
                    send_mail('激活账号',f'用户{username}请求激活账号，链接为：http://127.0.0.1:8000/user/active/?token='+result.decode('utf-8'),'2693606059@qq.com',['1926253863@qq.com'])
                    # return redirect("user:login")
                    return HttpResponse('yes')
        return HttpResponse("No")
    except:
        traceback.print_exc()
        return HttpResponse("no")


#激活
def active(request):
    try:
        token=request.GET.get('token')
        ser = Serializer(settings.SECRET_KEY, expires_in=120)
        print(token)
        print(123)
        result=ser.loads(token).get('id')
        print(result,type(result))
        user=TUser.objects.get(pk=result)
        user.is_active=True
        user.save()
        return HttpResponse("激活成功")
    except:
        traceback.print_exc()
        return HttpResponse('激活失败')





#登录

def login(request):
    username=request.COOKIES.get('username')
    if username:
        username = username.encode('latin-1').decode('utf-8')
        password=request.COOKIES.get('password')
        user=TUser.objects.filter(username=username,password=password)
        if user:
            request.session['is_login']=True
            return redirect("course:index")
        return render(request,'user/login.html')
    return render(request, 'user/login.html')


def login_logic(request):
    username=request.POST.get('username')
    password=request.POST.get('pwd')
    rem=request.POST.get('remember')
    name=TUser.objects.get(username=username)
    print(name)
    salt=name.salt
    # salt = str(uuid.uuid4())
    sha = hashlib.md5()
    sha.update((password + salt).encode())
    pwd = sha.hexdigest()
    print(pwd, 3333)
    # user=TUser.objects.filter(username=username,password=pwd,salt=salt)
    if pwd==name.password:
        if name.is_active:
            request.session['is_login']=True
            request.session['username']=username
            resp=HttpResponse('yes')
            if rem:
                username = username.encode('utf-8').decode('latin-1')
                resp.set_cookie("username",username,max_age=3600*24*7)
                resp.set_cookie("password",password,max_age=3600*24*7)
            return resp
        else:
            # return HttpResponse("账号为激活，是否重新发送邮件")
            return HttpResponse("n")
    return HttpResponse("no")
    # return render(request,'user/login.html')




#验证码
def get_captcha(request):
    # 声明一个验证码对象
    image = ImageCaptcha()
    # 生成随机码
    code = random.sample(string.ascii_letters+string.digits,4)
    code = "".join(code)
    print(code)
    request.session['code'] = code
    # 将码写入图片中
    data = image.generate(code)   #返回二进制数据
    return HttpResponse(data,'image/png')


#检测用户姓名
def register_username(request):
    username=request.POST.get("user_name")
    user=TUser.objects.filter(username=username)
    if user:
        return HttpResponse('no')
    return HttpResponse('yes')


#检测用户密码
def register_pwd(request):
    password=request.POST.get("pwd")
    password1=request.POST.get("cpwd")
    if password==password1:
        # return HttpResponse("no")
        # return HttpResponse("yes")
        return render(request, 'user/register.html')
    # return HttpResponse("no")
    return HttpResponse("两次密码不一致")
    # return HttpResponse("yes")

def logout(request):
    return render(request,'user/logout.html')