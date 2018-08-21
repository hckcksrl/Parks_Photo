from django.db import models
from parks .users import models as user_models

# Create your models here.

class TimeStamp(models.Model) : 

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta : 
        abstract = True

    
class Image(TimeStamp):

    file = models.ImageField()
    location = models.CharField(max_length=1000 , null = True)
    creator = models.ForeignKey(user_models.User,related_name = 'images' , on_delete = models.CASCADE, null =True)


    def __str__(self):

        return '{}'.format(self.location)