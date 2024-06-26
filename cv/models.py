from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Certificate(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    link = models.URLField(null=False, blank=False)
    gratudated_date = models.DateField(null=False, blank=False)
    
    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    link = models.URLField(null=False, blank=False)
    completion_date = models.DateField(null=False, blank=False)

    
    class Meta:
        ordering = ('-completion_date',)
        
    def __str__(self) -> str:
        return self.title
    

class Info(models.Model):
    image = models.ImageField(upload_to = 'info/')
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    about_text = models.TextField(max_length=400, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = PhoneNumberField(null=False, blank=False)
    github_link = models.URLField(null=False, blank=False)
    linkedin_link = models.URLField(null=False, blank=False)
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    

class Education(models.Model):
    university = models.CharField(max_length=150, null=False, blank=False)
    major = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    graduation_date = models.DateField(null=False, blank=False)
    
    def __str__(self) -> str:
        return self.university + " " + self.degree + " " + self.major
    

class Language(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=254, null=False, blank=False) 
    
    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    description = models.CharField(max_length=254, null=False, blank=False) 
    
    def __str__(self) -> str:
        return self.description


class Tool(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.name