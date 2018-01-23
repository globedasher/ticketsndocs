import os

from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Document

# Create your views here.

def index(request):
    context = {
            "documents": Document.objects.filter(uploaded_by__id=request.user.id),
            "turkey": "trotting",
            }
    return render(request, "docs/index.html", context)

def upload_center(request):
    return render(request, "docs/upload.html")

def upload(request):
    # Accept the upload submitted by the user.
    try:
        upload_file_handler(request.FILES['payload'], request.user.id)
    except:
        messages.error(request, "Upload failed")
        return redirect(reverse("docs:index"))

    path = "media/" + str(request.user.id) + "/" + str(request.FILES['payload'])
    user = User.objects.get(id=request.user.id)
    doc = Document.objects.create(uploaded_by=user, path=path)
    doc.save()
    return redirect(reverse("docs:index"))

def records(request):
    context = {"documents": Document.objects.all()}
    return render(request, "docs/records.html", context)

def upload_file_handler(f, user_id):
    path = "media/" + str(user_id) + "/"
    #print(os.path.join(path) + str(f))
    if os.path.exists(os.path.join(path + str(f))):
        print("File exists.")
        message.error(request, "That file already exists.")
        return render(reverse("docs:upload_center"))
    try:
        if not os.path.exists(os.path.join(path)):
            os.makedirs(os.path.join(path))
    except OSError:
        print("error")
        pass
    except:
        print("Failed to detect folder.")
    # Finally do the actual file creation and write.
    with open("media/" + str(user_id) + "/"+ str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            print("saved")
            return
