from django.db import models

# Create your models here.
class PostDetails(models.Model): 
    city=models.CharField(max_length=30 , default="KANPUR")
    stat=(
        ('Verified' , 'Verified'),
        ('Non Verified' , 'Not Verified')
    )
    status=models.CharField(max_length=20 , choices=stat)
    contactperson=models.TextField()
    icu=models.BooleanField()
    phone=models.BigIntegerField(blank=True)
    mailid=models.EmailField(max_length=254 , blank=True)
    bed=models.BooleanField()
    oxygen=models.BooleanField()
    ventilator=models.BooleanField()
    tests=models.BooleanField()
    fabiflu=models.BooleanField()
    remdesivir=models.BooleanField()
    favipiravir=models.BooleanField()
    tocilizumab=models.BooleanField()
    plasma=models.BooleanField()
    food=models.BooleanField()
    price=models.IntegerField(blank=True,null=True,default=0)


    def __str__(self):
        return str(self.id)