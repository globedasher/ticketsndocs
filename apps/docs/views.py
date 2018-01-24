import os

from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Document

# Create your views here.

@login_required
def index(request):
    """
    This view returns documents uploaded by the current user.
    """
    documents = Document.objects.filter(uploaded_by__id=request.user.id)
    context = {
            "documents": documents,
            }
    return render(request, "docs/index.html", context)

@login_required
def upload_center(request):
    """
    This view returns documents uploaded by the current user.
    """
    return render(request, "docs/upload.html")

@login_required
def records(request):
    """
    This view returns documents uploaded by the current user.
    """
    context = {"documents": Document.objects.order_by('updated_at')}
    return render(request, "docs/records.html", context)

@login_required
def details(request, item_id):
    """
    This view returns documents uploaded by the current user.
    """
    document = Document.objects.get(id=item_id)
    print(document.updated_at)
    print(type(document.updated_at))
    context = {"document": document}
    return render(request, "docs/details.html", context)


@login_required
def upload(request):
    """
    This view returns documents uploaded by the current user.
    """
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


@login_required
def upload_file_handler(f, user_id):
    """
    This handler is used to check if a storage loation is available and saves
    the file.  I suggest splitting this later.
    """
    path = "media/" + str(user_id) + "/"
    #print(os.pkth.join(path) + str(f))
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
