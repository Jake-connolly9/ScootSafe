from django.db import models


class Device(models.Model):
    device_name = models. CharField(max_length=15)
    gps_latitude = models.DecimalField
    gps_longtitude = models.DecimalField

class Device_Group(models.Model):
    device_count = models.DecimalField
