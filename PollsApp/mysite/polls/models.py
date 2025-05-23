from django.db import models

"""we'll create two models: Question and Choice. A Question has a question and a 
publication date. A Choice has two fields: the text of the choice and a vote tally.
 Each Choice is associated with a Question."""

class Question(models.Model): #	To make our class a Django model (database table)
    question_text = models.CharField(max_length=200)  #To define a string/text column in the database
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #cascade mean if question deleted then corresponding choices will be deleted
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
