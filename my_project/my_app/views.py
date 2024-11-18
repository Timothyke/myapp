from django.shortcuts import render

# Create your views here.
from .models import Item
from django.http import HttpResponse

# List View
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

# Detail View
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})

# Create View
def create_item(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Item.objects.create(name=name, description=description, price=price)
        return redirect('item_list')
    return render(request, 'create_item.html')

# Update View
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.price = request.POST['price']
        item.save()
        return redirect('item_list')
    return render(request, 'update_item.html', {'item': item})

# Delete View
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('item_list')