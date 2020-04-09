from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author =models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank = True, null = True)
    image = models.ImageField(upload_to='pics', blank=True,null=True)


    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_Date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text
