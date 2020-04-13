import datetime
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView
from .models import Task


class TaskListAndCreateView(CreateView):
    """2 in 1 view. Create a task and display all tasks on the page."""
    model = Task
    template_name = 'main/home.html'
    fields = ['text']
    success_url = "/"

    def get_context_data(self, **kwargs):
        """
        Extend CreateView context data by a key which contains
        all tasks ordered from newest to the oldest.
        """
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all().order_by('-pk')
        return context


class TaskDeleteView(DeleteView):
    """Delete one, chosen task."""
    model = Task
    success_url = "/"


def finish_task(request, pk):
    """Mark the chosen task as finished."""
    task = Task.objects.get(pk=pk)
    task.finished = True
    task.when_finished_h = datetime.datetime.now()
    task.when_finished_date = datetime.date.today()
    task.save()

    return redirect('main-page')


def untick_finish(request, pk):
    """
    Mark the chosen, finished task as unfinished.
    Set finished date as None.
    """
    task = Task.objects.get(pk=pk)
    task.finished = False
    task.when_finished_h = None
    task.when_finished_date = None
    task.save()

    return redirect('main-page')


def delete_all(request):
    """Delete all user tasks."""
    Task.objects.all().delete()

    return redirect('main-page')


def delete_completed_tasks(request):
    """Delete only completed tasks."""
    Task.objects.filter(finished=True).delete()

    return redirect('main-page')


def untick_all(request):
    """Change the status of all finished tasks as unfinished."""
    completed_tasks = Task.objects.filter(finished=True)
    for complete_task in completed_tasks:
        complete_task.finished = False
        complete_task.when_finished_h = None
        complete_task.when_finished_date = None
        complete_task.save()

    return redirect('main-page')

