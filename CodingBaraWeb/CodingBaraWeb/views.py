from django.shortcuts import render, redirect, get_object_or_404
from todolist.models import ToDoList 
from todolist.forms import ToDoListForm 

def homepage(request): 
    if request.method == 'POST': 
        form = ToDoListForm(request.POST) 
        if form.is_valid(): 
            todo_item = form.cleaned_data.get('item') 
            ToDoList.objects.create(body=todo_item) 
            return redirect('homepage') # Changed from '' to 'homepage'
    else: 
        form = ToDoListForm() 
        
    todo = ToDoList.objects.all().order_by('-date') 
    return render(request, 'home.html', { 
        'form': form, 
        'todo': todo, 
    }) 

def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(ToDoList, id=item_id)
        item.delete()
    return redirect('homepage') # Sends user right back to the homepage

def ide(request): 
    return render(request, 'ide.html')