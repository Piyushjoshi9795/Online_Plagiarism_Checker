from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid
from college.models import Subject
from django.core.validators import FileExtensionValidator


class GiveAssignment(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="subject_assignment")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()

    class Meta:
        ordering = ('-date',)

    # class Meta:
    #     permissions = [
    #         ('special_status', 'Can read all books'),
    #     ]
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('assignment_detail', args=[str(self.id)])


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'assignments/user_{0}/{1}'.format(instance.student.username, filename)


class UploadAssignment(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    assignment = models.ForeignKey(
        GiveAssignment, on_delete=models.CASCADE, related_name='upload_assignment')
    student = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='upload_by_student')
    upload_file = models.FileField(upload_to=user_directory_path, validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])
    uploaded_date = models.DateField(auto_now_add=True,)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='pending')

    class Meta:
        ordering = ('-uploaded_date',)

    # def __str__(self):
    #     return self.str('uploaded_file')

    def get_absolute_url(self):
        return reverse('uploaded_detail', args=[str(self.id)])
