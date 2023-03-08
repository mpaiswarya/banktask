# from django.db import models
#
# # Create your models here.
# class District (models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
#
# class Branch(models.Model):
#     District = models.ForeignKey(District , on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
#
# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     DOB= models.DateField(null=True, blank=True)
#     Age=models.IntegerField
#     Contact=models.IntegerField
#     Email=models.EmailField(max_length=100)
#     Address=models.TextField(max_length=600)
#     District = models.ForeignKey(District , on_delete=models.SET_NULL, null=True)
#     Branch= models.ForeignKey( Branch, on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         return self.name
#
#
