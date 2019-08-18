from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=100)  # create title field that accepts chars until a max lenght of 100
    content = models.TextField()  # unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # We need to tell Django what to do if the user we created that post get's deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
