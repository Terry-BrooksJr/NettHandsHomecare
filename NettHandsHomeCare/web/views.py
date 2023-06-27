from django.shortcuts import redirect
from django.shortcuts import render
from web.forms import ClientInterestForm
from web.forms import EmploymentApplicationForm

# SECTION - Page Rendering Views


def index(request):
    """Primary Render Function that Renders the Homepage template located in index.html.

    Args:
        request (HttpRequestObject): Request Object Passed at time of calling.

    Returns:
        Renders Homepage
    """
    return render(request, "index.html", {"title": "Home"})

 
def about(request):
    """Primary Render Function that Renders the about sub-page template located in contact.html.

    Args:
        request (HttpRequestObject): Request Object Passed at time of calling.

    Returns:
        Renders Contact Subpage
    """
    return render(request, "about.html", {"title": "About Nett Hands"})


#!SECTION


# SECTION - Form Processing Views
def client_interest(request):
    """Instatiates the ClientInterestForm Class and checks the request.method. If Post - Processes Form Data. If GET - Renders Form

    Args:
        request (_type_): Request Object Passed at time of calling.

    Returns:
        Renders or Processes ClientInterestForm
    """
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ClientInterestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect("submitted")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientInterestForm()

    return render(
        request,
        "client-interest.html",
        {"form": form, "title": "Client Interest Form"},
    )


def employee_interest(request):
    """Secondary Render Function that Renders the sub-page for the employee interest form template located in 'employee-interest.html' file.

    Args:
        request (HttpRequestObject): Request Object Passed at time of calling.

    Returns:
        Renders sub-page Employee Application Form
    """
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EmploymentApplicationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect("submitted")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmploymentApplicationForm()

    return render(
        request,
        "employee-interest.html",
        {"form": form, "title": "Employment Application"},
    )


def submitted(request):
    return render(request, "submission.html", {"title": "Form Submission Confirmation"})


#!SECTION
