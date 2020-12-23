from django import forms
class StudentForm(forms.Form):
    sName = forms.CharField(max_length=20)
    sBranch = forms.CharField(max_length=3)
    sCourse = forms.CharField(max_length=10)
    sRollno = forms.CharField(max_length=10)
    sYear = forms.IntegerField()
    sAddress = forms.CharField(max_length=15)