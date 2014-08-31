# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from Monitoring.models import Event
from Monitoring.forms import AreaForm

def index(request):
	# Request the context of the request.
	# The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
	 
	 # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    events_list = Event.objects.order_by('-id')[:5]
    context_dict = {'events': events_list}
        
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    """context_dict = {'boldmessage': "OF A HUGE FISH"}"""

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('Monitoring/index.html', context_dict, context)

def about(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "OF A HUGE FISH"}
	return render_to_response('Monitoring/about.html', context_dict, context)

def add_area(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = AreaForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = AreaForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('Monitoring/add_area.html', {'form': form}, context)

