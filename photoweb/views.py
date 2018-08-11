from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
import pyrebase
from django.contrib import auth

config = {
    "apiKey": "AIzaSyADbyDfFtvRm2quo0xkPmUvGlEUaYrgoeQ",
    "authDomain": "mangalak-acacc.firebaseapp.com",
    "databaseURL": "https://mangalak-acacc.firebaseio.com",
    "projectId": "mangalak-acacc",
    "storageBucket": "mangalak-acacc.appspot.com",
    "messagingSenderId": "751379753582"
}
firebase = pyrebase.initialize_app(config)
mAuth = firebase.auth()
# db = firebase.database().child("projects")
db = firebase.database().child("projects")


# Create your views here.
def index(request):
    return render(request, 'photoapp/index.html')


def send(request):
    name = request.POST.get('Name')
    uid = name
    data = {"name": "mangal", "email": "mangal@gmail.com"}
    db.child("123").set(data)
    return render(request, "photoapp/index.html")


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = mAuth.sign_in_with_email_and_password(email, password)
    except:
        message = 'invalid password or email'
        return render(request, "photoapp/index.html", {"msg": message})
    print(user)
    session_id = user['idToken']
    request.session['uid'] = str(session_id)

    return render(request, "photoapp/index.html", {"e": 'login sucsessful'})

def logout(request):
    auth.logout(request)
    return render(request,'photoapp/index.html')