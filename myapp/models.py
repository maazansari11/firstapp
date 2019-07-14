import uuid

from django.contrib.auth.models import User
from django.db import models


class Doctor (models.Model):
    f_name = models.CharField (max_length=100)
    l_name = models.CharField (max_length=100)
    email = models.EmailField (max_length=100)
    username = models.CharField (primary_key=True, max_length=50)
    password = models.CharField (max_length=20)
    confirm_password = models.CharField (max_length=20, default="")
    user = models.ForeignKey (User, null=True, blank=True, on_delete="cascade")

    def __str__(self):
        return self.username


class UploadToDirPatientApp:
    def __init__(self, name):
        self.name = name

    def __call__(self, instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        u_uuid = uuid.uuid4
        new_filename = '{}.{}'.format (u_uuid, filename.split ('.')[-1])

        return '{0}/{1}/{2}/{3}'.format ('pat_backend_app/pat_scan_img', instance._meta.db_table, self.name,
                                         new_filename)

    def deconstruct(self):
        return ('myapp.models.UploadToDirPatientApp', [self.name], {})


class Patient (models.Model):
    f_name = models.CharField (max_length=100)
    l_name = models.CharField (max_length=100)
    email = models.EmailField (max_length=100)
    address = models.CharField (max_length=500)
    age = models.PositiveIntegerField ()
    dob = models.DateField ()
    contact_no = models.PositiveIntegerField ()
    user = models.ForeignKey (Doctor, null=True, blank=True, on_delete="cascade")
    logo_image = models.ImageField (verbose_name='Logo Image',
                                    upload_to=UploadToDirPatientApp ('logo_image'),
                                    blank=True, null=True)

    def __str__(self):
        return self.f_name
