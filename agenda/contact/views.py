from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages
import time

def index(request, letter = any):
    if request.method == 'GET':
        if letter != any:
            contacts = Contact.objects.filter(name__istartswith= letter)
        else:
            contacts = Contact.objects.filter(name__contains= request.GET.get('search', ''))
    context = {'contacts': contacts}
    return render(request, 'contact/index.html', context)

def view(request, id):
    contact = Contact.objects.get(id=id)
    context= {
        'contact': contact
    }
    return render(request, 'contact/detail.html', context )

def edit(request, id):
    contact = Contact.objects.get(id=id)

    if (request.method == 'GET'):
        contact = Contact.objects.get(id=id)
        form = ContactForm(instance= contact)
        section = "Edit"
        context = {
            'section': section,
            'form': form,
            'id': id
        }
        return render(request, 'contact/edit.html', context)
    elif (request.method == "POST"):
        form = ContactForm(request.POST, instance= contact)
        if form.is_valid():
            form.save()
        
        context =  {
            'form': form,
            'id': id
        }
        messages.success(request, 'Contacto actualizado con exito!')
        return render(request, 'contact/edit.html', context)
    else:
        return HttpResponse("A ocurrido algun error, porfavor reintente luego")
    
def create(request):
    if (request.method == 'GET'):
        form = ContactForm()
        section = 'Create'
        context = {
            'form': form,
            'section': section
        }
        return render(request, 'contact/create.html', context)
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        # messages.success(request, 'Contacto creado con exito!')
        return redirect('contact')
    else:
        return HttpResponse("A ocurrido un Error")

def delete(request, id):
    contact = Contact.objects.get(id = id)
    contact.delete()
    return redirect('contact')