from django.shortcuts import render, redirect
from .models import Professors, Courses, Students
from .tables import ProfessorsTable, CoursesTable, StudentsTable
from .forms import ProfessorsForm, CoursesForm, StudentsForm
from django_tables2 import RequestConfig

##professors
#show all professors in a list
def professors_list(request):
    #make table
    table = ProfessorsTable(Professors.objects.all())
    #specify number of rows per page in table
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Professors'
    })

#create a new professor
def new_professor(request):
    if request.method == "POST":
        form = ProfessorsForm(request.POST)
        if form.is_valid():
            professor = form.save()
            return redirect('professors_list')
    else:
        form = ProfessorsForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Professor'})

#edit existing professor
def edit_professor(request, pk):
    professor = Professors.objects.get(pk=pk)
    if request.method == "POST":
        #instance=professor auto fills the form with current professors info
        form = ProfessorsForm(request.POST, instance=professor)
        if form.is_valid():
            courprofessorse = form.save()
            return redirect('professors_list')
    else:
        form = ProfessorsForm(instance=professor)
    return render(request, 'edit.html', {'form': form, 'title': 'Edit Professor'})

##students
#show all students in a list
def students_list(request):
    #prefetch related returns a QuerySet that will automatically retrieve, in a single batch, related objects for each of the specified lookups.
    table = StudentsTable(Students.objects.all().prefetch_related('courses'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Students'
    })

#create a new student
def new_student(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_list')
    else:
        form = StudentsForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Student'})

##courses
#show all courses in a list
def courses_list(request):
    table = CoursesTable(Courses.objects.all().prefetch_related('professor'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Courses'
    })

#show course and its students on a page
def course_detail(request, pk):
    course = Courses.objects.get(pk=pk)
    courseTable = CoursesTable(Courses.objects.filter(id=pk))
    studentsTable = StudentsTable(Students.objects.filter(courses=pk))
    return render(request, 'detail.html', {
        'title': 'Course Information',
        'item': course,
        'courseTable': courseTable,
        'studentsTable': studentsTable,
    })

#create a new course
def new_course(request):
    if request.method == "POST":
        form = CoursesForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('courses_list')
    else:
        form = CoursesForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Course'})

#edit existing course
def edit_course(request, pk):
    course = Courses.objects.get(pk=pk)
    if request.method == "POST":
        form = CoursesForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CoursesForm(instance=course)
    return render(request, 'edit.html', {'form': form, 'title': 'Edit Course', 'item': course})

##delete course
def delete_course(request, pk):
    course = Courses.objects.get(pk=pk).delete()
    return redirect('courses_list')