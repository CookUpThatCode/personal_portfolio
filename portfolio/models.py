from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
        # blank, for any of these models, if set to true, means that this attribute is optional
        # for some of the individual model objects. In this case, some of our projects displayed
        # on the site won't have a clickable link.
    
    def __str__(self):
        return self.title
    
