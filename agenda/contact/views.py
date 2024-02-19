from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    if (request.method == 'GET'):
        contacts = Contact.objects.filter(name__contains= request.GET.get('search', ''))
    else:
        contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
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
        return render(request, 'contact/create.html', context)
    elif (request.method == "POST"):
        form = ContactForm(request.POST, instance= contact)
        if form.is_valid():
            form.save()
        
        context =  {
            'form': form,
            'id': id
        }
        messages.success(request, 'Contacto actualizado con exito!')
        return render(request, 'contact/create.html', context)
    else:
        return HttpResponse("A ocurrido algun error, porfavor reintente luego")