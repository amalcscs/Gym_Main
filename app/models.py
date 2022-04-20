from xmlrpc.client import boolean
from django.contrib.auth.models import User
from django.db import models


class designation(models.Model):
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.designation

class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='userregistrationdesignation', null=True, blank=True)
    fullname = models.CharField(max_length=240, null=True)
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    height = models.CharField(max_length=240, null=True)
    weight = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    joiningdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')
    Trainer_id = models.IntegerField(default='0', null=True, blank=True)

    def __str__(self):
        return self.fullname
