from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .form import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class tasklistview(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 'Task'
class taskdetailview(DetailView):
    model=task
    template_name = 'details.html'
    context_object_name= 'tas'
class taskupdateview(UpdateView):
    model=task
    template_name = 'edit.html'
    context_object_name='tas'
    fields =('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbdetail',kwargs={'pk':self.object.id})
class taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbhome')

# Create your views here.
def home(request):
    Task = task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('Task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        TASK=task(name=name,priority=priority,date=date)
        TASK.save()


    return render(request,'home.html',{'Task':Task})
# def details(request):
#
#     return render(request,'details.html',,)
def delete(request,taskid):
    Task1=task.objects.get(id=taskid)
    if request.method == 'POST':
        Task1.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task2=task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task2)
    if f.is_valid():
        f.save()
        return redirect('/')

    return render(request,'update.html',{'f':f,'task2':task2})
