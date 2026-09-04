from django.shortcuts import render
from firebase_admin import firestore
from .forms import CodeForm
from .firebase import get_firestore_client

def ide(request):
    db = get_firestore_client()
    
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            submitted_code = form.cleaned_data.get('code')
            user_identifier = request.user.username if request.user.is_authenticated else 'anonymous'
            
            db.collection('code_submissions').add({
                'code': submitted_code,
                'user': user_identifier,
                'created_at': firestore.SERVER_TIMESTAMP,
            })
            
            # SUCCESS: Pass a fresh, new instance named 'form'
            return render(request, 'ide.html', {
                'form': CodeForm(), 
                'success': True
            })
        else:
            # FAILURE: Pass the invalid form with errors back named 'form'
            return render(request, 'ide.html', {'form': form})
            
    # GET REQUEST: This creates the form instance for initial page loads
    # MUST match the key name 'form' used in your HTML template {{ form.code }}
    form = CodeForm()
    return render(request, 'ide.html', {'form': form})
