from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):

    def __str__(self):
        return self.username
# Create your models here.
