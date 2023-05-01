from django.db import models

# Create your models here.

class Coal(models.Model):
    origin_choice=(
        ('USA', 'United States'),
        ('AUS', 'Australia'),
        ('CAN', 'Canada'),
        ('RUS', 'Russia'),
        ('CHN', 'China'),
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    origin = models.CharField(max_length=100, choices=origin_choice)
    availability = models.BooleanField(default=True)
    dt_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    