from django.shortcuts import render
from.models import ProductType

# Create your views here.
def index(request):
    return render(request,'techapp/index.html')

def techtype (request):
    type_list=ProductType.objects.all()
    return render (request, 'techapp/types.html', {'type_list': type_list})