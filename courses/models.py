from django.db import models as md


class category(md.Model):
    name = md.CharField(max_length=100)

    def __str__(self):
        return self.name
class course(md.Model):
    title = md.CharField(max_length=100)
    content = md.TextField()
    price = md.IntegerField(default=0)
    image = md.ImageField(upload_to='course' , default = 'course/default.jpg')
    cg = md.ManyToManyField(category)

    def __str__(self):
        return self.title
