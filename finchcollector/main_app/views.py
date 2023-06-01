from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch


finches = [
    {'name': 'American Goldfinch', 'home': 'North America & Mexico', 'description': 'tiny migratory bird', 'fact': 'one of the strictest vegetarian birds in the world'},
    {'name': 'Brambling or Mountain finch', 'home': 'Europe & Africa & Alaska', 'description': 'international migratory bird', 'fact': 'they fly in flocks, and millions gather for migration'},
    {'name': 'Evening Grosbeak', 'home': 'Southern California', 'description': 'north american bulky looking finch', 'fact': 'they have powerful beaks that can crush seeds that other birds can not'},
    {'name': 'Hawfinch', 'home': 'Europe & Asia', 'description': 'short stocky finch with large bills', 'fact': 'the only finch placed in the genus coccothraustes'},
    {'name': 'Pine Grosbeak', 'home': 'Alaska', 'description': 'adorable qual looking finch', 'fact': 'their song depends on their geographical range'},
    {'name': 'Eurasian Bullfinch', 'home': 'Europe & Asia', 'description': 'worm-eating bird', 'fact': 'capable of learning specific melodies'},
    {'name': 'Purple Finch', 'home': 'North America', 'description': 'sparrow dipped in rasberry juice', 'fact': 'they are masters at breaking seeds with their beaks', 'image':'../static/imgs/purplefinch.jpg'},
]
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
    return render(request, 'finches/detail.html', { 'finch': finch })

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