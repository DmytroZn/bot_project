from mongoengine import *



connect('web_shop_bot')



class Texts(Document):
    title = StringField(unique=True)
    body = StringField(max_lenght=4096)


class Properties(DynamicEmbeddedDocument): # не важные характеристикаи , ссылка
    weight = FloatField(min_value=0)

class Category(Document):
    title = StringField(max_lenght=255, required=True) #по люблму
    description = StringField(max_lenght=512)
    subcategory = ListField(ReferenceField('self'))
    # is_root = BooleanField(default=False)
    parent = ReferenceField('self')


    @classmethod
    def get_root_categories(cls):
        # return cls.objects(is_root=True)
        return cls.objects(parent=None)

    @property
    def is_parent(self):
        return bool(self.subcategory)

    @property
    def is_root(self):
        return not bool(self.parent)

    @property
    # для того что бы вывести все продукты из подкатегории
    def get_products(self, **kwargs):
        return Product.objects(category=self, **kwargs)

    
    def add_subcategory(self, obj):
        # return 'subcategory'
        obj.parent = self
        obj.save()
        self.subcategory.append(obj)
        self.save()


# def ref(value=None):
#     if value != None:
#         obj = Category.objects(id=value).first()
#         return obj.id
#     else:
#         return Category



class Product(Document):
    title = StringField(max_lenght=255)
    description = StringField(max_lenght=1024)
    price = IntField(min_value=0)
    new_price = IntField(min_value=0)
    is_discount = BooleanField(default=False)
    properties = EmbeddedDocumentField(Properties)
    category = ReferenceField(Category)
    photo = FileField()





    @property
    def get_price(self):
        if self.is_discount:
            return self.new_price
        return self.price

    @property
    def get_price_str(self):
        if self.is_discount:
            return str(self.new_price / 100)
        return str(self.price / 100)   

def get_suum_of_prices(list_of_price):
    c = 0
    for i in list_of_price:
        c += i
    return c / 100
    

    
    @classmethod
    def get_discount_products(cls):
        return cls.objects(is_discount=True, **kwargs)



class User(Document):
    id_user = StringField()
    first_name = StringField()
    username = StringField()
    last_name = StringField()


class Cart(Document):
    user = ReferenceField(User)
    products = ListField(ReferenceField(Product))
    active = BooleanField(default=True)
    date_time = DateTimeField()
   


# Category.objects.update(is_root=True)
# list_of_catteg = [i.title for i in Category.objects()]


class Testing(Document):
    name = StringField()
    last_name = StringField()
    list_of = ListField(ReferenceField(Product))











