from django import forms

class CodeForm(forms.Form):
    code = forms.CharField(
        widget=forms.Textarea(attrs={
            'id': 'code-editor',
            'rows': 25,
            'style': 'display: block; width: 100%; min-height: 500px; font-family: monospace; font-size: 16px; padding: 15px; background-color: #1e1e1e; color: #ffffff; border: 2px solid #333; border-radius: 8px; resize: none; box-sizing: border-box;',
            'placeholder': 'Paste your code here...',
        })
    )
