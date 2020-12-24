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
        form = StudentForm(request.POST)
        student=StudentModel()
        student.sName=form.data['sName']
        student.sRollno=form.data['sRollno']
        student.sYear=form.data['sYear']
        student.sCourse=form.data['sCourse']
        student.sBranch=form.data['sBranch']
        student.sAddress=form.data['sAddress']
        student.save()
    # return redirect('/student/view-student')
    display={'sName':form.data['sName'],'sRollno':form.data['sRollno']}
    student=StudentModel.objects.all()
    return render(request,'StudentApp/Display.html',{'student':student,'add':1,'display':display})

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
        form = StudentForm(request.POST)
        student=StudentModel()
        student.id=request.POST['id']
        student.sName=form.data['sName']
        student.sRollno=form.data['sRollno']
        student.sYear=form.data['sYear']
        student.sCourse=form.data['sCourse']
        student.sBranch=form.data['sBranch']
        student.sAddress=form.data['sAddress']
        student.save()
    # return redirect('/student/view-student/')
    display={'sName':form.data['sName'],'sRollno':form.data['sRollno']}
    student=StudentModel.objects.all()
    return render(request,'StudentApp/Display.html',{'student':student,'update':1,'display':display})

def deleteView(request):
    student = StudentModel.objects.all()
    return render(request,'StudentApp/deleteView.html',{'student':student})

def deleteStudent(request):
    student1=StudentModel.objects.get(id=request.POST['id'])
    display={'sName':student1.sName,'sRollno':student1.sRollno}
    student1.delete()
    # student = StudentModel.objects.all()
    # return render(request,'StudentApp/Display.html',{'toast':toast,'student':student,'update':1})
    student=StudentModel.objects.all()
    return render(request,'StudentApp/Display.html',{'student':student,'delete':1,'display':display})

def Search(request):
    student=StudentModel.objects.filter(sRollno=request.GET['sRollno'])
    return render(request,'StudentApp/Display.html',{'student':student})
