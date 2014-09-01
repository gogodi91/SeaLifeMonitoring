from django import forms
from monitoring.models import Area, Vessel, Cruise, Notes, Stations, TypeSpec, TAXA, ChemParam, Event, Chemistry, DataAB, SizeAgeFish, Age, Size
from monitoring.models import UserProfile
from django.contrib.auth.models import User


class AreaForm(forms.ModelForm):
	Start_Latitude_Degrees = forms.IntegerField(initial=0, help_text = "Please enter start latitude degrees")
	Start_Latitude_Minutes = forms.IntegerField(initial=0, help_text = "Please enter start latitude minutes")
	Start_Latitude_Seconds = forms.IntegerField(initial=0, help_text = "Please enter start latitude seconds")
	
	Start_Longitude_Degrees = forms.IntegerField(initial=0, help_text = "Please enter start longitude degrees")
	Start_Longitude_Minutes = forms.IntegerField(initial=0, help_text = "Please enter start longitude minutes")
	Start_Longitude_Seconds = forms.IntegerField(initial=0, help_text = "Please enter start longitude seconds")
	
	End_Latitude_Degrees = forms.IntegerField(initial=0, help_text = "Please enter end latitude degrees")
	End_Latitude_Minutes = forms.IntegerField(initial=0, help_text = "Please enter end latitude minutes")
	End_Latitude_Seconds = forms.IntegerField(initial=0, help_text = "Please enter end latitude seconds")
	
	End_Longitude_Degrees = forms.IntegerField(initial=0, help_text = "Please enter end longitude degrees")
	End_Longitude_Minutes = forms.IntegerField(initial=0, help_text = "Please enter end longitude minutes")
	End_Longitude_Seconds = forms.IntegerField(initial=0, help_text = "Please enter end longitude seconds")
	
	Start_Date_Time = forms.DateTimeField(help_text = "Please enter a starting date")
	End_Date_Time = forms.DateTimeField(help_text = "Please enter an end date")
	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Area
		# What fields do we want to include in our form?
		# This way we don't need every field in the model present.
		# Some fields may allow NULL values, so we may not want to include them...
		# Here, we are hiding the foreign key.
		fields = ('Start_Latitude_Degrees', 'Start_Latitude_Minutes', 'Start_Latitude_Seconds', 'Start_Longitude_Degrees', 'Start_Longitude_Minutes', 'Start_Longitude_Seconds', 'End_Latitude_Degrees', 'End_Latitude_Minutes', 'End_Latitude_Seconds', 'End_Longitude_Degrees', 'End_Longitude_Minutes', 'End_Longitude_Seconds', 'Start_Date_Time', 'End_Date_Time')
	
# good practice for URLs:
"""class PageForm(forms.ModelForm):

    ...

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data
"""

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
