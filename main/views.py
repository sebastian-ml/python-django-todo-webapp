import datetime
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
        context["objects"] = self.model.objects.all().order_by('-pk')
        return context


class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"


def finish_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.finished = True
    task.when_finished_h = datetime.datetime.now()
    task.when_finished_date = datetime.date.today()
    task.save()

    return redirect('main-page')


def untick_finish(request, pk):
    task = Task.objects.get(pk=pk)
    task.finished = False
    task.when_finished_h = None
    task.when_finished_date = None
    task.save()

    return redirect('main-page')


def delete_all(request):
    Task.objects.all().delete()

    return redirect('main-page')


def delete_completed_tasks(request):
    Task.objects.filter(finished=True).delete()

    return redirect('main-page')


def untick_all(request):
    completed_tasks = Task.objects.filter(finished=True)
    for complete_task in completed_tasks:
        complete_task.finished = False
        complete_task.save()

    return redirect('main-page')

