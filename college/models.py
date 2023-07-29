from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse


class SubjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='completed')


class Subject(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('completed', 'Completed'),
    )
    FACULTY_CHOICES = (('bce', 'BCE'),
                       ('bct', 'BCT'), ('bel', 'BEL'), ('bie', 'BIE'), ('bme', 'BME'), ('arch', 'ARCH')
                       )

    YEAR_CHOICES = (('1', '1'),
                    ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')
                    )
    SEMESTER_CHOICES = (('1', '1'),
                        ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
                        ('10', '10')
                        )
    subject = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish', blank=True)

    faculty = models.CharField(max_length=5,
                               choices=FACULTY_CHOICES,
                               default='bct')
    year = models.CharField(max_length=5,
                            choices=YEAR_CHOICES,
                            default='1')
    semester = models.CharField(max_length=5,
                                choices=SEMESTER_CHOICES,
                                default='1')
    teacher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='subject_teacher')

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    published = SubjectManager()  # custom manager.

    class Meta:
        ordering = ('subject',)
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return f"{self.subject} {self.faculty} year-{self.year} semester-{self.semester}"

    def get_absolute_url(self):
        return reverse('assignment_list', args=[str(self.slug)])


class SubjectStudent(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_student")
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="student")

    def __str__(self):
        return f"{self.subject} {self.student}"
