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
# n = models.Category.objects(title='Apple2').first().update(title='Apple3')
# n = models.Category.objects(title='Apple2').first().update(title='Apple4')
# n = models.Category.objects(title='Apple2').first().update(title='Apple5')
# n = models.Category.objects(title='Apple2').first().update(title='Apple6')
# n = models.Category.objects(title='Apple').first().update(title='Apple2')
# n = models.Category.objects(title='Apple').first().update(title='Apple3')
# n = models.Category.objects(title='Apple').first().update(title='Apple4')

# n = models.Category.objects(title='Apple4').first()
# prod1 = models.Product(**{'title': 'iPhone 11',
#                         'description': 'Apple iPhone 11 64Gb Black',
#                         'price': 300,
#                         'category': n,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/iPhone_11.webp', 'rb')
# prod1 = models.Product.objects(title='iPhone 11').first()
# prod1.photo.put(open_cart, content_type='iPhone_7/webp')
# prod1.save()

c = models.Product.objects().delete()
