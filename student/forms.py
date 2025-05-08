from django import forms
from student.models import Student


class StudentForm(forms.ModelForm):
    # extra_field=forms.CharField(max_length=5,required=true)
    class Meta:
        model=Student
        fields= "__all__"