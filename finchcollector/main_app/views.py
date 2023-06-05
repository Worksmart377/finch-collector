from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Finch, Toy
from django.shortcuts import render, redirect
from .models import Finch
from .forms import FeedingForm


# Create your views here.
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
    'finches': finches
})
    
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.toys.all().values_list('id') # [1, 3, 7]

    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)

    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', 
    { 
        'finch': finch,
        'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have
    })
def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)

    # validate the form
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        '''
        {
            meal: 'B',
            date: '2023-06-02',
            cat_id: 1
        }
        '''
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)
class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'home', 'description', 'fact']
    # success_url = '/finches/' # not the preferred way 
    
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['description', 'fact']
    
class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'
    
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'