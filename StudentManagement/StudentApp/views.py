from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
# Create your views here.
from StudentApp.models import StudentModel,searchStudent
from StudentApp.form import StudentForm

def base(request):
    return render(request,'StudentApp/Base.html')

def addStudent(request):
    form = StudentForm()
    return render(request,'StudentApp/Add.html',{'form':form})

def add(request):
    if request.method == 'POST':
        sform = StudentForm(request.POST)
        student=StudentModel()
        student.sName=sform.data['sName']
        student.sRollno=sform.data['sRollno']
        student.sYear=sform.data['sYear']
        student.sCourse=sform.data['sCourse']
        student.sBranch=sform.data['sBranch']
        student.sAddress=sform.data['sAddress']
        student.save()
    return redirect('/student/view-student/')

def viewStudent(request):
    student = StudentModel.objects.all()
    return render(request,'StudentApp/Display.html',{'student':student})

def editView(request):
    student = StudentModel.objects.all()
    return render(request,'StudentApp/editView.html',{'student':student})
def editStudent(request):
    if request.method == 'POST':
        student=StudentModel.objects.get(id=request.POST['id'])
        return render(request,'StudentApp/editForm.html',{'student':student})
def edit(request):
    if request.method == 'POST':
        sform = StudentForm(request.POST)
        student=StudentModel()
        student.id=request.POST['id']
        student.sName=sform.data['sName']
        student.sRollno=sform.data['sRollno']
        student.sYear=sform.data['sYear']
        student.sCourse=sform.data['sCourse']
        student.sBranch=sform.data['sBranch']
        student.sAddress=sform.data['sAddress']
        student.save()
    return redirect('/student/view-student/')

def deleteView(request):
    student = StudentModel.objects.all()
    return render(request,'StudentApp/deleteView.html',{'student':student})

def deleteStudent(request):
    student1=StudentModel.objects.get(id=request.POST['id'])
    toast=student1.sName
    toast1=student1.sRollno
    student1.delete()
    student = StudentModel.objects.all()
    return render(request,'StudentApp/Display.html',{'toast':toast,'toast1':toast1,'student':student,'var':'delete.js'})

def Search(request):
    student=StudentModel.objects.filter(sRollno=request.GET['sRollno'])
    return render(request,'StudentApp/Display.html',{'student':student})
