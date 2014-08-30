from django.db import models

# Create your models here.
"""/*------------------------
			Area
--------------------------*/"""
class Area(models.Model):
	Start_Latitude = models.IntegerField()
	Start_Longitude = models.IntegerField()
	End_Latitude = models.IntegerField()
	End_Longitude = models.IntegerField()
	Start_Date_Time = models.DateTimeField()
	End_Date_Time = models.DateTimeField()
	
	def __unicode__(self):
		return self.Start_Latitude

"""/*------------------------
			Vessel
--------------------------*/"""
class Vessel(models.Model):
	Name = models.CharField(max_length=64)
	Captain = models.CharField(max_length=64)
	CSR_Code = models.CharField(max_length=32)
	
	def __unicode__(self):
		return self.Name
	def __unicode__(self):
		return self.Captain
	def __unicode__(self):
		return self.CSR_Code

"""------------------------
			Cruise
--------------------------"""
class Cruise(models.Model):
	Vessel_ID = models.ForeignKey(Vessel, on_delete=models.CASCADE)
	Start_Date = models.DateField()
	End_Date = models.DateField()
	Objectives = models.CharField(max_length=64)
	
	def __unicode__(self):
		return self.Objectives

"""/*------------------------
			Notes
--------------------------*/"""
class Notes(models.Model):
	Value = models.TextField()
	
"""/*------------------------
	Stations
--------------------------*/"""
class Stations(models.Model):
	Notes_ID = models.ForeignKey(Cruise, on_delete = models.CASCADE)
	Station_Type = models.CharField(max_length=10)
	Station_Code = models.CharField(max_length=20)
	Station_Name_BG = models.CharField(max_length=32)
	Station_Name_LAT = models.CharField(max_length=32)
	Station_Depth = models.FloatField()
	Latitude	= models.CharField(max_length=9)
	Longitude = models.CharField(max_length=9)
	Substrat	= models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.Station_Type
	def __unicode__(self):
		return self.Station_Code
	def __unicode__(self):
		return self.Station_Name_BG
	def __unicode__(self):
		return self.Station_Name_LAT
	def __unicode__(self):
		return self.Latitude
	def __unicode__(self):
		return self.Longitude
	def __unicode__(self):
		return self.Substrat

"""/*------------------------
	TypeSpec
--------------------------*/"""
class TypeSpec(models.Model):
	Type = models.CharField(max_length=7)
	BSID = models.IntegerField()
	
	def __unicode__(self):
		return self.Type

"""/*------------------------
	TAXA
--------------------------*/"""
class TAXA(models.Model):
	Type_Spec_ID = models.ForeignKey(TypeSpec, on_delete = models.CASCADE)
	URL = models.URLField(max_length=128)
	Scientific_Name = models.CharField(max_length=64)
	Authority = models.CharField(max_length=64)
	Rank = models.CharField(max_length=64)
	Status = models.CharField(max_length=64)
	Unaccept_Reason = models.CharField(max_length=64)
	Valid_APHIA_ID = models.IntegerField(max_length=64)
	Valid_Name = models.CharField(max_length=64)
	Valid_Authority = models.CharField(max_length=64)
	Kingdom = models.CharField(max_length=64)
	Phylum = models.CharField(max_length=64)
	Class	 = models.CharField(max_length=64)
	Order = models.CharField(max_length=64)
	Family = models.CharField(max_length=64)
	Genus = models.CharField(max_length=64)
	Citation = models.CharField(max_length=512)
	LSID = models.CharField(max_length=128)
	Is_Marine = models.BooleanField()
	Is_Brackish = models.BooleanField()
	Is_Freshwater = models.BooleanField()
	Is_Terestrial = models.BooleanField()
	Is_Extinct = models.BooleanField()
	Match_Type = models.CharField(max_length=32)
	Modified = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.Scientific_Name
	def __unicode__(self):
		return self.Authority
	def __unicode__(self):
		return self.Rank
	def __unicode__(self):
		return self.Status
	def __unicode__(self):
		return self.Unaccept_rReason
	def __unicode__(self):
		return self.Valid_Name
	def __unicode__(self):
		return self.Valid_Authority
	def __unicode__(self):
		return self.Kingdom
	def __unicode__(self):
		return self.Phylum
	def __unicode__(self):
		return self.Class
	def __unicode__(self):
		return self.Order
	def __unicode__(self):
		return self.Family
	def __unicode__(self):
		return self.Genus
	def __unicode__(self):
		return self.Citation
	def __unicode__(self):
		return self.LSID
	def __unicode__(self):
		return self.Match_Type
	def __unicode__(self):
		return self.Modified

"""/*------------------------
	ChemParam
--------------------------*/"""
class ChemParam(models.Model):
	Parameter = models.CharField(max_length=10)
	Dimention = models.CharField(max_length=10)
	
	def __unicode__(self):
		return self.Parameter
	def __unicode__(self):
		return self.Dimention

"""/*------------------------
	Event
--------------------------*/"""
class Event(models.Model):
	Station_ID = models.ForeignKey(Stations, on_delete = models.CASCADE)
	Area_ID = models.ForeignKey(Area, on_delete = models.CASCADE)
	Cruise_ID = models.ForeignKey(Cruise, on_delete = models.CASCADE)
	Notes_ID	= models.ForeignKey(Notes, on_delete = models.CASCADE)
	Institute_Code = models.CharField(max_length=15)
	Collect_Code = models.CharField(max_length=32)
	Gear_Equipment = models.CharField(max_length=20)
	Sample_type = models.CharField(max_length=8)
	Date_Local_Time = models.DateField()
	Date_UTC = models.DateField()
	Start_Depth	= models.FloatField()
	End_Depth = models.FloatField()
	Operator	 = models.CharField(max_length=32)
	Post_Operator  = models.CharField(max_length=32)
	
	def __unicode__(self):
		return self.Institute_Code
	def __unicode__(self):
		return self.Collect_Code
	def __unicode__(self):
		return self.Gear_Equipment
	def __unicode__(self):
		return self.Sample_type
	def __unicode__(self):
		return self.Operator
	def __unicode__(self):
		return self.Post_Operator

"""/*------------------------
	Chemistry
--------------------------*/"""
class Chemistry(models.Model):
	Event_ID = models.ForeignKey(Event, on_delete = models.CASCADE)
	Param_ID = models.ForeignKey(ChemParam, on_delete = models.CASCADE)
	Notes_ID = models.ForeignKey(Notes, on_delete = models.CASCADE)
	Param_Value	= models.FloatField()
	Sample_Validated = models.BooleanField()
	Sample_Number = models.IntegerField()
	Protocol_Number = models.IntegerField()

"""/*------------------------
	DataAB
--------------------------*/"""
class DataAB(models.Model):
	Chem_ID = models.ForeignKey(Chemistry, on_delete = models.CASCADE)
	TAXA_ID = models.ForeignKey(TAXA, on_delete = models.CASCADE)
	Type_Spec_ID = models.ForeignKey(TypeSpec, on_delete = models.CASCADE)
	Notes_ID = models.ForeignKey(Notes, on_delete = models.CASCADE)
	Abundance = models.IntegerField()
	Abundance_Unit	= models.CharField(max_length=15)
	Biomass= models.FloatField()
	Biomass_Unit	= models.CharField(max_length=15)
	Replica_Unit = models.IntegerField()
	def __unicode__(self):
		return self.Abundance_Unit
	def __unicode__(self):
		return self.Biomass_Unit

"""/*------------------------
	SizeAgeFish
--------------------------*/"""
class SizeAgeFish(models.Model):
	AB_ID = models.ForeignKey(DataAB, on_delete = models.CASCADE)

"""/*------------------------
	Age
--------------------------*/"""
class Age(models.Model):
	Size_Age_ID = models.ForeignKey(SizeAgeFish, on_delete = models.CASCADE)
	Age_From = models.FloatField()
	Age_To = models.FloatField()
	Weight = models.FloatField()

"""/*------------------------
	Size
--------------------------*/"""
class Size(models.Model):
	Size_Age_ID = models.ForeignKey(SizeAgeFish, on_delete = models.CASCADE)
	Size_From = models.FloatField()
	Size_To = models.FloatField()
	Weight = models.FloatField()
	




