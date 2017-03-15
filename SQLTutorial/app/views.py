from django.shortcuts import render, redirect
from .models import Departments, Professors, Courses, Students, Reviews
from .tables import DepartmentsTable, ProfessorsTable, CoursesTable, StudentsTable, ReviewsTable
from .forms import ReviewsForm
def welcome(request):
    ##welcome page 

def departments_list(request):
    table = DepartmentsTable(Departments.objects.all())
    RequestConfig(request, paginate={'per_page': 9000}).configure(table) #all on one page
    return render(request, 'app/list.html', {
        'table': table,
        'title': 'Departments'
    })

def professors_list(request):
    table = ProfessorsTable(Professors.objects.all().prefetch_related('Departments'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'app/list.html', {
        'table': table,
        'title': 'Departments'
    })

def courses_list(request):
    table = CoursesTable(Courses.objects.all().prefetch_related('Departments', 'Professors'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'app/list.html', {
        'table': table,
        'title': 'Courses'
    })

def courses_detail(request, pk):
    #course = Course.objects.get(pk=pk)
    courseTable = CoursesTable(Courses.objects.filter(ID=pk))
    studentsTable = StudentsTable(Students.objects.filter(course=pk))
    reviewsTable = ReviewsTable(Reviews.objects.filter(courses=pk)


    return render(request, 'app/app_detail2.html', {
        'courseTable': courseTable,
        'studentsTable': studentsTable,
        'reviewsTable': reviewsTable
    })

def students_list(request):
    table = StudentsTable(Students.objects.all().prefetch_related('Courses'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'app/list.html', {
        'table': table,
        'title': 'Students'
    })


def reviews_list(request):
    table = ReviewsTable(Reviews.objects.all().prefetch_related('Courses'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'app/list.html', {
        'table': table,
        'title': 'Reviews'
    })
def new_review(request):
    if request.method == "POST":
        form = ReviewsForm(request.POST)
        if form.is_valid():
            feature = form.save()
            return redirect('done')
    else:
        form = ReviewsForm()
    return render(request, 'app/review.html', {'form': form})

def done(request):
    return render(request, 'app/done.html')