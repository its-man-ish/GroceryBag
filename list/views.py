from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MyList
from .forms import AddItemForm
from django.urls import reverse, reverse_lazy
from .filters import DateFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils import timezone
from .helper import Render
class HomeView(LoginRequiredMixin,ListView):
    model = MyList
    context_object_name = 'items'
    login_url = 'login'
    template_name ='list/home.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DateFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SavedList(LoginRequiredMixin,ListView):
    model = MyList
    context_object_name = 'items'
    login_url = 'login'
    template_name ='list/saved_list.html'


class AddItemView(LoginRequiredMixin,CreateView):
    form_class = AddItemForm
    template_name = 'list/add_item.html'
    login_url = 'login'
    def get_absolute_url(self):
        return reverse('home')


class UpdateItem(UpdateView):
    model = MyList
    fields = ('item_name','item_quantity','item_status',)
    template_name ='list/update_item.html'

    def get_absolute_url(self):
        return reverse('home')


class DeleteItem(DeleteView):
    model = MyList
    fields = '__all__'
    context_object_name = 'items'
    success_url = reverse_lazy('home')
    template_name = 'list/delete_item.html'
    


def index(request):
    return render(request, 'list/index.html')

def MyBag(request):
    return render(request, 'list/mybag.html')


class ExportList(View):
    
    def get(self, request):
        items = MyList.objects.all()
        today = timezone.now()
        params = {
            'items': items,
            'today':today,
            'request':request,
        }

        return Render.render('list/export_list.html', params)
