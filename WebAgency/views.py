from django.template import Context, Template, loader
from django.http import HttpResponse

dominio = "http://127.0.0.1:8000/"
rutas = {"home": dominio+"home", "nosotros": dominio+"nosotros", "contacto":dominio+"contacto", "tours":dominio+"tours"
         ,"traslados":dominio+"traslados","tours_personalisados":dominio+"tours_personalisados","menu":dominio+"menu",}

def home(response):
    doc = loader.get_template("home.html")
    salida = doc.render(rutas)
    return HttpResponse(salida)

def menu(response):
    doc = loader.get_template("menu.html")
    salida = doc.render(rutas)
    return HttpResponse(salida)

def nosotros(response):
    doc = loader.get_template("nosotros.html")
    return HttpResponse(doc.render(rutas))

def contacto(response):
    return HttpResponse(loader.get_template("contacto.html").render(rutas))

def tours(response):
    return HttpResponse(loader.get_template("tours.html").render(rutas))

def tours_personalisados(response):
    return HttpResponse(loader.get_template("tours_personalisados.html").render(rutas))

def traslados(response):
    return HttpResponse(loader.get_template("traslados.html").render(rutas))

