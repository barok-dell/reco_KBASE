from django.db import models
from django.contrib.auth.models import User
#Questions
class Question(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


#Answer model
class Answers(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail
class Comments(models.Model):
    answer=models.ForeignKey(Answers,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE, related_name='comment_user')
    add_time = models.DateTimeField(auto_now_add=True)


class Vote_up(models.Model):
    answer=models.ForeignKey(Answers,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE, related_name='voteup_user')

class Vote_down(models.Model):
    answer=models.ForeignKey(Answers,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE, related_name='votedown_user')
