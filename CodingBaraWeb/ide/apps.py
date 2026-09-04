from pathlib import Path
from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials, firestore

# Define a global placeholder variable that other modules can import
db = None

class IdeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ide'

    def ready(self):
        global db
        # Resolve path to serviceAccountKey.json at your Django project root
        base_dir = Path(__file__).resolve().parent.parent
        cred_path = base_dir / 'serviceAccountKey.json'
        
        if not firebase_admin._apps:
            if cred_path.exists():
                cred = credentials.Certificate(str(cred_path))
                firebase_admin.initialize_app(cred)
                # Assign the database reference directly upon initialization
                db = firestore.client()
            else:
                print(f"ERROR: Firebase key not found at {cred_path}")
        else:
            # Fallback if app is already initialized elsewhere
            db = firestore.client()