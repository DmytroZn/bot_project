from mongoengine import *
from models import models
connect('web_shop_bot')




##############################################

# for i in range(5):
#     obj = models.Category(**{'title':f'root {i}',
#                         'description':f'descr {i}'}).save()

#     obj.add_subcategory(
#         models.Category(**{'title': f'sub {i}',
#                             'description': f'descr {i}'})
#     )
###########################################

# objects = models.Category.objects(parent__ne=None)

# for i in objects:
#     i.add_subcategory(
#         models.Category(**{'title': f'sub-sub {i}',
#                             'description': f'd {i}'})
#     )

###################################3

# prod1 = models.Product(**{'title': 'Meizu',
#                         'description': 'You can call',
#                         'price': 300,
#                         'category': '5dcaf2ac3db8e6530cc686ec'
#                        }).save()

# n = models.Category.objects(title='root 1').update(title='Phonies')
# n = models.Category.objects(title='sub 1').update(title='Apple')
n = models.Category.objects(title='Apple', description='d 1').update(title='Apple1')

