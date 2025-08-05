from django.shortcuts import render, get_object_or_404
from .models import Category, Store

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def store_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    stores = Store.objects.filter(category=category)
    return render(request, 'store_list.html', {'category': category, 'stores': stores})

def store_detail(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    menu_items = store.menuitem_set.all()
    return render(request, 'store_detail.html', {'store': store, 'menu_items': menu_items})
