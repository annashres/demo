import django_tables2 as tables
from django_tables2.utils import A
from .models import Departments, Professors, Courses, Students, Reviews

class DepartmentsTable(tables.Table):
    ID = tables.Column(visible=False)
    class Meta:
        model = Departments
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class ProfessorsTable(tables.Table):
    ID = tables.Column(visible=False)
    class Meta:
        model = Professors
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class CoursesTable(tables.Table):
    ID = tables.Column(visible=False)
    class Meta:
        model = Courses
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class StudentsTable(tables.Table):
    ID = tables.Column(visible=False)
    class Meta:
        model = Students
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class ReviewsTable(tables.Table):
    ID = tables.Column(visible=False)
    students = tables.Column(visible=False)
    class Meta:
        model = Reviews
        attrs = {'class': 'table table-bordered table-striped table-hover'}