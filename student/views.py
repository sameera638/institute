from django.shortcuts import render
from student.models import Student
from django.http import HttpResponse
from django.shortcuts import render, redirect
from student.forms import StudentForm
# def home_view(request):
#     name="adiguru prodigy"
#     return render(request,"index.html",{"companyname":name,"age":2})


def create_student_view(request):
    if request.method=="POST":
        student_form=StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
    student_form=StudentForm()
    return render(request,"student/create_student.html",{"form" :student_form })

# def update_student_view(request,id):
#     st=Student.objects.get(pk=id)
#     if request.method=="POST":
#         nm=request.POST.get("st_name")
#         roll=request.POST.get("st_roll_no")
#         st.name=nm
#         st.roll_no=roll 
#         st.save()
#     return render(request,"student/update_student.html",{'student':st})

# def student_list_view(request):
#     student_list=Student.objects.all()
#     return render(request,"student/student_list.html", {'student':student_list})

# def student_delete_view(request, id):
#     student = Student.objects.get(pk=id)
#     student.delete()
#     return redirect("/student/student_list/")


# def student_detail_view(request,id):
#      student = Student.objects.get(pk=id)
#      print(student)
#      return render(request,"student/student_detail.html",{"student":student})









# Create your views here.
