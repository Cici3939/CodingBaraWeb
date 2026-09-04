from django import forms

class ToDoListForm(forms.Form):
    item = forms.CharField(
        widget=forms.Textarea(attrs={
            'id': 'list-item', 
            'rows': 1, 
            'style': 'width: 100%; font-size: 16px; padding: 10px; background-color: #ffd8b3; color: #A87958; border-radius: 5px; resize: none;',
            'placeholder': 'Enter new item...'
        })
    )