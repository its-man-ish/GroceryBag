from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Other'),
    )
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    country = models.CharField(max_length=200,blank=True)
    avatar = models.ImageField(upload_to='avatars/',blank=True)
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
       to_slug = str(self.user.username)
       self.slug = to_slug
       super().save(*args, **kwargs)

