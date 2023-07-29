from django.contrib.auth.models import AbstractUser
from django.db import models

I_AM = [('teacher', 'Teacher'),
        ('student', 'Student')]


class CustomUser(AbstractUser):
    i_am = models.CharField(choices=I_AM, default='student', max_length=7)
