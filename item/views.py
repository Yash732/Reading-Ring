from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .forms import NewItemForm
from .models import Item
# Create your views here.

def detail(request, pk):

    #if item not present in DB it return 404 error, pk is the primary key given in request
    #the loading html page is present in templates 
    item = get_object_or_404(Item, pk = pk)

    #to show the related items below the selected item description
    related_items = Item.objects.filter(category = item.category, is_sold = False).exclude(pk = pk)[0:3]

    return render(request, 'item/detail.html',{
        'item': item,
        'related_items': related_items,
    })

#if not logged in the user will be directed to the login page
@login_required
def new(request):
    form = NewItemForm()

    return render(request, 'item/form.html',{
        'form' : form,
        'title' : 'New item'
    })
