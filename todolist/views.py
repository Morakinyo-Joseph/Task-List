from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Examples
from .forms import CreateNewTask


def index(response, id):

    name = TodoList.objects.get(id=id)

    if response.method == 'POST':
        if response.POST.get('save'):
            for task in name.examples_set.all():
                if response.POST.get("C" + str(task.id)) == "clicked":
                    task.complete = True
                else:
                    task.complete = False

                task.save()

        elif response.POST.get('addTask'):
            written_text = response.POST.get('writeTask')

            if len(written_text) > 2:
                name.examples_set.create(task=written_text, complete=False)
            else:
                print('Invalid Inputs')

        # This part is to delete task which was made by me
        elif response.POST.get('delete'):
            for task in name.examples_set.all():
                if response.POST.get(str(task.id)) == 'delete':
                    task.delete()

    return render(response, 'todolist/task.html', {'name': name})


def home(response):
    return render(response, 'todolist/home.html', {})


def create(response):
    if response.method == 'POST':
        form= CreateNewTask(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            data_info = TodoList(name=n)
            data_info.save()

        return HttpResponseRedirect("/%i" % data_info.id)

    else:
        form = CreateNewTask()

    return render(response, 'todolist/create.html', {'form': form})


def view(response):
    name = TodoList.objects.all()
    if response.method == 'POST':
        if response.POST.get('delete'):
            for lists in name:
                if response.POST.get(str(lists.id)) == 'del_from_list':
                    lists.delete()

        # trying to make a search button
        # elif response.POST.get('searchButton'):
        #     searching = response.POST.get('search')
        #
        #     return HttpResponseRedirect("/%i" % name.id)
        # passing this for now

    return render(response, 'todolist/view.html', {'name': name})


def profile(response):
    return render(response, 'todolist/profile.html', {})


print(TodoList.objects.all())



