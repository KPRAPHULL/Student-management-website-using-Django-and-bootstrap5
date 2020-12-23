from django.db import models

# Create your models here.
class StudentModel(models.Model):
    sName = models.CharField(max_length=20)
    sBranch = models.CharField(max_length=3)
    sCourse = models.CharField(max_length=10)
    sRollno = models.CharField(max_length=10)
    sYear = models.IntegerField(max_length=1)
    sAddress = models.CharField(max_length=15)
    def __str__(self):
        # return sName
        return ("%s %s" %(self.sName,self.sBranch))

class searchStudent(models.Model):
    sRollno= models.CharField(max_length=10)