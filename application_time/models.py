from django.db import models

# to sync the db because of some table missing
# manage.py migrate --run-syncdb

class ApplicationTimeStamp(models.Model):
    insert_time  = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # no instance in db
    class Meta:
        abstract = True