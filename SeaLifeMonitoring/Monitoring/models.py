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
	
