from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20, null=True)
    user_sex = models.CharField(max_length=10, null=True)
    user_phone_first = models.CharField(max_length=20, null=True)
    user_phone_second = models.CharField(max_length=20, null=True)
    user_address = models.TextField(null=True)
    user_qq = models.CharField(max_length=20, null=True)
    user_id_card = models.CharField(max_length=20, null=True)
    user_fy_vip = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user_name

class Technician(models.Model):
    technician_name = models.CharField(max_length=20, null=True)
    technician_account = models.CharField(max_length=20, null=True)
    technician_password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.technician_name


class Computer(models.Model):
    computer_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    computer_technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True)
    computer_name = models.TextField(null=True)
    computer_condition = models.CharField(max_length=10, default='待修')
    computer_get_code = models.CharField(max_length=20, null=True)
    computer_password = models.CharField(max_length=20, null=True)
    computer_peripheral = models.TextField(null=True)
    computer_destroy = models.TextField(null=True)
    computer_backups_data = models.TextField(null=True)
    computer_server = models.TextField(null=True)
    computer_is_reset = models.BooleanField(default=False)
    computer_is_clear = models.BooleanField(default=False)
    computer_description = models.TextField(null=True)
    computer_repair_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.computer_name






