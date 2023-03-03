from pipes import Template
from wsgiref.util import request_uri
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    data ={"header":"Hello Django","message": "Welcome to Python"}
    return TemplateResponse(request, "index.html", context=data)


def Hello(request):
    return HttpResponse("Hello METANIT.COM")

#def index(request):

#    host = request.META["HTTP_HOST"] # получаем адрес сервера
#    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
#    path = request.path     # получаем запрошенный путь
     
#    return HttpResponse(f"""
#        <p>Host: {host}</p>
#        <p>Path: {path}</p>
#        <p>User-agent: {user_agent}</p>
#    """
#        "Hello METANIT.COM", headers={"SecretCode": "21234567"})

def txt(request):
    return HttpResponse("<h1>Hello</h1>", content_type="text/plain", charset="utf-8")
    


 
def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
           
    """)
 
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def error(request):
    return HttpResponse("Произошла ошибка", status=400, reason="Incorrect data")


def user0(request):
    return HttpResponse("<h2>Главная</h2>")
  
def user(request, name="Undefined", age =0):
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


#####################
 
def index1(request):
    return HttpResponse("Главная страница")
 
def products(request, id):
    return HttpResponse(f"Товар {id}")
 
def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")
 
def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")

####################

def index3(request):
    return HttpResponse("<h2>Главная</h2>")
  
def user3(request):
    age = request.GET.get("age",0)
    name = request.GET.get("name", "Undefined")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

##############################

def index4(request):
    return HttpResponse("Index")
 
def about(request):
    return HttpResponse("About")
 
def contact(request):
    return HttpResponseRedirect("/about")
 
def details(request):
    return HttpResponsePermanentRedirect("/")

##################
#def index(request):
#    return JsonResponse({"name": "Tom", "age": 38})

#def index(request):
#    bob = Person("Bob", 41)
#    return JsonResponse(bob, safe=False, encoder=PersonEncoder)
 
class Person:
  
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age        # возраст человека
 
class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)


###############################################
# Передача данных в шаблон


def index20(request):
    header = "Данные пользователя"              # обычная переменная
    langs = ["Python", "Java", "C#"]            # список
    user ={"name" : "Tom", "age" : 23}          # словарь
    address = ("Абрикосовая", 23, 45)           # кортеж
  
    data = {"header": header, "langs": langs, "user": user, "address": address, "person": Person("Tomxx")}
    return render(request, "index.html", context=data)



class Person:
  
    def __init__(self, name):
        self.name = name    # имя человека

# Встроенные теги шаблонов

def index30(request):
    return render(request, "index.html", context = {"body": "<h1>Hello World!</h1>"})