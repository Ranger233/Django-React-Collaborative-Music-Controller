from django.db import models

import random
import string

def generate_unique_code():
  length = 6

  while True:
    newCode = ''.join(random.choices(string.ascii_uppercase, k=length))

    # to make sure the newCode doesn't already exist
    if Room.objects.filter(code=newCode).count() == 0: 
      break
  
  return newCode


# Create your models here.
class Room(models.Model): # class Room inherit from models.Model
  code = models.CharField(max_length=8, default='', unique=True)
  host = models.CharField(max_length=50, unique=True)
  guest_can_pause = models.BooleanField(null=False, default=False)
  votes_to_skip = models.IntegerField(null=False, default=1)
  created_at = models.DateTimeField(auto_now_add=True)