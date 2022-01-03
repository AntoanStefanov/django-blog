from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# CLASS -> TABLE IN THE DATABASE

class Post(models.Model):
    # ATTRIBUTE -> FIELD IN DATABASE

    # CharField -> Character field, we can set some arguments that specify some restraints on the field
    title = models.CharField(max_length=100)

    #  Now we have a title that will be a field of our post table in the database
    # And that title field will be a character field that has a restriction of a max length of a 100 characters

    content = models.TextField()

    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.DateField.auto_now_add
    # with that arg I could modify the creation date.
    date_posted = models.DateTimeField(default=timezone.now)


    # author is the user who created the post
    # user is a seperate table, so first we need to import the user model
    # The user model and post model will have a relationship
    author = models.CharField(max_length=100)
