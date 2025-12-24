from django.db import models

# Create your models here.
class Education(models.Model):
    level = models.CharField(max_length=100, choices=(('Bachelor', 'BSc'), ('Master', 'MSc'), ('PhD', 'PhD')))
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)
    status = models.CharField(max_length=20, choices=(('Graduated', 'Graduated'), ('Current', 'Current')))
    graduation_year = models.CharField(max_length=4)

    class Meta:
        verbose_name = 'Degree'
        verbose_name_plural = 'Degrees'
        ordering = ['start_year']

    def __str__(self):
        return self.level + " " + self.degree + " " + self.institution


class Experience(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)
    description = models.TextField()

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ['start_year']

    def __str__(self):
        return self.company + " " + self.title


class Certification(models.Model):
    img = models.ImageField(upload_to='certifications')
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=(('Completed', 'Completed'), ('In Progress', 'In Progress')))
    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    img = models.ImageField(upload_to='projects')
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    