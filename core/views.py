from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm
# Create your views here.

#Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text
def index(request):
    #only shows available items and 6 on page
    items = Item.objects.filter(is_sold = False)[0:6]

    #display all categories
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    }) 

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form,
    })