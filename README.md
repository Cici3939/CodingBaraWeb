# CodingBara Web Dashboard 🦫💻

> *The official web application for the CodingBara ecosystem. A capybara-themed productivity suite designed to keep coders focused, organized, and calm.*
> Link to CodingBara: https://github.com/Cici3939/CodingBara

> *Note: the Firebase integration is still a work in progress.*

---

## 📌 Overview

This repository (`codingbaraweb`) houses the web application component of the broader **CodingBara** project. While the physical Raspberry Pi companion handles emotional sensing (FER & SER) and AI debugging support, this web app serves as the developer's primary workspace dashboard.

### Core Features
* **Pomodoro Productivity Timer:** Custom study and work intervals specifically configured to prevent coder burnout and cognitive fatigue.
* **Cloud-Synced To-Do List:** An interactive task manager to organize debugging steps, linked directly to our Firebase backend (project: Calm Capy).
* **Chill UI/UX:** A warm, capybara-themed interface built to reduce stress during long programming sessions.

---

## 🛠 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Database & Cloud:** Firebase

<img width="1470" height="800" alt="Screenshot 2026-09-27 at 9 59 10 AM" src="https://github.com/user-attachments/assets/04764b29-0652-479c-a6c1-87280a559556" />

---

## 🚀 Quickstart & Local Setup

### 1. Prerequisites
* Python 3.9+
* `pip` package manager
* Firebase project credentials (for database syncing)

### 2. Installation

Clone the repository and set up your local environment:

```bash
git clone [https://github.com/Cici3939/codingbaraweb.git](https://github.com/Cici3939/codingbaraweb.git)
cd codingbaraweb

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install Django and dependencies
pip install django firebase-admin python-dotenv

```

*(Note: If you have a `requirements.txt` file, run `pip install -r requirements.txt` instead).*

### 3. Environment Variables

Create a `.env` file in the root directory to store your Django configuration and Firebase credentials:

```env
SECRET_KEY=your_django_secret_key_here
DEBUG=True
FIREBASE_CREDENTIALS=path/to/calm-capy-firebase-adminsdk.json

```

### 4. Database Migrations & Run

```bash
# Apply Django migrations
python manage.py migrate

# Start the local development server
python manage.py runserver

```

The web app will now be accessible at `http://127.0.0.1:8000/`.

---

## 🔗 System Integration

This web application is designed to operate alongside the **CodingBara Hardware Unit**.
For the machine learning (SER/FER) pipelines, camera/mic integration, and Raspberry Pi robotics code, please visit the main hardware repository: [CodingBara Core](https://github.com/Cici3939/CodingBara?utm_source=gemini).

---

## 📄 Authors

Developed by **Cici Xing** and **Sarah Xu**.

```
