from django.shortcuts import render, redirect
from .models import Professors, Courses, Students
from .tables import ProfessorsTable, CoursesTable, StudentsTable
from .forms import ProfessorsForm, CoursesForm, StudentsForm
from django_tables2 import RequestConfig

def professors_list(request):
    table = ProfessorsTable(Professors.objects.all())
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Professors'
    })

def courses_list(request):
    table = CoursesTable(Courses.objects.all().prefetch_related('professor'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Courses'
    })

def course_detail(request, pk):
    #course = Course.objects.get(pk=pk)
    courseTable = CoursesTable(Courses.objects.filter(id=pk))
    studentsTable = StudentsTable(Students.objects.filter(courses=pk))

    return render(request, 'detail.html', {
        'title': 'Course Information',
        'courseTable': courseTable,
        'studentsTable': studentsTable,
    })

def students_list(request):
    table = StudentsTable(Students.objects.all().prefetch_related('courses'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Students'
    })


##new pages
def new_professor(request):
    if request.method == "POST":
        form = ProfessorsForm(request.POST)
        if form.is_valid():
            feature = form.save()
            return redirect('professors_list')
    else:
        form = ProfessorsForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Professor'})

def new_course(request):
    if request.method == "POST":
        form = CoursesForm(request.POST)
        if form.is_valid():
            feature = form.save()
            return redirect('courses_list')
    else:
        form = CoursesForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Course'})

def new_student(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            feature = form.save()
            return redirect('student_list')
    else:
        form = StudentsForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Student'})

##edit pages
# def edit_professor(request, pk):
#     professor = Professors.objects.get(pk=pk)
#     if request.method == "POST":
#         form = ProfessorsForm(request.POST)
#         if form.is_valid():
#             feature = form.save()
#             return redirect('done')
#     else:
#         form = ProfessorsForm()
#     return render(request, 'app/edit.html', {'form': form})