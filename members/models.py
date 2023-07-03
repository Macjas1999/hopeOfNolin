from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
from django.urls import reverse


#Image model

class Image(models.Model):
    description = models.TextField(null =  True, blank = True)
    altTxt = models.TextField(null = True, blank = True)

    squareImg = ResizedImageField(size = [1000, 1000], crop = ['middle', 'center'], default = 'defaultS.jpg', upload_to = 'square')
    horiImg = ResizedImageField(size = [1920, 1080], crop = ['middle', 'center'], default = 'defaultH.jpg', upload_to = 'horizontal')
    vertiImg = ResizedImageField(size = [1080, 1920], crop = ['middle', 'center'], default = 'defaultV.jpg', upload_to = 'vertical')