from django.db import models

class Device_Group(models.Model):
    device_count = models.DecimalField(decimal_places=5,max_digits=9)
    device_user = models.CharField(max_length=15)

    def __str__(self):
        return self.device_user

class Device(models.Model):
    device_name = models.CharField(max_length=15)
    gps_latitude = models.DecimalField(decimal_places=5,max_digits=9)
    gps_longtitude = models.DecimalField(decimal_places=5,max_digits=9)
    device_group = models.ForeignKey(Device_Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.device_name