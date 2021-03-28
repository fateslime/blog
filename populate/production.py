from populate import base
from account.models import User

print('Creating admin account ... ', end='')
User.objects.create_superuser(username='admin', password='????????', email=None, fullName='管理者')
print('done')