from django.db import models

class Info(models.Model):
    id_num = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=20)
    age =  models.IntegerField()
    gender = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Contact(models.Model):
    id_num = models.ForeignKey(Info,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    address = models.TextField(max_length =100)

    def __str__(self):
        return str(self.id_num)

