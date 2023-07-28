from django.contrib.auth.models import User

user = User.objects.filter(username='nickeisenberg').first()

user.profile.image.width

user.profile.image.height

user.profile.image.url

test_user = User.objects.filter(username='TestUser').first()

test_user.profile.image
