from django.contrib.admin.models import LogEntry

def run():

    LogEntry.objects.all().delete()