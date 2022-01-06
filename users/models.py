from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    # cascade -> if user is deleted, delete the profile too
    # but if we delete the profile, it won't delete the user
    # JUST ONE WAY thing
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # when I make a change in a model , also it will make a change in the DB 
    # to apply changes -> make migrations(prepare SQL code) -> migrate(update the DB)