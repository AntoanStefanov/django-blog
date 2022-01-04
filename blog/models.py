from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# CLASS -> TABLE IN THE DATABASE


class Post(models.Model):
    # ATTRIBUTE -> FIELD IN DATABASE

    # CharField -> Character field, we can set some arguments that specify some restraints on the field
    title = models.CharField(max_length=100)

    # Now we have a title that will be a field of our post table in the database
    # And that title field will be a character field that has a restriction of a max length of a 100 characters

    content = models.TextField()

    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.DateField.auto_now_add
    # with that arg I could modify the creation date.
    date_posted = models.DateTimeField(default=timezone.now)

    # author is the user who created the post
    # user is a seperate table, so first we need to import the user model
    # The user model and post model will have a relationship,
    # since users are going to author(Post class)

    # One-to-many relationship,
    #   one user can have many posts
    #   but a post can have one author
    # For that, use foreign key, pass the related table as arg.

    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#foreignkey
    # If user created post and the user was deleted, what we will do with the post ?
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # CASCADE -> If a user is deleted, delete their posts as well
    # one-way street, if you delete a post it's not going to delete the user

    # Changes for the database were coded.
    # Now we need to make migrations, and update the database with these migrations - migrate.
