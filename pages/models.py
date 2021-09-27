from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField

CATEGORY_CHOICES = (
    ('SW','SmartWatch'),
    ('P','Phone'),
    ('Pl','Planshet')
)
LABEL_CHOICES = (
    ('Y', 'primary'),
    ('D', 'danger'),
    ('S', 'secondry')
)
class Item(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    price = models.FloatField()
    condition = models.CharField(max_length=50)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    price = models.FloatField()
    condition = models.CharField(max_length=50)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

# class CommentModel(models.Model):
#     blog = models.ForeignKey('Postmodel', on_delete=models.CASCADE, related_name='comments')
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     comment = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return '%s - %s' % (self.blog.title,self.first_name)

#     # class Meta:
#     #     verbos_name = 'comment'
#     #     verbos_name_plural ='comments'