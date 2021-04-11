from django.db import models

# Create your models here.
class AddBooks(models.Model):
    CATEGORY = (
        ('Enginnering' , 'Enginnering'),
        ('Deploma' , 'Deploma'),
        ('Masters','Masters'),
        ('Farmacy' , 'Farmacy')
    )

    book_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=150 ,null=True ,choices=CATEGORY)
    book_name = models.CharField(max_length=150)
    book_author = models.CharField(max_length=150)
    total_no_books = models.IntegerField()
    no_book_available = models.IntegerField()
    is_available = models.BooleanField(default=True)
    location = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.book_name
    

class RequestBook(models.Model):
    CATEGORY = (
        ('Enginnering' , 'Enginnering'),
        ('Deploma' , 'Deploma'),
        ('Masters','Masters'),
        ('Farmacy' , 'Farmacy')
    )
    category = models.CharField(max_length=150 ,null=True ,choices=CATEGORY)
    book_name = models.CharField(max_length=150)
    book_author = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.book_name