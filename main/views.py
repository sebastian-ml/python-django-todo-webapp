from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView
from .models import Task


class TaskListAndCreateView(CreateView):
    model = Task
    template_name = 'main/home.html'
    fields = ['text']
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context


class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"
    template_name = 'main/home.html'


def finish_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.finished = True
    task.save()

    return redirect('main-page')


def untick_finish(request, pk):
    task = Task.objects.get(pk=pk)
    task.finished = False
    task.save()

    return redirect('main-page')
