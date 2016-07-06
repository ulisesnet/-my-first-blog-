from django.contrib.auth.models import User
User.objects.all()
me = User.objects.get(username='ulisesnet')
Post.objects.create(author=me, title='Sample title', text='Test')

