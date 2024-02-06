from django.db import models

class SuzdalUser(models.Model):
    id          = models.AutoField(primary_key=True)
    email       = models.CharField(max_length=77, null=True)
    token       = models.CharField(max_length=77, null=True)
    uid         = models.CharField(max_length=77, null=True)
    first_login = models.CharField(max_length=22, null=True) # 2022-11-11 14:13:43
    last_login  = models.CharField(max_length=22, null=True)

    province    = models.CharField(max_length=3, null=True)
    category    = models.CharField(max_length=3, null=True)
    city        = models.CharField(max_length=22, null=True)
    zone        = models.CharField(max_length=22, null=True)

    name        = models.CharField(max_length=33, null=True)
    age         = models.CharField(max_length=3, null=True)
    phone       = models.CharField(max_length=22, null=True)

    page_title  = models.CharField(max_length=77, null=True)
    about_me    = models.TextField(null=True)

    cover_image = models.CharField(max_length=77, null=True)
    images      = models.TextField(null=True)
   
    complaints  = models.IntegerField(null=True) 
    state       = models.IntegerField(null=True)
    
    class Meta:
        db_table = 'suzdal_user'
        indexes  = [
            models.Index(fields=['id', 'email']),
        ]


class SuzdalImage(models.Model):
    id          = models.AutoField(primary_key=True)
    user_id     = models.IntegerField(null=True)
    image1      = models.TextField(null=True)
    image2      = models.TextField(null=True)
    image3      = models.TextField(null=True)
    image4      = models.TextField(null=True)

    class Meta:
        db_table = 'suzdal_image'
        indexes  = [
            models.Index(fields=['user_id']),
        ]