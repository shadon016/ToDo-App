from django.db import models
from django.db import models
from django.contrib.auth.models import User

class AddTodo(models.Model):
    username=models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    task=models.CharField(max_length=255)
    description=models.TextField(max_length=500)
    isCompleted=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.task)
class Category(models.Model):
    category=models.ForeignKey(AddTodo,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.category)
