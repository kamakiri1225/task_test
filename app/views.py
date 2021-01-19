from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Choise


# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-pub_date')[:5]
    context = {
        'category_list':category_list,
    }
    return render(request, 'app/index.html', context)

def detail(request, question_id):
    print(Choise)
    question = get_object_or_404(Choise, pk=question_id)
    return render(request, 'app/detail.html', {'question': question})