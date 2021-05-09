from django.db import models

class Category(models.Model):
    title = models.fields.CharField(max_length=55,primary_key=True)

    def __str__(self) -> str:
        return self.title

class Detail_Vote(models.Model):
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.fields.CharField(blank=False,max_length=59)
    date_create = models.fields.DateTimeField(auto_now_add=True)
    time = models.fields.IntegerField()
    start_qustion  = models.fields.IntegerField()
    end_qustion  = models.fields.IntegerField()
    type_answer =[
        (4,"4 chocies"),
        (5,"5 chocies"),
        (6,"6 chocies"),
        (7,"7 chocies"),
        (8,"8 chocies")
                ]
    type_choices = models.SmallIntegerField(choices=type_answer,default=4)

    def __str__(self) -> str:
        return f'{self.category.title} {self.title}'

class Answer(models.Model):

    vote = models.ForeignKey(Detail_Vote,on_delete=models.CASCADE)
    number = models.fields.CharField(max_length=4,primary_key=True)
    answer = models.fields.IntegerField(default=0)
    def __str__(self) -> str:
        return f'[{self.vote.title}] [ number  {self.number} : answer {self.answer} ]'

class Correct_Answer(models.Model):

    vote = models.ForeignKey(Detail_Vote,on_delete=models.CASCADE)
    number = models.fields.CharField(max_length=4,primary_key=True)
    answer = models.fields.IntegerField(default=0)
    def __str__(self) -> str:
        return f'[{self.vote.title}] [ number  {self.number} : answer {self.answer} ]'
