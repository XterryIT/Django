from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    description = models.TextField('Description')
    image = models.ImageField('Images',upload_to='static/main/img')

    # def __str__(self):
    #     return self.title 
