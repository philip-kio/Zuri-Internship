from django.db import models

# Create your models here.
class bookStore(models.Model):
    book_title = models.CharField(max_length=50)
    book_author= models.CharField(max_length=50)
    year_published= models.CharField(max_length=50)
    
    
    class Meta:
        verbose_name = "Book Store"
        verbose_name_plural = 'Book Stores'