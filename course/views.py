import traceback

from django.core.paginator import Paginator
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse

from course.models import TArticle,TCategory
# Create your views here.


def index(request):
     article = TArticle.objects.all()
     sort = request.GET.get('sort')
     print(sort,777777777)
     if sort == '1':
          article = TArticle.objects.all().order_by('count')
     elif sort == '2':
          article = TArticle.objects.all().order_by('publish_time')
     cates=TCategory.objects.filter(level=1)
     sub_cates=TCategory.objects.filter(level=2)
     level=request.GET.get('level')
     number = request.GET.get('number', request.session.get('number', 1))
     id = request.GET.get('id', request.session.get('id'))
     if id:
         if not TArticle.objects.filter(cate_id=id):
             article=TArticle.objects.filter(cate__parent_id=id)
         else:
             article=TArticle.objects.filter(cate_id=id)  #二级对象
     for i in article:
         print(i.title)
     request.session['id']=id
     request.session['number']=number
     pagtor=Paginator(object_list=article,per_page=3)
     page = pagtor.page(number)
     username=request.session.get('username')
     print(username)
     return render(request,'course/index.html',{'username':username,'cates':cates,'sub_cates':sub_cates,
                                                'page':page,'level':level,'id':id})



def pythonBase(request):
    cates = TCategory.objects.filter(level=1)
    sub_cates = TCategory.objects.filter(level=2)
    id=request.GET.get('id')
    print(id,4444)
    number = request.GET.get('number',1)
    level=request.GET.get('level')
    print(level)
    try:
        if level=='1':
           parent=TCategory.objects.filter(parent_id=id)
           name_title = TCategory.objects.filter(pk=id)[0].title
           print(name_title,666666)
           list=[]
           for i in parent:
               list.extend(TArticle.objects.filter(cate_id=i.id))
               print(list)
           pagtor = Paginator(object_list= list, per_page=4)
           page = pagtor.page(number)
           username = request.session.get('username')
           return render(request,'course/pythonBase.html',{'sub_cates':sub_cates,'page':page,'username':username,
                                                           'cates':cates,'level':level,'name_title':name_title,'id':id})
        elif level=='2':
            title = TCategory.objects.get(pk=id)
            name_title=TCategory.objects.get(id=title.parent_id).title
            cat=TArticle.objects.filter(cate_id=id)
            sub_cates_name=TCategory.objects.get(pk=id).title
            pagtor = Paginator(object_list=cat, per_page=4)
            page = pagtor.page(number)
            print(page,5555)
            username = request.session.get('username')
            return render(request, 'course/pythonBase.html', {'name_title':name_title,'sub_cates_name':sub_cates_name,'username':username,
                                                         'cates': cates, 'page': page,'sub_cates':sub_cates,'level':level,'id':id})

    except:
        return render(request,'course/index.html')



#增加文章
def addArticle(request):
    cates = TCategory.objects.filter(level=1)
    sub_cates = TCategory.objects.filter(level=2)
    username = request.session.get('username')
    id=request.GET.get('id')
    print(id)
    level=request.GET.get('level')
    print(level)
    return render(request,'course/addArticle.html',{"cates":cates,'sub_cates':sub_cates,'level':level,'id':id,'username':username})




def addArticle_logic(request):
    try:
        level=request.POST.get('level')
        print(level,8888899999)
        article = request.POST.get('article')
        print(article,1)
        course = request.POST.get('course_sel')
        sel = request.POST.get('cate_sel')
        time=request.POST.get('time')
        details=request.POST.get('details')
        username = request.session.get('username')
        print(77777,course,sel)
        # level = TCategory.objects.get(title=course).level
        if article=="":
            return HttpResponse("该文章名称不能为空！")
        if TCategory.objects.get(id=course).id==TCategory.objects.get(title=sel).parent_id:
        # if TCategory.objects.get(title=course).id==TCategory.objects.get(title=sel).parent_id:
            print(66666)
            art=TArticle.objects.create(title=article,content=details,publish_time=time)
            print(art)
            # return redirect("course:pythonBase")
            return HttpResponse('yes!'+level,{'username':username})
        else:
            return HttpResponse("no!")
    except:
        return HttpResponse("no")





#增加课程
def addCourse(request):
    id=request.GET.get('id')
    level=request.GET.get('level')
    username = request.session.get('username')
    cates = TCategory.objects.filter(level=1)
    sub_cates = TCategory.objects.filter(level=2)
    cate=TCategory.objects.filter(level=1)[0].title
    return render(request,'course/addCourse.html',{'cates':cates,'sub_cates':sub_cates,'level':level,'id':id,'username':username,'cate':cate})


#增加课程
def addCourse_logic(request):
    # id=request.GET.get("id")
    title=request.POST.get('title')
    print(title,111199999)
    level=request.POST.get('level')
    cate_sel = request.POST.get('cate_sel')
    print(cate_sel,8888)
    content=request.POST.get('content')
    username = request.session.get('username')
    print(11111,content)
    if title=='1':
        cate=TCategory.objects.create(title=content,level=1,parent_id=0)
        # id=cate.id
        if cate:
            return HttpResponse('yes!'+str(level),{'username':username})
            # return HttpResponse('yes',{'username':username,'level':level,'id':id})
        return HttpResponse('no')
    elif title=='2':
        id=TCategory.objects.get(title=cate_sel).id
        print(id,3333333333)
        cat=TCategory.objects.create(title=content,level=2,parent_id=id)
        if cat:
            return HttpResponse('yes!'+str(level),{'username':username})
            # return HttpResponse('yes',{'username':username,'level':level})
        return HttpResponse('no')



#删除
def delete_logic(request):
    title = request.GET.get('title')
    print(title)
    value = TArticle.objects.get(title=title)
    value.delete()
    return redirect('course:index')
    # id=request.GET.get('id')
    # level=request.GET.get('level')
    # print(level)
    # print(66666,id)
    # TArticle.objects.get(pk=id).delete()
    # article=TArticle.objects.all()
    # pagtor=Paginator(object_list=article,per_page=3)
    # pa=pagtor.page_range
    # number=int(request.session.get('number',1))
    # if number not in pa:
    #     request.session['number']=number-1
    # return redirect('course:pythonBase')




def update(request):
    try:
        level=request.GET.get('level')
        print('level',level)
        id = request.GET.get('id')
        username = request.session.get('username')
        article = TArticle.objects.get(id=id)  # 文章
        sub_cate = TCategory.objects.get(id=article.cate_id)
        parent_id = sub_cate.parent_id
        cate = TCategory.objects.filter(id=parent_id)
        print(cate[0].title)
        cates = TCategory.objects.filter(level=1)  # 一级分类
        sub_cates = TCategory.objects.filter(level=2)  # 二级分类
        return render(request,'course/update.html',{'article':article,
                                                    'cates':cates,
                                                    'cate':cate[0],
                                                    'sub_cates':sub_cates,
                                                    'sub_cat':sub_cate,
                                                    'level':level,'username':username
                                                    })
    except:
        traceback.print_exc()
        return HttpResponse('跳转出错')


def update_logic(request):
    try:
        id=request.GET.get('id')
        article_name=request.POST.get('title')
        check_course=request.POST.get('cate_sel')  # 一级分类名
        check_cate=request.POST.get('course_sel') # 二级分类名
        content=request.POST.get('content')
        print('id',id,'文章名',article_name,'课程id',check_course,'分类id',check_cate,'文章内容',content)
        with transaction.atomic():
            result=TArticle.objects.get(id=id)
            result.title=article_name
            result.course_id=check_cate
            result.content=content
            print(77777888888888)
            result.save()
            return HttpResponse("yes")
    except:
        traceback.print_exc()
        return HttpResponse("no")
        # return HttpResponse('修改失败')



def get_category(request):
    course_sel=request.GET.get("course_id")
    print(course_sel,99999999)
    # course_id = request.GET.get("course_id")
    cates = TCategory.objects.filter(parent_id=course_sel)
    def my_default(c):
        if isinstance(c, TCategory):
            return {"id": c.id, "title": c.title}
    return JsonResponse({"cates":list(cates)}, safe=False, json_dumps_params={"default": my_default})



def order(request):
    article=TArticle.objects.all()
    sort=request.GET.get('sort')
    if sort == '1':
        article = TArticle.objects.all().order_by('count')
        print(33333)
    elif sort == '2':
        article = TArticle.objects.all().order_by('publish_time')
        print(444444)
    cates = TCategory.objects.filter(level=1)
    sub_cates = TCategory.objects.filter(level=2)
    id = request.GET.get('id')
    print(id, 4444)
    number = request.GET.get('number', 1)
    level = request.GET.get('level')
    print(level)
    if level == '1':
        parent = TCategory.objects.filter(parent_id=id)
        name_title = TCategory.objects.filter(pk=id)[0].title
        print(name_title, 666666)
        list = []
        for i in parent:
            list.extend(TArticle.objects.filter(cate_id=i.id))
            print(list)
        pagtor = Paginator(object_list=list, per_page=4)
        page = pagtor.page(number)
        username = request.session.get('username')
        return render(request, 'course/pythonBase.html',
                      {'sub_cates': sub_cates, 'page': page, 'username': username,
                       'cates': cates, 'level': level, 'name_title': name_title, 'id': id})
    elif level == '2':
        title = TCategory.objects.get(pk=id)
        name_title = TCategory.objects.get(id=title.parent_id).title
        cat = TArticle.objects.filter(cate_id=id)
        sub_cates_name = TCategory.objects.get(pk=id).title
        pagtor = Paginator(object_list=cat, per_page=4)
        page = pagtor.page(number)
        print(page, 5555)
        username = request.session.get('username')
        return render(request, 'course/pythonBase.html',
                      {'name_title': name_title, 'sub_cates_name': sub_cates_name, 'username': username,
                       'cates': cates, 'page': page, 'sub_cates': sub_cates, 'level': level, 'id': id})