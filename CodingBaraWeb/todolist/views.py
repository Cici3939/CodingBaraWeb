from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList
from .forms import ToDoListForm

def todolist(request):
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            todo_item = form.cleaned_data.get('item')
            
            # Saves the text directly into the 'body' field of your database model
            ToDoList.objects.create(body=todo_item)
            
            return redirect('todolist')  # Change this to match your actual URL name
    else:
        form = ToDoListForm()
        
    # Crucial fix: Name this variable 'todo' to match your {% for item in todo %} template loop
    todo = ToDoList.objects.all()
    
    return render(request, 'todo.html', {'form': form, 'todo': todo})

def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(ToDoList, id=item_id)
        item.delete()
    return redirect('todolist')