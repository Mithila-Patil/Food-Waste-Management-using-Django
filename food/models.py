from django.db import models

class Donor(models.Model):
    user_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Receiver(models.Model):
    user_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class FoodDonor(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    food_info = models.TextField()
    quantity = models.IntegerField()
    pick_up_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.city}"
    
    class Meta:
        verbose_name="My Post"
        verbose_name_plural="Received Forms"
