from django.shortcuts import render
from .models import DishCategory


# Create your views here.
def main_page(request):
    categories = DishCategory.objects.filter(is_visible=True)
    return render(request, 'main.html', context={'category': categories})