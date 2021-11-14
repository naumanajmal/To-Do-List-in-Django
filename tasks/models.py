from django.db import models
from datetime import datetime

class Task(models.Model):
    FRESHMAN = 'FRESHMAN'
    SOPHOMORE = 'SOPHOMOR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'), )
    units = models.IntegerField(default=0)
    title = models.CharField(max_length = 200)
    vacine_name = models.CharField(max_length = 200, default='myname')
    type = models.CharField(max_length=8,choices=YEAR_IN_SCHOOL_CHOICES,default=FRESHMAN)
    expirydate = models.DateTimeField(auto_now_add=True)
	
    
	



# Create your models here.
