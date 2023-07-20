from django.db import models
from django.urls import reverse


class District(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class AccountType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=12)
    email_id = models.EmailField(max_length=254)
    address = models.CharField(max_length=300)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True)




    def __str__(self):
        return self.name