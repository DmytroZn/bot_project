import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from flask import Flask, request, abort
import config
import keyboards
import datetime
from models import models
from keyboards import ReplyKB

from flask_restful import Api
from resources.product_resources import *


bot = telebot.TeleBot(config.TOKEN)
app = Flask(__name__)


# Process webhook calls
@app.route('/', methods=['POST'])  #config.handle_url
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)


@bot.message_handler(commands=['start'])
def start(message):
  
    dict_of_user = message.from_user
    user_id = models.User.objects(id_user=str(dict_of_user.id)).first()
    print(user_id)

    print(dict_of_user.id)
    if not models.User.objects(id_user=str(dict_of_user.id)):
        data_of_user = models.User(**{
            'id_user' : str(dict_of_user.id),
            'first_name' : dict_of_user.first_name,
            'username' : dict_of_user.username,
            'last_name' : dict_of_user.last_name
            }).save()
    
    greeting_str = f'Hello {dict_of_user.first_name} {dict_of_user.last_name}'
    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    bot.send_message(message.chat.id, greeting_str, reply_markup=keyboard)

    real_user_id = models.User.objects(id_user=str(dict_of_user.id)).first()
    print(real_user_id)

    if not models.Cart.objects(user=user_id, active=True):
        cart_user = models.Cart(**{'user':real_user_id}).save()
    else:
        pass


@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['news'])
def say_news(message):
    # prod = models.Product.objects(category='5dcfe1badcd794512cc89b03')
    # inlin = InlineKeyboardMarkup()
    # in1 = InlineKeyboardButton(text='test1', callback_data='testing')
    # inlin.add(in1)
    # bot.send_photo(message.chat.id, 'https://images8.alphacoders.com/953/thumb-1920-953503.jpg', caption='po', reply_markup=inlin)
    bot.send_message(message.chat.id, 'We created this bot 23.11.2019')


@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['sales'])
def say_sales(message):

    bot.send_message(message.chat.id, 'Now we don`t have product for sale')


@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['about'])
def say_about(message):

    text = '''
    This is bot-shop. 
    You can see products, choice products from categories and add products to your cart also buy.
    
    If you want have similar bot like this you can write to email: dmytro.zn@gmail.com'''
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['cart'])
def say_cart(message):

    cat = models.Category.objects().first()
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='My cart', callback_data=f'look my cart_{cat.id}')
    keyboard.add(button)
    bot.send_message(message.chat.id, text='Open cart', reply_markup=keyboard)

    
@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['history'])
def say_history(message):
    dict_of_user = message.from_user
    user_id = models.User.objects(id_user=str(dict_of_user.id)).first()
    cat = models.Cart.objects(user=user_id.id, active=False).all()
    bot.send_message(message.chat.id, text='You bought')
    if cat:
        for k in cat:
            d = k.date_time
            date = str(d).split(' ')[1].split(':')
            all_date = f'{str(d).split(" ")[0]} {date[0]}:{date[1]}'
            p = [i.title for i in k.products]  
            text = f'''{all_date} \n {', '.join(p)}'''
            print(text)
            bot.send_message(message.chat.id, text=text)
    else:
        bot.send_message(message.chat.id, text='Your history is empty') 
   

@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['products'])
def show_categories(message):
        
    kb = keyboards.InlineKB(key='root', lookup_field='id', named_arg='category')
    bot.send_message(message.chat.id, 'Chooce category', reply_markup=kb.generate_kb())


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'category')
def show_products_or_sub_category(call):
    
    """
    :param call
    :return listed
    """

    obj_id = call.data.split('_')[1]
    category = models.Category.objects(id=obj_id).get()
 
    if category.is_parent:

        kb = keyboards.InlineKB(
            iterable=category.subcategory,
            lookup_field='id',
            named_arg='category'
        )
        kb.generate_kb()
        kb.add(InlineKeyboardButton(text=f'<< {category.title}',
                            callback_data=f'back_{category.id}'))
        bot.delete_message(chat_id=call.message.chat.id,
                            message_id=call.message.message_id)
        bot.send_message(text=category.title, chat_id=call.message.chat.id,reply_markup=kb)
        # bot.edit_message_text(text=category.title, chat_id=call.message.chat.id,
        #                     message_id=call.message.message_id,
        #                     reply_markup=kb)

    else:
        print('NON PARANT')
        if call.data.split('_')[1]:
            products = models.Product.objects(category=call.data.split('_')[1])
            keyboard = InlineKeyboardMarkup(row_width=1)
            prods = [InlineKeyboardButton(text=i.title, callback_data=f'show product_{i.id}_{category.id}') for i in products]
            back = InlineKeyboardButton(text=f'<< back', callback_data=f'back_{category.id}')
            if len(prods) == 0:
                text = 'Empty'
            else:
                text = category.title
            keyboard.add(*prods)
            keyboard.add(back)

            bot.delete_message(chat_id=call.message.chat.id,
                            message_id=call.message.message_id)

            bot.send_message(text=text, chat_id=call.message.chat.id, reply_markup=keyboard)
            # bot.edit_message_text(text=text, chat_id=call.message.chat.id,
            #                 message_id=call.message.message_id,
            #                 reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'show product')
def show_prod(call):

    product = models.Product.objects(id=call.data.split('_')[1]).first()

    keyboard = InlineKeyboardMarkup()
    add_product = InlineKeyboardButton(text='Add to cart', callback_data=f'add to cart_{product.id}')
    back = InlineKeyboardButton(text='<< back', callback_data=f'category_{call.data.split("_")[2]}') # call.data.split("_")[2]}')
    look_cart = InlineKeyboardButton(text='Look my cart', callback_data=f'look my cart_{call.data.split("_")[2]}') 
    keyboard.add(add_product)
    keyboard.add(back, look_cart)

    bot.delete_message(chat_id=call.message.chat.id,
                            message_id=call.message.message_id)
    text = f"""<b>{product.title}</b>\n {product.description} \n {product.get_price_str} USD \n """
    photo = product.photo.read()
    bot.send_photo(call.message.chat.id, photo, caption=text, parse_mode='HTML', reply_markup=keyboard)
    # bot.edit_message_text(text=f"""{product.title}\n {product.description} \n {product.get_price} USD \n """, chat_id=call.message.chat.id,
    #                         message_id=call.message.message_id, reply_markup=keyboard)

    
@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'add to cart')
def add_to_cart(call):

    dict_of_user = call.from_user
    user_id = models.User.objects(id_user=str(dict_of_user.id)).first()
    print(user_id)

    if not models.Cart.objects(user=user_id, active=True):
        cart_user = models.Cart(**{'user':user_id}).save()
    else:
        pass
    cart_user = models.Cart.objects(user=user_id, active=True).first()
    ref_prod = models.Product.objects(id=call.data[12:]).first()
    cart_user.update(push__products=ref_prod)
    print(ref_prod.title)
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=f'You added {ref_prod.title}') 


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'look my cart')
def look_my_cart(call):

    user_id = models.User.objects(id_user=str(call.from_user.id)).first()
    print(f'user_id {user_id.id}')   
    if not models.Cart.objects(user=user_id, active=True):
        cart_user = models.Cart(**{'user':user_id.id}).save()
    else:
        cart_user = models.Cart.objects(user=user_id.id, active=True).first()
        print(f'cart_user {cart_user}')
    print(200)
    try:
        num1 = models.Product.objects(id=call.data.split('_')[2]).first()
        num = cart_user.products.index(num1)
        print(num)
        cart_user.products[0], cart_user.products[num] = cart_user.products[num], cart_user.products[0]
        cart_user.save()

        delete_product = cart_user.update(pop__products=-1)
        cart_user = models.Cart.objects(user=user_id.id, active=True).first()
        print('deleted')
    except (ValueError, IndexError): #, AttributeError):
        pass
    
    list_of_price = [i.get_price for i in cart_user.products]
    print(list_of_price)
    amount = (models.get_suum_of_prices(list_of_price))                                       
    keyboard = InlineKeyboardMarkup(row_width=2)
    back = InlineKeyboardButton(text='<< back', callback_data=f'category_{call.data.split("_")[1]}_{None}')
    buy = InlineKeyboardButton(text=f'pay {amount} USD', callback_data=f'buy_{call.data.split("_")[1]}')
    print([i for i in cart_user.products])
    prod_from_cart = [InlineKeyboardButton(text=f'{i.title} delete', callback_data=f'look my cart_{call.data.split("_")[1]}_{i.id}') for i in cart_user.products]
    if len(prod_from_cart) == 0:
        text='You don`t have any products \n but you can buy something'
        keyboard.add(back)
    else:
        text = 'My cart'
        keyboard.add(*prod_from_cart)
        keyboard.add(back, buy)

    bot.delete_message(chat_id=call.message.chat.id,
                            message_id=call.message.message_id)

    bot.send_message(text=text, chat_id=call.message.chat.id,
                            reply_markup=keyboard)

   
# @bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'dell')
# def delete_product(call):
#     print('dell')
#     print(call.data)
#     cart = models.Cart.objects(id=call.data.split('_')[1]).delete()
  
#     bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=f'You delete') 
     

@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'buy')
def buy_product(call):

    keyboard = InlineKeyboardMarkup()
    back = InlineKeyboardButton(text='<< back', callback_data=f'look my cart_{call.data.split("_")[1]}')
    keyboard.add(back)

    bot.edit_message_text(text='You bought!.', chat_id=call.message.chat.id,
                            message_id=call.message.message_id, reply_markup=keyboard)

    user_id = models.User.objects(id_user=str(call.from_user.id)).first()
    cart_user = models.Cart.objects(user=user_id.id, active=True).first()
    cart_user.update(active=False, date_time=datetime.datetime.now())
    print('bbbb')
    print(datetime.datetime.now())

    
@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'back')
def go_back(call):
    obj_id = call.data.split('_')[1]
    category = models.Category.objects(id=obj_id).get()
   
    if category.is_root:
        kb = keyboards.InlineKB(key='root', lookup_field='id', named_arg='category')
        kb.generate_kb()
    else:
        kb = keyboards.InlineKB(
            iterable=category.parent.subcategory,
            lookup_field='id',
            named_arg='category'
        )
        kb.generate_kb()
        kb.add(InlineKeyboardButton(text=f'<<< {category.parent.title}',
                                    callback_data=f'back_{category.parent.id}'))

    text = 'Categories' if not category.parent else category.parent.title

    bot.delete_message(chat_id=call.message.chat.id,
                            message_id=call.message.message_id)

    bot.send_message(text=text, chat_id=call.message.chat.id,
                            reply_markup=kb)
    # bot.edit_message_text(text=text, chat_id=call.message.chat.id,
    #                     message_id=call.message.message_id,
    #                     reply_markup=kb)


# wsgi
# gunicorn

if __name__ == '__main__':
    # bot.polling(none_stop=True)
    # app.run()
    import time
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(config.webhook_url,
                                certificate=open('webhook_cert.pem', 'r'))
    app.run(port=1516, debug=True)



