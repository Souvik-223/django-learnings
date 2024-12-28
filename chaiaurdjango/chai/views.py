from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.

def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais',chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(request, 'chai/chai_detail.html', {'chai':chai})
    return render(request, 'chai_detail')