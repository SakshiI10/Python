from django.db import models

# Create your models here: 
# Make model -> make migrations (No changes detected -> register your model in admin.py file -> register your app (copy app name from apps.py) in setting.py in string -> runserver again) -> make migrations again -> migrate (Table is created when you run migrate command)

# makemigration = create changes and store in a file
# migrate = apply the pending changes created by makemigrations

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name