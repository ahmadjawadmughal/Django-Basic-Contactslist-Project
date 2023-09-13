from django.db import models

# Create your models here.
class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    comment = models.TextField(max_length = 600)

    def to_string(self):
        return f"<strong>Name:</strong> {self.first_name} {self.last_name} <strong>Email:</strong>{self.email} <strong>Comment:</strong>{self.comment}"