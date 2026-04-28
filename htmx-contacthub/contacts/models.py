from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
        related_name= 'contacts' #related_name allows you to access a User's related Contact objects from the User instance itself.
    )
    
    class meta():
        unique_together = ('user', 'email')

    def __str__(self):
        return f" Name: {self.name} Email: {self.email}"