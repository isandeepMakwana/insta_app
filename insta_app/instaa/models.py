from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth_User', on_delete = models.CASCADE)
    image = models.ImageField(blank = True, null =True)
    caption = models.TextField()
    Created_date = models.DateTimeField(default = timeZone.now)
