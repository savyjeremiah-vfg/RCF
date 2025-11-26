from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db.models import Case, When, Value, BooleanField
from .models import Image, Testimony, Testimonys


def home(request):
    return render(request, "home.html")



def connectgroup(request):
    return render(request, "connectgroup.html")

def eventsingle(request):
    return render(request, "eventsingle.html")

def events(request):
    return render(request, "events.html")

def style(request):
    return render(request, "style.html")

def volunteer(request):
    return render(request, "volunteer.html")

def contact(request):
    return render(request, "contact.html")


def nav(request):
    return render(request, "nav.html")

def styles(request):
    return render(request, "styles.html")



def image(request):
    images = Image.objects.all()
    return render(request, "image.html", {"images": images})


def tem(request):
    testimonies = Testimony.objects.all()
    return render(request, "Tem.html", {"testimonies": testimonies})


def MEDIA(request):
    """
    Handles testimony submission with optional image upload.
    Displays the list of testimonies as well.
    """
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        image = request.FILES.get("image")  

        
        if not name or not message:
            messages.error(request, "Name and message are required.")
            return redirect("MEDIA")

        
        testimony = Testimonys.objects.create(
            name=name,
            message=message,
            image=image 
        )

        messages.success(request, "Your testimony has been submitted successfully!")
        return redirect("testimony_success")

    
    testimonies = Testimonys.objects.all().order_by("-created_at")
    return render(request, "MEDIA.html", {"testimonies": testimonies})



def testimony_success(request):
    """
    Shows a success message after submitting a testimony.
    """
    return render(request, "success_redirect.html")



def testimony_page(request):
    """
    Displays testimonies, prioritizing those older than 48 hours.
    """
    now = timezone.now()
    testimonies = Testimonys.objects.annotate(
        older_than_48=Case(
            When(created_at__lte=now - timezone.timedelta(hours=48), then=Value(True)),
            default=Value(False),
            output_field=BooleanField()
        )
    ).order_by('-older_than_48', '-created_at')

    return render(request, "Tem.html", {"testimonies": testimonies})




def delete_testimony(request, testimony_id):
    """
    Deletes a testimony with a given ID. Only accessible by logged-in users.
    """
    testimony = get_object_or_404(Testimonys, id=testimony_id)

    if request.method == "POST":
        testimony.delete()
        messages.success(request, "Testimony deleted successfully!")
        return redirect("testimony_page")

    return render(request, "confirm_delete.html", {"testimony": testimony})
