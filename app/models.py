from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    pub_date = models.DateTimeField('add publish')

    def __str__(self):
        return self.category

class Choise(models.Model):
    question = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_num = models.IntegerField(default=0)
    choise_text1 = models.CharField(max_length=200,null=True)
    choise_text2 = models.CharField(max_length=200,null=True)
    choise_text3 = models.CharField(max_length=200,null=True)
    choise_text4 = models.CharField(max_length=200,null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'問題{str(self.question_num)}'
