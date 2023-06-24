from django.shortcuts import render

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