# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from monitoring.models import Area, Vessel, Cruise, Notes, Stations, TypeSpec, TAXA, ChemParam, Event, Chemistry, DataAB, SizeAgeFish, Age, Size
from monitoring.forms import AreaForm, VesselForm, CruiseForm, NotesForm, StationsForm, TypeSpecForm, TAXAForm, ChemParamForm, EventForm, ChemistryForm, DataABForm, SizeAgeFishForm, AgeForm, SizeForm
from monitoring.forms import UserForm, UserProfileForm



####################  INDEX  ####################

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
    
	#### CODE FOR VISITS COUNTER WITH COOKIES ####
    if request.session.get('last_visit'):
        # The session has a value for the last visit
        last_visit_time = request.session.get('last_visit')
        visits = request.session.get('visits', 0)

        if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
            request.session['visits'] = visits + 1
            request.session['last_visit'] = str(datetime.now())
    else:
        # The get returns None, and the session does not have a value for the last visit.
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = 1
    #### END  CODE ####
    
    return render_to_response('monitoring/index.html', context_dict, context)
    

####################  ABOUT  ####################

def about(request):
	context = RequestContext(request)
	
	
	# If the visits session varible exists, take it and use it.
    # If it doesn't, we haven't visited the site so set the count to zero.
	if request.session.get('visits'):
		count = request.session.get('visits')
		print '>>>> HITS COUNT {}'.format(count)
	else:
		count = 0
		print '>>>> HITS COUNT hihi {}'.format(count)
    # remember to include the visit data
	return render_to_response('monitoring/about.html', {'visits': count}, context)
	

####################  ADD_AREA  ####################

@login_required #requires user to be logged in to see this page
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
    return render_to_response('monitoring/records/add_area.html', {'form': form}, context)


####################  ADD_VESSEL  ####################

@login_required #requires user to be logged in to see this page
def add_vessel(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = VesselForm()
    return render_to_response('monitoring/records/add_vessel.html', {'form': form}, context)


####################  ADD_CRUISE  ####################

@login_required #requires user to be logged in to see this page
def add_cruise(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CruiseForm()
    return render_to_response('monitoring/records/add_cruise.html', {'form': form}, context)    


####################  ADD_NOTE  ####################

@login_required #requires user to be logged in to see this page
def add_note(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = NotesForm()
    return render_to_response('monitoring/records/add_note.html', {'form': form}, context)


####################  ADD_STATION  ####################

@login_required #requires user to be logged in to see this page
def add_station(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = StationsForm()
    return render_to_response('monitoring/records/add_station.html', {'form': form}, context)


####################  ADD_TYPESPEC  ####################

@login_required #requires user to be logged in to see this page
def add_typespec(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = TypeSpecForm()
    return render_to_response('monitoring/records/add_typespec.html', {'form': form}, context)


####################  ADD_TAXA  ####################

@login_required #requires user to be logged in to see this page
def add_taxa(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = TAXAForm()
    return render_to_response('monitoring/records/add_taxa.html', {'form': form}, context)


####################  ADD_CHEMPARAM  ####################

@login_required #requires user to be logged in to see this page
def add_chemparam(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = ChemParamForm()
    return render_to_response('monitoring/records/add_chemparam.html', {'form': form}, context)


####################  ADD_EVENT  ####################

@login_required #requires user to be logged in to see this page
def add_event(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = EventForm()
    return render_to_response('monitoring/records/add_event.html', {'form': form}, context)


####################  ADD_CHEMISTRY  ####################

@login_required #requires user to be logged in to see this page
def add_chemistry(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = ChemistryForm()
    return render_to_response('monitoring/records/add_chemistry.html', {'form': form}, context)


####################  ADD_DATAAB  ####################

@login_required #requires user to be logged in to see this page
def add_dataab(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = DataABForm()
    return render_to_response('monitoring/records/add_dataab.html', {'form': form}, context)


####################  ADD_SIZEAGEFISH  ####################

@login_required #requires user to be logged in to see this page
def add_sizeagefish(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = SizeAgeFishForm()
    return render_to_response('monitoring/records/add_sizeagefish.html', {'form': form}, context)


####################  ADD_AGE  ####################

@login_required #requires user to be logged in to see this page
def add_age(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = AgeForm()
    return render_to_response('monitoring/records/add_age.html', {'form': form}, context)


####################  ADD_SIZE  ####################

@login_required #requires user to be logged in to see this page
def add_size(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VesselForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = SizeForm()
    return render_to_response('monitoring/records/add_size.html', {'form': form}, context)
    

####################  REGISTER  ####################

def register(request):
	# Like before, get the request's context.
	context = RequestContext(request)
	
	#if request.session.test_cookie_worked():
	#	print ">>>> TEST COOKIE WORKED!"
	#	request.session.delete_test_cookie()
	
	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

			# Did the user provide a profile picture?
			# If so, we need to get it from the input form and put it in the UserProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			# Now we save the UserProfile model instance.
			profile.save()

			# Update our variable to tell the template registration was successful.
			registered = True

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print user_form.errors, profile_form.errors

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	# Render the template depending on the context.
	return render_to_response(
			'monitoring/register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
			context)

			
####################  LOGIN  ####################

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/monitoring/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your SeaLifeMonitoring account is disabled. Please contact your administrator for further help!")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('monitoring/login.html', {}, context)


####################  LOGOUT  ####################

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/monitoring/')


####################  ADD INFO  ####################

@login_required
def add_info(request):
	context = RequestContext(request)
	#<!-->needs to be reworked to use dinamic data (dictionary)</-->
	#table_dict = {'table_name': table_name}
	return render_to_response('monitoring/add_info.html', context)
	

####################  GET INFO  ####################

def get_info(request):
	context = RequestContext(request)
	#<!-->needs to be reworked to use dinamic data (dictionary)</-->
	#table_dict = {'table_name': table_name}
	return render_to_response('monitoring/get_info.html', context)

####################  ADD INFO RECORDS  ####################
