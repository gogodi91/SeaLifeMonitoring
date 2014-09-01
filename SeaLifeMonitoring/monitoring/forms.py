from django import forms
from monitoring.models import Area, Vessel, Cruise, Notes, Stations, TypeSpec, TAXA, ChemParam, Event, Chemistry, DataAB, SizeAgeFish, Age, Size
from monitoring.models import UserProfile
from django.contrib.auth.models import User

####################  AREA FORM  ####################

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

####################  VESSEL FORM  ####################

class VesselForm(forms.ModelForm):
	Name = forms.CharField(help_text="Enter the vessel`s Name")
	Captain = forms.CharField(help_text="Enter the vessel`s Captain")
	CSR_Code = forms.CharField(help_text="Enter the vessel`s CSR")
	class Meta:
		model = Vessel
		fields = ('Name', 'Captain', 'CSR_Code')
	

####################  CRUISE FORM  ####################

class CruiseForm(forms.ModelForm):
	Vessel_ID = forms.ModelChoiceField(queryset = Vessel.objects.all(), help_text = "Select a Vessel preforming the cruise")
	Start_Date = forms.DateField(help_text = "Enter cruise`s Starting Date")
	End_Date = forms.DateField(help_text = "Enter cruise`s End Date")
	Objectives = forms.CharField(help_text="Enter cruise`s Objectives")
	class Meta:
		model = Cruise
		fields = ('Vessel_ID', 'Start_Date', 'End_Date', 'Objectives')

####################  NOTES FORM  ####################

class NotesForm(forms.ModelForm):
	Value = forms.CharField(widget=forms.Textarea, help_text = "Enter a Note")
	class Meta:
		model = Notes
		#fields = ('Value')
	

####################  STATIONS FORM  ####################

class StationsForm(forms.ModelForm):
	Notes_ID = forms.ModelChoiceField(queryset = Notes.objects.all(), help_text = "Select a Note")
	Station_Type = forms.CharField(help_text = "Enter station Type")
	Station_Code = forms.CharField(help_text = "Enter station Code")
	"""Station_Name_BG = forms.CharField()"""
	Station_Name_LAT = forms.CharField(help_text = "Enter station Name in Latin")
	Station_Depth = forms.FloatField(initial=0, help_text = "Enter station Depth")
	Latitude_Degrees = forms.IntegerField(initial=0, help_text = "Enter station Degrees of Latitude")
	Latitude_Minutes = forms.IntegerField(initial=0, help_text = "Enter station Minutes of Latitude")
	Latitude_Seconds = forms.IntegerField(initial=0, help_text = "Enter station Seconds of Latitude")
	Longitude_Degrees = forms.IntegerField(initial=0, help_text = "Enter station Degrees of Longitude")
	Longitude_Minutes = forms.IntegerField(initial=0, help_text = "Enter station Minutes of Longitude")
	Longitude_Seconds = forms.IntegerField(initial=0, help_text = "Enter station Seconds of Longitude")
	Substrat	= forms.CharField(help_text = "Enter station Substrat")
	class Meta:
		model = Stations
		fields = ('Notes_ID', 'Station_Type', 'Station_Code', 'Station_Name_LAT', 'Station_Depth', 'Latitude_Degrees', 'Latitude_Minutes', 'Latitude_Seconds', 'Longitude_Degrees', 'Longitude_Minutes', 'Longitude_Seconds', 'Substrat')


####################  TYPE SPEC FORM  ####################

class TypeSpecForm(forms.ModelForm):
	Type = forms.CharField(help_text = "Enter Species Type")
	BSID = forms.IntegerField(help_text = "Enter BSID")
	class Meta:
		model = TypeSpec
		fields = ('Type', 'BSID')


####################  TAXA FORM  ####################

class TAXAForm(forms.ModelForm):
	Type_Spec_ID = forms.ModelChoiceField(queryset = TypeSpec.objects.all(), help_text = "Select a Type")
	URL = forms.URLField(help_text = "Enter TAXA URL")
	Scientific_Name = forms.CharField(help_text = "Enter Latin Name")
	Authority = forms.CharField(help_text = "Enter Authority")
	Rank = forms.CharField(help_text = "Enter Rank")
	Status = forms.CharField(help_text = "Enter Status")
	Unaccept_Reason = forms.CharField(help_text = "Enter Reason for not being accepted")
	Valid_APHIA_ID = forms.IntegerField(help_text = "Enter a valid APHIA ID")
	Valid_Name = forms.CharField(help_text = "Enter a valid Vame")
	Valid_Authority = forms.CharField(help_text = "Enter a valid Authority")
	Kingdom = forms.CharField(help_text = "Enter the animal`s Kingdom")
	Phylum = forms.CharField(help_text = "Enter the animal`s Phylum")
	Class	 = forms.CharField(help_text = "Enter the animal`s Class")
	Order = forms.CharField(help_text = "Enter the animal`s Order")
	Family = forms.CharField(help_text = "Enter the animal`s Family")
	Genus = forms.CharField(help_text = "Enter the animal`s Genus")
	Citation = forms.CharField(512, help_text = "Enter the animal`s Citation")
	LSID = forms.CharField(help_text = "Enter the animal`s LSID")
	Is_Marine = forms.BooleanField(help_text = "Is it Marine?")
	Is_Brackish = forms.BooleanField(help_text = "Is it Brackish?")
	Is_Freshwater = forms.BooleanField(help_text = "Is it Freshwater?")
	Is_Terestrial = forms.BooleanField(help_text = "Is it Terestrial?")
	Is_Extinct = forms.BooleanField(help_text = "Is it Extinct?")
	Match_Type = forms.CharField(help_text = "Enter Matching Type")
	Modified = forms.CharField(help_text = "Modified?")
	class Meta:
		model = TAXA
		fields = ('Type_Spec_ID', 'URL', 'Scientific_Name', 'Authority', 'Rank', 'Status', 'Unaccept_Reason', 'Valid_APHIA_ID', 'Valid_Name', 'Valid_Authority', 'Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Citation', 'LSID', 'Is_Marine', 'Is_Brackish', 'Is_Freshwater', 'Is_Terestrial', 'Is_Extinct', 'Match_Type', 'Modified')
	

####################  CHEM PARAM FORM  ####################

class ChemParamForm(forms.ModelForm):
	Parameter = forms.CharField(help_text = "Enter Chemistry Parameter")
	Dimention = forms.CharField(help_text = "Enter Chemical Dimention")
	class Meta:
		model = ChemParam
		fields = ('Parameter','Dimention')


####################  EVENT FORM  ####################

class EventForm(forms.ModelForm):
	Station_ID = forms.ModelChoiceField(queryset = Stations.objects.all(), help_text = "Select Station")
	Area_ID = forms.ModelChoiceField(queryset = Area.objects.all(), help_text = "Select Area")
	Cruise_ID = forms.ModelChoiceField(queryset = Cruise.objects.all(), help_text = "Select Cruise")
	Notes_ID	= forms.ModelChoiceField(queryset = Notes.objects.all(), help_text = "Select Note")
	Institute_Code = forms.CharField(help_text = "Enter Institute Code")
	Collect_Code = forms.CharField(help_text = "Enter Collection code")
	Gear_Equipment = forms.CharField(help_text = "Enter Gear used")
	Sample_type = forms.CharField(help_text = "Enter Type of Sample")
	Date_Local_Time = forms.DateField(help_text = "Enter Local Date")
	Date_UTC = forms.DateTimeField(help_text = "Enter UTC Date and Time")
	Start_Depth	= forms.FloatField(help_text = "Enter Start Depth")
	End_Depth = forms.FloatField(help_text = "Enter End Depth")
	Operator	 = forms.CharField(help_text = "Enter Operator Name")
	Post_Operator  = forms.CharField(help_text = "Enter Post Operator Name")
	class Meta:
		model = Event
		fields = ('Station_ID', 'Area_ID', 'Cruise_ID', 'Notes_ID', 'Institute_Code', 'Collect_Code', 'Gear_Equipment', 'Sample_type', 'Date_Local_Time', 'Date_UTC', 'Start_Depth', 'End_Depth', 'Operator', 'Post_Operator')


####################  CHEMISTRY FORM  ####################

class ChemistryForm(forms.ModelForm):
	Event_ID = forms.ModelChoiceField(queryset = Event.objects.all(), help_text = "Select an Event")
	Param_ID = forms.ModelChoiceField(queryset = ChemParam.objects.all(), help_text = "Select a Parameter")
	Notes_ID = forms.ModelChoiceField(queryset = Notes.objects.all(), help_text = "Select Note")
	Param_Value	= forms.FloatField(help_text = "Enter Parameter Value")
	Sample_Validated = forms.BooleanField(help_text = "Is the sample Validated?")
	Sample_Number = forms.IntegerField(help_text = "Enter Sample Number")
	Protocol_Number = forms.IntegerField(help_text = "Enter Protocol Number")
	class Meta:
		model = Cruise
		fields = ('Event_ID', 'Param_ID', 'Notes_ID', 'Param_Value', 'Sample_Validated', 'Sample_Number', 'Protocol_Number')


####################  DATAAB FORM  ####################

class DataABForm(forms.ModelForm):
	Chem_ID = forms.ModelChoiceField(queryset = Chemistry.objects.all(), help_text = "Select Chemistry ID")
	TAXA_ID = forms.ModelChoiceField(queryset = TAXA.objects.all(), help_text = "Select TAXA")
	Type_Spec_ID = forms.ModelChoiceField(queryset = TypeSpec.objects.all(), help_text = "Select a Type")
	Notes_ID = forms.ModelChoiceField(queryset = Notes.objects.all(), help_text = "Select a Note")
	Abundance = forms.IntegerField(help_text = "Enter Abundance Value")
	Abundance_Unit	= forms.CharField(help_text = "Enter Abundance measurement Units")
	Biomass= forms.FloatField(help_text = "Enter Biomass Value")
	Biomass_Unit	= forms.CharField(help_text = "Enter Biomass measurement Units")
	Replica_Unit = forms.IntegerField(help_text = "Enter Replica Unit")
	class Meta:
		model = DataAB
		fields = ('Chem_ID', 'TAXA_ID', 'Type_Spec_ID', 'Notes_ID', 'Abundance', 'Abundance_Unit', 'Biomass', 'Biomass_Unit', 'Replica_Unit')


####################  SIZE AGE FISH FORM  ####################

class SizeAgeFishForm(forms.ModelForm):
	AB_ID = forms.ModelChoiceField(queryset = DataAB.objects.all(), help_text = "Select Chemistry ID")
	class Meta:
		model = SizeAgeFish
		#fields = ('AB_ID')
		

####################  AGE FORM  ####################

class AgeForm(forms.ModelForm):
	Size_Age_ID = forms.ModelChoiceField(SizeAgeFish.objects.all(), help_text = "Select SizeAgeFish")
	Age_From = forms.FloatField(help_text = "Enter Fish lowest Age")
	Age_To = forms.FloatField(help_text = "Enter Fish highest Age")
	Weight = forms.FloatField(help_text = "Enter Fish Weight")
	class Meta:
		model = Age
		fields = ('Size_Age_ID', 'Age_From', 'Age_To', 'Weight')
		

####################  SIZE FORM  ####################

class SizeForm(forms.ModelForm):
	Size_Age_ID = forms.ModelChoiceField(SizeAgeFish.objects.all(), help_text = "Select SizeAgeFish")
	Size_From = forms.FloatField(help_text = "Enter Fish lowest Size")
	Size_To = forms.FloatField(help_text = "Enter Fish highest Size")
	Weight = forms.FloatField(help_text = "Enter Fish Weight")
	class Meta:
		model = Size
		fields = ('Size_Age_ID', 'Size_From', 'Size_To', 'Weight')
		

####################  USER FORM  ####################

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


####################  USER PROFILE FORM  ####################

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
