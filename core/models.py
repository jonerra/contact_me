from django.db import models

TITLE_CHOICES = (
(0, ' '),
(1, 'Ms.'),
(2, 'Mrs.'),
(3, 'Mr.'),
(4, 'Dr.'),
)

# Create your models here.
class Message(models.Model):
    title = models.IntegerField(choices=TITLE_CHOICES, default=0)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title