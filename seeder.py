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


# c = models.Product.objects().delete()
# c = models.Category.objects().delete()
# c = models.Cart.objects().delete()
# c = [i.title for i in models.Category.objects().all()]
# print(c)


# for i in range(5):
#     obj = models.Category(**{'title':f'root {i}',
#                         'description':f'descr {i}'}).save()


############################


# obj1 = models.Category(**{'title': 'Mobile phones', 'description': 'there are mobile phones'}).save()

# obj1.add_subcategory(
#         models.Category(**{'title': 'Apple',
#                             'description': 'there are iPhone'}))
                
# obj1.add_subcategory(
#         models.Category(**{'title': 'Meizu',
#                             'description': 'there are Meizu'}))
                            
# obj1.add_subcategory(
#         models.Category(**{'title': 'Xiaomi',
#                             'description': 'there are Xiaomi'}))    
                                 
# obj1.add_subcategory(
#         models.Category(**{'title': 'Samsung',
#                             'description': 'there are Samsung'}))  
# 




# obj2 = models.Category(**{'title': 'Audio', 'description': 'there are Accessories for phones'}).save()
# # # obj2 = models.Category.objects(title='Audio').first()

# obj2.add_subcategory(
#         models.Category(**{'title': 'Earphones',
#                             'description': 'there are earphones'}))
                
# obj2.add_subcategory(
#         models.Category(**{'title': 'Acoustics',
#                             'description': 'there are Acoustics'}))

# # # models.Product.objects.all().delete()
# n = models.Category.objects(title='Apple').first()
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


# o = models.Category.objects(title='Earphones').first()
# o.add_subcategory(
#     models.Category(**{'title': 'Wireless earphones',
#                             'description': 'there are Wireless earphones'})
# )

# o.add_subcategory(
#     models.Category(**{'title': 'Leading earphones',
#                             'description': 'there are Leading earphones'})
# )


#
# n = models.Category.objects(title='Apple').first()
# prod1 = models.Product(**{'title': 'iPhone 7',
#                         'description': 'Apple iPhone 7 128Gb Black',
#                         'price': 40000,
#                         'category': n,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/iPhone_7.webp', 'rb')
# prod1 = models.Product.objects(title='iPhone 7').first()
# prod1.photo.put(open_cart, content_type='iPhone_7/webp')
# prod1.save()

# #
# prod1 = models.Product(**{'title': 'iPhone 8',
#                         'description': 'Apple iPhone 8 128Gb Gold',
#                         'price': 35000,
#                         'category': n,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/iPhone_8.webp', 'rb')
# prod1 = models.Product.objects(title='iPhone 8').first()
# prod1.photo.put(open_cart, content_type='iPhone_8/webp')
# prod1.save()

# #

# prod1 = models.Product(**{'title': 'iPhone X',
#                         'description': 'Apple iPhone X 64Gb Silver',
#                         'price': 35000,
#                         'category': n,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/iphone_X.webp', 'rb')
# prod1 = models.Product.objects(title='iPhone X').first()
# prod1.photo.put(open_cart, content_type='iPhone_X/webp')
# prod1.save()

# #
# m = models.Category.objects(title='Meizu').first()
# prod1 = models.Product(**{'title': 'Meizu 16Xs',
#                         'description': 'Meizu 16Xs 64Gb Carbon Black',
#                         'price': 22500,
#                         'category': m,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/Meizu_16Xs.jpg', 'rb')
# prod1 = models.Product.objects(title='Meizu 16Xs').first()
# prod1.photo.put(open_cart, content_type='Meizu_16Xs/jpg')
# prod1.save()
#


# prod1 = models.Product(**{'title': 'Meizu M5',
#                         'description': 'Meizu M5 16GB White',
#                         'price': 15700,
#                         'category': m,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/Meizu_M5.jpg', 'rb')
# prod1 = models.Product.objects(title='Meizu M5').first()
# prod1.photo.put(open_cart, content_type='Meizu_M5/jpg')
# prod1.save()

# #
# prod1 = models.Product(**{'title': 'Meizu M10',
#                         'description': 'Meizu M10 32Gb Black',
#                         'price': 10105,
#                         'category': m,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/Meizu_M10.jpg', 'rb')
# prod1 = models.Product.objects(title='Meizu M10').first()
# prod1.photo.put(open_cart, content_type='Meizu_M10/jpg')
# prod1.save()

#


#

# s = models.Category.objects(title='Samsung').first()
# prod1 = models.Product(**{'title': 'Samsung Galaxy A50',
#                         'description': 'Samsung Galaxy A50 2019 64Gb White',
#                         'price': 45865,
#                         'category': s,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/Samsung_Galaxy_A50.webp', 'rb')
# prod1 = models.Product.objects(title='Samsung Galaxy A50').first()
# prod1.photo.put(open_cart, content_type='Samsung_Galaxy_A50/webp')
# prod1.save()

# #

# prod1 = models.Product(**{'title': 'Samsung Galaxy Note 10 Plus',
#                         'description': 'Samsung Galaxy Note 10 Plus 2019 256Gb Aura Black',
#                         'price': 45000,
#                         'category': s,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/Samsung_Galaxy_Note_10_Plus.webp', 'rb')
# prod1 = models.Product.objects(title='Samsung Galaxy Note 10 Plus').first()
# prod1.photo.put(open_cart, content_type='Samsung_Galaxy_Note_10_Plus/webp')
# prod1.save()

# #



# x = models.Category.objects(title='Xiaomi').first()
# prod1 = models.Product(**{'title': 'Xiaomi Redmi Note 8',
#                         'description': 'Xiaomi Redmi Note 8 64Gb Blue',
#                         'price': 29900,
#                         'category': x,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/Xiaomi_Redmi_Note_8.webp', 'rb')
# prod1 = models.Product.objects(title='Xiaomi Redmi Note 8').first()
# prod1.photo.put(open_cart, content_type='Xiaomi_Redmi_Note_8/webp')
# prod1.save()

# #
# prod1 = models.Product(**{'title': 'Xiaomi Redmi Note 8 Pro',
#                         'description': 'Xiaomi Redmi Note 8 Pro 128Gb Green',
#                         'price': 50900,
#                         'category': x,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/Xiaomi_Redmi_Note_8_Pro.webp', 'rb')
# prod1 = models.Product.objects(title='Xiaomi Redmi Note 8 Pro').first()
# prod1.photo.put(open_cart, content_type='Xiaomi_Redmi_Note_8_Pro/webp')
# prod1.save()

# o = models.Category.objects(title='Wireless earphones').first()
# o.add_subcategory(
#     models.Category(**{'title': 'Apple',
#                             'description': 'there are airpods'})
# )


# air = models.Category.objects(title='Apple', description='there are airpods').first()

# prod1 = models.Product(**{'title': 'AirPods 2019',
#                         'description': 'Apple AirPods 2019 with Charging Case',
#                         'price': 50900,
#                         'category': air,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/Apple_AirPods_2019.webp', 'rb')
# prod1 = models.Product.objects(title='AirPods 2019').first()
# prod1.photo.put(open_cart, content_type='Apple_AirPods_2019/webp')
# prod1.save()

#

# air = models.Category.objects(title='Leading earphones').first()

# prod1 = models.Product(**{'title': 'Earphones JBL T110',
#                         'description': 'Earphones JBL T110 White',
#                         'price': 2500,
#                         'category': air,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/Earphones_JBL_T110.webp', 'rb')
# prod1 = models.Product.objects(title='Earphones JBL T110').first()
# prod1.photo.put(open_cart, content_type='Earphones_JBL_T110/webp')
# prod1.save()

#



# air = models.Category.objects(title='Acoustics').first()

# prod1 = models.Product(**{'title': 'Portable speaker',
#                         'description': 'Portable speaker AIR MUSIC FLIP Orange',
#                         'price': 4700,
#                         'category': air,
#                         # 'photo': None
#                        }).save()

# open_cart = open('photos/Portable_speaker.webp', 'rb')
# prod1 = models.Product.objects(title='Portable speaker').first()
# prod1.photo.put(open_cart, content_type='Portable_speaker/webp')
# prod1.save()
i = models.User.objects().all()
print(f'first_name {[k.first_name for k in i]}')
print(f'id_user {[k.id_user for k in i]}')


print("username {[k.username for k in i]}")

u = models.Cart.objects(active=False).all()
print("cart {[i.user.first_name for i in u]}")