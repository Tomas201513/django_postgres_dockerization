from django.db import models

# Create your models here.
class Grandparent(models.Model):
    g1=models.CharField(max_length=255)
    g2=models.IntegerField()
    g3=models.TextField(null=True)
    def __str__(self):
        return self.g1

class Parent(models.Model):
    p1=models.CharField(max_length=255)
    p2=models.IntegerField()
    p3=models.TextField(null=True)
    fgrandparent=models.ForeignKey(Grandparent,on_delete=models.PROTECT)
    def __str__(self):
        return self.p1

class Children(models.Model):
    c1=models.CharField(max_length=255)
    c2=models.IntegerField()
    c3=models.TextField(null=True)
    fparentf=models.ForeignKey(Parent,on_delete=models.PROTECT)
    def __str__(self):
        return self.c1