from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Person, Branch
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm



class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


def load_cities(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'accountapp/branch_dropdown_list_options.html', {'branches': branches})

def logout(request):
    auth.logout(request)
    return redirect('/')

def contact_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        form.save();
        return render(request, "message with link.html",{'mess':'Form submitted successfully '})


