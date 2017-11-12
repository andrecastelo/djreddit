from django.contrib.auth.models import AbstractUser
from django.db import models
from .user import User


class Post(models.Model):
    POST_TYPES = (
        ('text', 'Text'),
        ('link', 'Link'),
    )

    title = models.CharField(max_length=140, blank=False)
    body = models.CharField(max_length=512, blank=True)
    post_type = models.CharField(
        choices=POST_TYPES,
        blank=False,
        max_length=4,
        default='link'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title