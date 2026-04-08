from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML','MASALA'),
        ('GR','GREEN'),
        ('BL','BLACK'),
        ('HE','HERBAL'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='No description available.')
    def __str__(self):
        return self.name
#one to many 
class ChaiReveiw(models.Model):
    chai=models.ForeignKey(ChaiVariety,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
#many to many
class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    chai_varieties=models.ManyToManyField(ChaiVariety,related_name='stores')
    def __str__(self):
        return self.name
#0ne to one
class ChaiCertificate(models.Model):
    chai=models.OneToOneField(ChaiVariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    issue_date=models.DateTimeField(default=timezone.now)
    valid_untill=models.DateTimeField()
    def __str__(self):
        return f'Certificate for {self.chai.name}'
