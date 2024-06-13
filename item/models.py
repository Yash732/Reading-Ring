from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Creating a new database model

class Category(models.Model):
    name = models.CharField(max_length =255)

    class Meta:
        # alphateical ordering
        ordering = ('name',)

        #changes the default django categorys to categories
        verbose_name_plural = 'Categories'
    
    # returns the actual vallues of the objects in a Category and not like Category object (1)
    def __str__(self):
        return self.name

class Item(models.Model):
    #links the item to its category, if the category is deleted all items in the category also get deleted
    category = models.ForeignKey(Category, related_name ='items', on_delete =models.CASCADE)
    
    name = models.CharField(max_length =255)
    description = models.TextField(blank =True, null= True)
    price = models.FloatField()
    image = models.ImageField(upload_to ='item_images',blank =True, null =True)
    is_sold = models.BooleanField(default = False)
    created_by = models.ForeignKey(User, related_name ='items', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name
    

    
