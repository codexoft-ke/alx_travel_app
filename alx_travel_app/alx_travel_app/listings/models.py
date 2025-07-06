from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Listing(models.Model):
    """
    Travel listing model - basic structure for future development
    """
    title = models.CharField(max_length=200, help_text="Title of the travel listing")
    description = models.TextField(help_text="Detailed description of the listing")
    location = models.CharField(max_length=100, help_text="Location of the travel destination")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per night")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Travel Listing"
        verbose_name_plural = "Travel Listings"

    def __str__(self):
        return f"{self.title} - {self.location}"
