from django.shortcuts import render, redirect
from .models import Departments, Professors, Courses, Students, Reviews
from .tables import DepartmentsTable, ProfessorsTable, CoursesTable, StudentsTable, ReviewsTable

def welcome(request):
    ##welcome page 

def departments_list(request):
    table = DepartmentsTable(Departments.objects.all())
    RequestConfig(request, paginate={'per_page': 9000}).configure(table) #all on one page
    return render(request, 'app/list.html', {
        'table': table,
        'title': 'Departments',
        'client_principal_name': __get_client_principal_name(request)
    })

def professors_list(request):
    table = ProfessorsTable(Professors.objects.all().prefetch_related('Departments'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'app/list.html', {
        'table': table,
        'title': 'Departments',
        'client_principal_name': __get_client_principal_name(request)
    })

def courses_list(request):
    table = CoursesTable(Courses.objects.all().prefetch_related('Departments', 'Professors'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'app/list.html', {
        'table': table,
        'title': 'Courses',
        'client_principal_name': __get_client_principal_name(request)
    })

def courses_detail(request, pk):
    #course = Course.objects.get(pk=pk)
    courseTable = CoursesTable(Courses.objects.filter(ID=pk))
    studentsTable = StudentsTable(Students.objects.filter(course=pk))
    reviewsTable = ReviewsTable(Reviews.objects.filter(courses=pk).order_by('-Date'))
    blockersTable =  BlockersTable(Blockers.objects.filter(Apps=app))
    contactsTable =  ContactsTable(Contacts.objects.filter(Apps=app))
    featuresTable =  FeaturesTable(Features.objects.filter(applications=app))
    ID = pk


    return render(request, 'app/app_detail2.html', {
        'ID': pk,
        'app': app,
        'appTable': appTable,
        'blockersTable': blockersTable,
        'featuresTable': featuresTable,
        'contactsTable': contactsTable,
        'notesTable': notesTable,
        'client_prinicpal_name': __get_client_principal_name(request)
    })

def students_list(request):
    table = StudentsTable(Students.objects.all().prefetch_related('Courses'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'app/list.html', {
        'table': table,
        'title': 'Students',
        'client_principal_name': __get_client_principal_name(request)
    })


def reviews_list(request):
    table = ReviewsTable(Reviews.objects.all().prefetch_related('Courses'))
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    return render(request, 'app/list.html', {
        'table': table,
        'title': 'Reviews',
        'client_principal_name': __get_client_principal_name(request)
    })
