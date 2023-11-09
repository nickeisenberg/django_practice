# python manage.py shell
from django.contrib.auth.models import User

User.objects.all()


#get the host and username string of a room
from base.models import Room

Room.objects.get(id=1).host
Room.objects.get(id=1).host.username
