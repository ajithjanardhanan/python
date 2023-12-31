from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from .forms import taskforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class tasklistview(ListView):
    model=task
    template_name='home.html'
    context_object_name = 'task'
class detailview(DetailView):
    model =task
    template_name = 'detail.html'
    context_object_name = 'task'

class updateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})
class deleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def add(request):
    Task1 = task.objects.all()
    if request.method=='POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        Task = task(name=name,priority=priority,date=date)
        Task.save()
    return render(request,"home.html",{'task':Task1})

#def detail(request):

   # return render(request,'detail.html',)
def delete(request,taskid):
    Task = task.objects.get(id=taskid)
    if request.method =='POST':
        Task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    Task = task.objects.get(id=id)
    form = taskforms(request.POST or None,instance=Task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{"task":Task,"form":form})

