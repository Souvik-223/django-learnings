from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE=[     #similar to Enums in python
        ('ML', 'Masala Chai'),
        ('GC', 'Ginger Chai'),
        ('CC', 'Cardamom Chai'),
        ('KC', 'Kashmiri Chai'),
        ('IC', 'Irani Chai'),
        ('SC', 'Sulemani Chai'),
        ('DC', 'Dum Chai'),
        ('OC', 'Other Chai'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type=models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    image = models.ImageField(upload_to='chai/images')
    description = models.TextField()

    def __str__(self):
        return self.name


# one to many 

class chaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return f'{self.user.Username} review for {self.chai.name}'
    
    
# Many to Many 

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name="Stores") 
    
    def __str__(self):
        return self.name
    

# one to one
class Certificates(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name="Certificate")
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until= models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.name.chai}'