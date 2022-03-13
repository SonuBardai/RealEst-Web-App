from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile-pics')

    def __str__(self):
        return f'Profile of {self.user.username}'

    def save(self):
        super().save()
        # Saving the new profile picture to the DB

        img = Image.open(self.image.path)
        if img.height > 200 or img.width > 200:
            size = (200, 200)
            img.thumbnail(size)
            img.save(self.image.path)
        # Grabbing the saved profile picture and compressing it

class Contact(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    desc = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Query by {self.author.username}'