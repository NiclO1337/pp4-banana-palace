from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    """
    Store a single restaurants information
    """
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    avalible_tables = models.IntegerField()

    def __str__(self):
        return f'Restaurant name: *{self.name}*'






# Query the database


# print('\n'
#     f'{'Name:':<14}',
#     f'{'Email address:':<25}',
#     'Is superuser:',
#     sep=" | "
# )

# print(
#     '----------------------------------------------------------'
# )
# for user in User.objects.raw("SELECT * FROM auth_user"):
#     print(
#         f'{user.username:<14}',
#         f'{user.email:<25}',
#         user.is_superuser,
#         sep=" | "
#     )