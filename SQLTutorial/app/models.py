from django.db import models

class Departments(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(
        max_length = 64,
        choices = (
        ('Math', 'Math'), ('English','English'), ('Science','Science'), ('History', 'History')), verbose_name='Name')
    def __str__(self):
        return self.name

class Professors(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    firstname = models.CharField(max_length=256, verbose_name='First Name')
    lastname = models.CharField(max_length=256, verbose_name='Last Name')
    email = models.EmailField(max_length=256, verbose_name='Email Address') 
    department = models.ForeignKey('Departments', verbose_name='Department')
    def __str__(self):
        return self.email

class Courses(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=256, verbose_name='Name')
    department = models.ForeignKey('Departments', verbose_name='Department')
    professor = models.ForeignKey('Professors', verbose_name='Professor')
    semester = models.CharField(
        max_length = 64,
        choices = (
        ('Fall', 'Fall'), ('Winter','Winter'), ('Spring','Spring'), ('Summer', 'Summer')), verbose_name='Semester')
    year = models.CharField(max_length=64)
    def __str__(self):
        return self.id 

class Students(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    email = models.EmailField(max_length=256, verbose_name='Email Address') 
    firstname = models.CharField(max_length=256, verbose_name='First Name')
    lastname = models.CharField(max_length=256, verbose_name='Last Name')
    graduation_year = models.CharField(
        max_length = 64,
        choices = (
        ('2017', '2017'), ('2018','2018'), ('2019','2019'), ('2020', '2020')), verbose_name='Grad Year')
    courses = models.ManyToManyField('Courses', blank=True, verbose_name='Courses')
    def __str__(self):
        return self.email

class Reviews(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    course = models.ForeignKey('Courses', verbose_name='Course')
    students = models.ForeignKey('Students', verbose_name='Email Address')
    workload = models.CharField(
        max_length = 64,
        choices = (
        ('1', '1'), ('2','2'), ('3','3'), ('4', '4'), ('5', '5')), verbose_name='Amount of Work')
    difficulty = models.CharField(
        max_length = 64,
        choices = (
        ('1', '1'), ('2','2'), ('3','3'), ('4', '4'), ('5', '5')), verbose_name='Level of Difficulty')
    interest = models.CharField(
        max_length = 64,
        choices = (
        ('1', '1'), ('2','2'), ('3','3'), ('4', '4'), ('5', '5')), verbose_name='Level of Interest')
    def __str__(self):
        return self.email

