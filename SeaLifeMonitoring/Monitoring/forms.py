from django import forms
from Monitoring.models import Area, Vessel, Cruise, Notes, Stations, TypeSpec, TAXA, ChemParam, Event, Chemistry, DataAB, SizeAgeFish, Age, Size

class AreaForm(forms.ModelForm):
	Start_Latitude = forms.IntegerField(initial=0, help_text = "Please enter start latitude coordinates")
	Start_Longitude = forms.IntegerField(initial=0, help_text = "Please enter start longitude coordinates")
	End_Latitude = forms.IntegerField(initial=0, help_text = "Please enter end latitude coordinates")
	End_Longitude = forms.IntegerField(initial=0, help_text = "Please enter start longitude coordinates")
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
		fields = ('Start_Latitude', 'Start_Longitude', 'End_Latitude', 'End_Longitude', 'Start_Date_Time', 'End_Date_Time')
	
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
