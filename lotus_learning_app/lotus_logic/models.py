from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    path = models.CharField(max_length=60)
    datetime = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=100)
    datetime = models.DateTimeField(blank=False, null=False)
    video = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='videos')
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='users')


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Library(models.Model):
    video = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='library_videos')
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='library_users')
