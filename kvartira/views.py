from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy

from .forms import KvartiraForm
from .models import Kvartira
from django.views.generic import View
from django.db.models import Q



class Kvartira_list(View):
    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            kvartira = Kvartira.objects.filter(
                Q(title__icontains=query) | Q(price__icontains=query)
            )
        else:
            kvartira = Kvartira.objects.all().order_by('-id')
        return render(request,'kvarteralar.html',{'kvartira':kvartira})
    
class Kvartira_detal(View):
    def get(self, request, pk):
        kvartir = Kvartira.objects.get(id=pk)
        return render(request,'kvartera_detal.html',{'kvartir':kvartir})

class Kvartira_create(View):
    def get(self, request):
        form = KvartiraForm()
        return render(request, 'create_kvartera.html',{'form':form})

    def post(self, request):
        form = KvartiraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('kvartira')
        return render(request, 'create_kvartera.html',{'form':form})
    
class Kvartera_update(View):
    def get(self, request, pk):
        kvartera = get_object_or_404(Kvartira, id=pk)
        form = KvartiraForm(instance=kvartera)
        return render(request, 'kvartera_update.html',{'form':form})
    
    def post(self, request, pk):
        kvartera = get_object_or_404(Kvartira, id=pk)
        form = KvartiraForm(request.POST, request.FILES, instance=kvartera)
        if form.is_valid():
            form.save()
            return redirect('kvartera_detal', pk=kvartera.id)
        return render(request, 'kvartera_update.html', {'form': form})

class Kvartera_delete(View):
    def get(self, request, pk):
        kvartera = get_object_or_404(Kvartira, id=pk)
        return render(request, 'kvartera_delete.html', {'kvartera': kvartera})
    
    def post(self, request, pk):
        kvartera = get_object_or_404(Kvartira, id=pk)
        kvartera.delete()
        return redirect('kvartira')
# Create your views here.
