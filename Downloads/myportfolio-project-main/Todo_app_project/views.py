from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Todo, TodoCategory


# Create your views here.


@login_required
def todo_homepage(request):
    query = request.GET.get('query')
    todos = Todo.objects.filter(
        user=request.user
    ).order_by('-created_at')
    if query:
        todos = todos.filter(
            title__icontains=query
        )
    todos = todos.order_by('-created_at')
    context = {
        'todos': todos
    }
    return render(request, 'todo_app/todo_homepage.html', context)


@login_required
def create_todo(request):

    if request.method == 'POST':

        category_id = request.POST.get('category')

        category = None

        if category_id:
            category = TodoCategory.objects.get(
                id=category_id
            )

        Todo.objects.create(

            user=request.user,

            title=request.POST.get('title'),

            description=request.POST.get('description'),

            priority=request.POST.get('priority'),

            due_date=request.POST.get('due_date'),

            category=category

        )

        return redirect('todo_homepage')

    categories = TodoCategory.objects.all()

    print(categories)  # Debug

    return render(
        request,
        'todo_app/create_todo.html',
        {
            'categories': categories
        }
    )



    

@login_required
def complete_todo(request, id):

    todo = Todo.objects.get(
        id=id,
        user=request.user
    )

    todo.is_completed = True

    todo.save()

    return redirect(
        'todo_homepage'
    )


@login_required
def delete_todo(request, id):

    todo = Todo.objects.get(
        id=id,
        user=request.user
    )

    todo.delete()

    return redirect(
        'todo_homepage'
    )


@login_required
def update_todo(request, id):

    todo = Todo.objects.get(
        id=id,
        user=request.user
    )

    if request.method == 'POST':

        todo.title = request.POST.get(
            'title'
        )

        todo.description = request.POST.get(
            'description'
        )

        todo.priority = request.POST.get(
            'priority'
        )

        todo.due_date = request.POST.get(
            'due_date'
        )

        todo.save()

        return redirect(
            'todo_homepage'
        )

    return render(
        request,
        'todo_app/update_todo.html',
        {
            'todo': todo
        }
    )

@login_required
def todo_dashboard(request):

    todos = Todo.objects.filter(
        user=request.user
    )

    total_tasks = todos.count()

    completed_tasks = todos.filter(
        is_completed=True
    ).count()

    pending_tasks = todos.filter(
        is_completed=False
    ).count()

    high_priority = todos.filter(
        priority='High'
    ).count()

    progress = 0
    if total_tasks > 0:
        progress = (completed_tasks / total_tasks) * 100

    context = {

        'total_tasks': total_tasks,

        'completed_tasks': completed_tasks,

        'pending_tasks': pending_tasks,

        'high_priority': high_priority,
        'progress': progress

    }

    return render(
        request,
        'todo_app/todo_dashboard.html',
        context
    )