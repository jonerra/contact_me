from django.db import models
from django.core.exceptions import ValidationError

TITLE_CHOICES = (
(0, ' '),
(1, 'Ms.'),
(2, 'Mrs.'),
(3, 'Mr.'),
(4, 'Dr.'),
)

# Create your models here.
class Message(models.Model):
    subject = models.CharField(max_length=300)
    title = models.IntegerField(choices=TITLE_CHOICES, default=0)
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, blank=False, unique=False)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.subject