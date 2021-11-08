from django.shortcuts import render, redirect
from .models import Contacts
from .forms import ContactsForm
from django.views.generic import UpdateView, DetailView


def my_list(request):
    contacts = Contacts.objects.order_by('name')
    return render(request, 'main/list.html', {'contacts': contacts})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            error = 'Данные заполнены неверно'

    form = ContactsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


class ContactsDetailView(DetailView):
    model = Contacts
    template_name = 'main/details.html'
    context_object_name = 'contact'


class ContactsUpdateView(UpdateView):
    model = Contacts
    template_name = 'main/update.html'
    form_class = ContactsForm
