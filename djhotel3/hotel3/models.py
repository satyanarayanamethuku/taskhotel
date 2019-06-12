from django.db import models

# Create your models here.
Room1=[
    ('101','101'),
    ('102','102'),
    ('103','103'),
    ('104','104'),
    ('105','105'),
]
CHOICES = [('Platinum', 'Platinum'),
   ('Suit', 'Suit'),]




class Register(models.Model):
    Customer_name = models.CharField(max_length=64)
    Username      = models.CharField(max_length=64)
    Password      = models.CharField(max_length=64)
    Membership_type=models.CharField(max_length=64)
    Booking1_id=models.IntegerField()

    def __str__(self):
        return str(self.Booking1_id)

class Platinum(models.Model):
   
    User = models.ForeignKey(Register, on_delete=models.CASCADE)
    Check_In = models.DateTimeField()
    Check_Out = models.DateTimeField()
    Room_number=models.CharField(max_length=64,choices=Room1,)
    Booking_id=models.IntegerField()
    Room_type=models.CharField(max_length=64, choices=CHOICES,)
    
   
    