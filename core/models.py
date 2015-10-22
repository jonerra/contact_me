from django.db import models
from django.core.exceptions import ValidationError

TITLE_CHOICES = (
('0', 'Ms.'),
('1', 'Mrs.'),
('2', 'Mr.'),
('3', 'Dr.'),
)

# Create your models here.
class Message(models.Model):
    subject = models.CharField(max_length=300)
    title = models.CharField(max_length=4, choices=TITLE_CHOICES)
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, blank=False, unique=False)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.subject