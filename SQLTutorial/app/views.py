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
    table = CoursesTable(Courses.objects.all().prefetch_related('Professors'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Courses'
    })

# def courses_detail(request, pk):
#     #course = Course.objects.get(pk=pk)
#     courseTable = CoursesTable(Courses.objects.filter(ID=pk))
#     studentsTable = StudentsTable(Students.objects.filter(course=pk))

#     return render(request, 'app/app_detail2.html', {
#         'courseTable': courseTable,
#         'studentsTable': studentsTable,
#     })

def students_list(request):
    table = StudentsTable(Students.objects.all().prefetch_related('Courses'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Students'
    })


def new_professor(request):
    if request.method == "POST":
        form = ProfessorsForm(request.POST)
        if form.is_valid():
            feature = form.save()
            return redirect('professors_list')
    else:
        form = ProfessorsForm()
    return render(request, 'edit.html', {'form': form, 'title':' Add Professor'})

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