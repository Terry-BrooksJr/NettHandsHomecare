from django.shortcuts import render
from web.forms import ClientInterestForm
#SECTION - Page Rendering Views

def index(request):
    """Primary Render Function that Renders the Homepage template located in index.html.

    Args:
        request (HttpRequestObject): Request Object Passed at time of calling. 

    Returns:
        Renders Homepage
    """
    return render('index.html', {"title":"Home"})

def client_interest(request):
    """Secondary Render Function that Renders the sub-page for the client interest form  template located in 'client-interest.html' file.

    Args:
        request (HttpRequestObject): Request Object Passed at time of calling. 

    Returns:
        Renders sub-page Client Interest Form 
    """
    return render('client-interest.html', {"title":"Client Interest Form"})

def employee_interest(request):
    """Secondary Render Function that Renders the sub-page for the employee interest form  template located in 'employee-interest.html' file .

    Args:
        request (HttpRequestObject): Request Object Passed at time of calling. 

    Returns:
        Renders sub-page Employee Application Form 
    """
    return render('employee-interest.html', {"title":"Caregiver Employment Application"})
#!SECTION

#SECTION - Form Processing Views
def submit_client_intrest(request):
    """Instatiates the ClientInterestForm Class and checks the request.method. If Post - Processes Form Data. If GET - Renders Form

    Args:
        request (_type_): _description_
    """
        # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})
#!SECTION