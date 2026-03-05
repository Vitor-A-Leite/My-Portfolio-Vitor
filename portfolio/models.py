from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    summary = models.TextField()
    email = models.EmailField()
    college_email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"Profile - {self.email}"

class Education(models.Model):
    DEGREES_CHOICES = [
        ("Bachelor's Degree", "Bachelor's Degree"),
        ("Professional Training", "Professional Training"),
        ("Online Courses", "Online Courses"),
    ]
    STATUS_CHOISES = [
        ('InProgress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=50,choices=DEGREES_CHOICES)
    field = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOISES, default='InProgress')
    start_year = models.DateField(blank=True)
    end_year = models.DateField(blank=True, default=timezone.now)

    def __str__(self):
        return f"{self.institution} - {self.degree}"

class Experience(models.Model):
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    responsibilities = models.TextField()
    tags = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.company} - {self.role}"

class Skills(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SoftSkills(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Languages(models.Model):
    PROFICIENCY_CHOICES = [
        ('Basic', 'Basic'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Native', 'Native'),
    ]
    name = models.CharField(max_length=255)
    proficiency = models.CharField(max_length=50, choices=PROFICIENCY_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.proficiency}"

class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.CharField(max_length=255)
    link = models.URLField()
    project_image = models.ImageField(upload_to='project_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name
