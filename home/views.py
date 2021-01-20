from django.shortcuts import render , HttpResponse
from home.models import ArticleModel,Contact,ContactModel
from datetime import date
from django.views import View
# Create your views here.

def index(request):
    return render(request,'index.html')
#    return HttpResponse('this is my app')

    #context={
     #   'variable':'this is vaiable 19'
    #}
    #return render(request,'index.html',context)

    #return HttpResponse('This is home [page')

def about(request):
     return render(request,'about.html')
    #return HttpResponse('This is  about page')

def services(request):
     return render(request,'services.html')
    #return HttpResponse('This is services page')

class contact(View):
    def get(self,request):
        return render(request,'contact.html')
    def post(self,request):
        name=request.POST['name']
        email= request.POST['email']
        phone=  request.POST['phone']
        desc=  request.POST['desc']
        Contact.objects.create(name=name,email=email ,phone=phone,desc=desc)
        return render(request,'contact.html')

   # if request.method == 'GET':
    #    return render(request,'contact.html')
    #if request.method == 'POST':
     #   return render(request,'contact.html')
       # Contact.save(Name='Ghulam Qadir',email='ths',phone='this phone',desc='this descr')
      #  Name=request.POST.get('name')
       # email=request.POST.get('Email')
        #phone=request.POST.get('Phone')
        #desc=request.POST.get('Desc')
        #date=date.today()
        #contact=Contact.save(Name='name',email='Email',phone='Phone',desc='Desc')
             
#    return HttpResponse('This is contact page')

def services1(request):
     if request.method == 'GET':
         return HttpResponse('services html ')
     if request.method == 'POST':
         return HttpResponse('POST REQUEST Called')
     
    #return HttpResponse('This is services page')

class services2(View):
    def get(self,request):
        return HttpResponse('GET services2 html ')
    def post(self,request):
        return HttpResponse('POST services2 html ')

class Article(View):
    def get(self,request):
        data=[{'Name':'Ghulam Qadir', 'Age':'37 Years'}]
        return render(request,'articles.html',{'data':data})
   # def post(self,request):
    #    return HttpResponse('POST Article html ')