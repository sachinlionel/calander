from django.shortcuts import reverse
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    invitees = models.ManyToManyField(User, related_name='invitees')

    def __str__(self):
        return "Event: {} \nby: {}\nInvitees:{}\n".format(self.title, self.owner, self.invitees.all())

    def get_absolute_url(self):
        # breakpoint()
        # for invitee in self.invitees.all():
        #     pass
        return reverse('event-detail', kwargs={'pk': int(self.pk)})
