import django_tables2 as tables
from django_tables2.utils import A
from .models import Professors, Courses, Students

class ProfessorsTable(tables.Table):
    id = tables.Column(visible=False)
    class Meta:
        model = Professors
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class CoursesTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.LinkColumn('course_detail', args=[A('pk')])
    class Meta:
        model = Courses
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class StudentsTable(tables.Table):
    id = tables.Column(visible=False)
    class Meta:
        model = Students
        attrs = {'class': 'table table-bordered table-striped table-hover'}