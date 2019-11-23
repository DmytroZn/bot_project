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
from models import models
from keyboards import ReplyKB

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




@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['news'])
def say_news(message):
    # prod = models.Product.objects(category='5dcfe1badcd794512cc89b03')

    # inlin = InlineKeyboardMarkup()
    # in1 = InlineKeyboardButton(text='test1', callback_data='testing')
    # inlin.add(in1)
    bot.send_message(message.chat.id, 'We created this bot 23.11.2019 ')


 



@bot.callback_query_handler(func=lambda call: call.data == 'testing')
def sow(call):
    prod = models.Product.objects(category='5dcfe1badcd794512cc89b03').all()
    
    inline_one = InlineKeyboardMarkup()
    in1 = [InlineKeyboardButton(text=f'{i.title}\t', callback_data=f'{i.id}_prodgood') for i in prod]
    l = InlineKeyboardButton(text='cart', callback_data='cart')
    inline_one.add(*in1)
    inline_one.add(l)
    bot.edit_message_text(text='products', chat_id=call.message.chat.id,
                                message_id=call.message.message_id, reply_markup=inline_one)
    

  
        
@bot.callback_query_handler(func=lambda call: call.data.split('_')[1] == 'prodgood')
def soe2(call):
    a = call.data.split('_')[0]
    bot.edit_message_text(text='new', chat_id=call.message.chat.id,
                                message_id=call.message.message_id)
   




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
     
        bot.edit_message_text(text=category.title, chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            reply_markup=kb)

    
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

            bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'show product')
def show_prod(call):
    product = models.Product.objects(id=call.data.split('_')[1]).first()
    keyboard = InlineKeyboardMarkup()
    add_product = InlineKeyboardButton(text='Add to cart', callback_data=f'add to cart_{product.id}')
    back = InlineKeyboardButton(text='<< back', callback_data=f'category_{call.data.split("_")[2]}')
    print(f'ba_{call.data.split("_")[2]}')
    look_cart = InlineKeyboardButton(text='Look my cart', callback_data=f'look my cart_{call.data.split("_")[2]}')
    keyboard.add(add_product)
    keyboard.add(back, look_cart)
    
    bot.edit_message_text(text=f"""{product.title}\n {product.description} \n {product.price} USD \n """, chat_id=call.message.chat.id,
                            message_id=call.message.message_id, reply_markup=keyboard)

    


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'add to cart')
def add_to_cart(call):
    
    mod = models.User.objects(id_user=str(call.from_user.id)).first()
    print(mod.id)

    m = models.Cart(**{'user':models.User.objects(id_user=str(call.from_user.id)).first(), 'product': call.data[12:]}).save()

    b = models.Product.objects(id=call.data[12:]).first()
    print(b.title)
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=f'You added {b.title}') 


             



@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'look my cart')
def look_my_cart(call):
    try:
        cart = models.Cart.objects(id=call.data.split('_')[2]).delete()
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=f'You delete') 
    except IndexError:
        pass
 


    print(call.data)


    user = models.User.objects(id_user=str(call.from_user.id)).first()
    cart = models.Cart.objects(user=user.id).all()


    keyboard = InlineKeyboardMarkup(row_width=2)
    back = InlineKeyboardButton(text='<< back', callback_data=f'category_{call.data.split("_")[1]}_{None}')
    buy = InlineKeyboardButton(text='buy', callback_data='buy')
    prod_from_cart = [InlineKeyboardButton(text=f'{i.product.title} delete', callback_data=f'look my cart_{call.data.split("_")[1]}_{i.id}') for i in cart]
    if len(prod_from_cart) == 0:
        text='You don`t have any products \n but you can buy something'
        # prod_from_cart = [InlineKeyboardButton(text='You don`t have any products \n but you can buy something', callback_data=f'category_{call.data.split("_")[1]}_{None}')]
        # keyboard.add(*prod_from_cart)
        keyboard.add(back)
        
    else:
        text = 'My cart'
        keyboard.add(*prod_from_cart)
        keyboard.add(back, buy)
    bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                            message_id=call.message.message_id, reply_markup=keyboard)

   

@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'dell')
def delete_product(call):
    print('dell')
    print(call.data)
    cart = models.Cart.objects(id=call.data.split('_')[1]).delete()
  
    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=f'You delete') 
     



   

@bot.callback_query_handler(func=lambda call: call.data == 'buy')
def buy_product(call):
    mod = models.User.objects(id_user=str(call.from_user.id)).first()
    look = models.Cart.objects(user=mod.id).all()

    if look:
        for i in look:
            look.delete()
       


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


    print(text)

    bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        reply_markup=kb)





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
    app.run(port=2328, debug=True)



