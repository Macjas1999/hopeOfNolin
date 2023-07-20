from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
from django.urls import reverse

DEFAULT_SQ = 'squareDefault.png'
DEFAULT_VT = 'defaultV.jpg'
DEFAULT_HR = 'defaultH.jpg'
#Image model

class Image(models.Model):
    #description = models.TextField(null =  True, blank = True)
    title = models.TextField(null =  True, blank = False)
    altTxt = models.TextField(null = True, blank = True)
    #display_index = models.IntegerField(null = True, blank = False, unique = True)

    squareImg = ResizedImageField(size = [1000, 1000], crop = ['middle', 'center'], default = DEFAULT_SQ, upload_to = 'square')
    #horiImg = ResizedImageField(size = [1920, 1080], crop = ['middle', 'center'], default = DEFAULT_HR, upload_to = 'horizontal')
    #vertiImg = ResizedImageField(size = [1080, 1920], crop = ['middle', 'center'], default = DEFAULT_VT, upload_to = 'vertical')

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.title, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.altTxt == "":
            self.altTxt = self.title        
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Image, self).save(*args, **kwargs)

#Puppies

class Puppies(models.Model):
    name = models.TextField(null =  True, blank = False)
    description = models.TextField(null =  True, blank = False)
    altTxt = models.TextField(null = True, blank = True)
    date_of_birth = models.DateField(null = True, blank = False)

    squareImg = ResizedImageField(size = [1000, 1000], crop = ['middle', 'center'], default = DEFAULT_SQ, upload_to = 'square')

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.name, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.altTxt == "":
            self.altTxt = self.name   
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.name, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Puppies, self).save(*args, **kwargs)

#Whippets

class Whippets(models.Model):
    name = models.TextField(null =  True, blank = False)
    description = models.TextField(null =  True, blank = False)
    altTxt = models.TextField(null = True, blank = True)
    date_of_birth = models.DateField(null = True, blank = False)

    squareImg = ResizedImageField(size = [1000, 1000], crop = ['middle', 'center'], default = DEFAULT_SQ, upload_to = 'square')

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.name, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.altTxt == "":
            self.altTxt = self.name   
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.name, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Whippets, self).save(*args, **kwargs)


#News contrent

class News(models.Model):
    title = models.TextField(null =  True, blank = False)
    contents = models.TextField(null =  True, blank = False)
    altTxt = models.TextField(null = True, blank = True)

    #squareImg = ResizedImageField(size = [1000, 1000], crop = ['middle', 'center'], default = DEFAULT_SQ, upload_to = 'square')
    horiImg = ResizedImageField(size = [1920, 1080], crop = ['middle', 'center'], default = DEFAULT_HR, upload_to = 'horizontal')
    #vertiImg = ResizedImageField(size = [1080, 1920], crop = ['middle', 'center'], default = DEFAULT_VT, upload_to = 'vertical')

    date_display = models.DateField(blank=False, null=True)

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    def __str__(self) -> str:
        return '{} {}'.format(self.title, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.altTxt == "":
            self.altTxt = self.title        
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(News, self).save(*args, **kwargs)

