import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

import config
import keyboards
from models import models
from keyboards import ReplyKB

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # greetings_str = models.Texts(title='Greetings').get().body # получаемобект get()
    greeting_str = 'Not'

    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    # keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # buttons = [KeyboardButton(x) for x in keyboards.beginning_kb.values()]
    # keyboard.add(*buttons)
    # bot.register_next_step_handler(message, inline)
    bot.send_message(message.chat.id, greeting_str, reply_markup=keyboard)
    

@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['products'])
def show_categories(message):
    
    # category_queryset = models.Category.get_root_categories()
    kb = keyboards.InlineKB(key='root', lookup_field='id', named_arg='category')

    bot.send_message(message.chat.id, 'Chooce category', reply_markup=kb.generate_kb())




# @bot.callback_query_handler(funk=lambda call: True)
# def test(call):
#     print(call.data)




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
        
        # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.generate_kb())

    # elif call.text == 'Sub of sub':
    #     bot.send_photo(call.message.chat.id, 'https://images8.alphacoders.com/953/thumb-1920-953503.jpg')

    
    else:
        # bot.send_message(call.message.chat.id, 'sdfsf')
        # bot.send_photo(call.message.chat.id, 'https://images8.alphacoders.com/953/thumb-1920-953503.jpg')
        print('NON PARANT')
        
        # if call.data.split('_')[1] == '5dcaf2ac3db8e6530cc686ee':
        if call.data.split('_')[1]:
    
            keyboard = InlineKeyboardMarkup()
            b = InlineKeyboardButton('add to cart', callback_data='add to cart')
            keyboard.add(b)

            print('200')
            
            # obj = models.Category(
            # u = models.Product.objects(category='5dcaf2ac3db8e6530cc686ee')
            u = models.Product.objects(category=call.data.split('_')[1])

            for i in u:
                bot.send_message(call.message.chat.id, i.title)
                bot.send_photo(call.message.chat.id, 'https://images8.alphacoders.com/953/thumb-1920-953503.jpg')
                bot.send_message(call.message.chat.id, i.description,reply_markup=keyboard)
            # print(models.Product.get_price)
            # bot.send_message(call.message.chat.id, 'Inline Mode', reply_markup=keyboard)

            # bot.send_message(message.chat.id, 'Inline Mode', reply_markup=keyboard)
            # p = models.Category.get_products(models.Product.objects())
            # print(p)
          
            
            # bot.send_message(call.message.chat.id, 'title')
            # bot.send_photo(call.message.chat.id, 'https://images8.alphacoders.com/953/thumb-1920-953503.jpg')
        
@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'back')
def go_back(call):
    obj_id = call.data.split('_')[1]
    category = models.Category.objects(id=obj_id).get()
   
    if category.is_root:
        # category_queryset = models.Category.get_root_categories()
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
    bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        reply_markup=kb)



##############3
# @bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['Sub of sub'])
# def show_categories(message):
#     bot.send_photo(message.chat.id, 'https://images8.alphacoders.com/953/thumb-1920-953503.jpg')

    # category_queryset = models.Category.get_root_categories()
    # kb = keyboards.InlineKB(
    #     iterable=category_queryset,
    #     lookup_field='id',
    #     named_arg='category',
    #     # named_arg='myobj'
    #     # title_field = 'id'
    # )

    # bot.send_message(message.chat.id, 'Chooce categot', reply_markup=kb.generate_kb())


#############
# bot.send_photo(message.chat.id, 'https://images8.alphacoders.com/953/thumb-1920-953503.jpg')







# @bot.message_handler(commands=['inline'])
# def inline(message):
#     if message.text == 'Products':
#         keyboard = InlineKeyboardMarkup()
#         buttons = [InlineKeyboardButton(k, callback_data=str(k)) for k in [*models.list_of_catteg]]
#         keyboard.add(*buttons)
#         bot.send_message(message.chat.id, 'Inline Mode', reply_markup=keyboard)

    ###
# @bot.message_handler(commands=['inline'])
# def check(message):
#     if message.text == 'Products':
#         bot.send_message(message.chat.id, 'LLL')
# @bot.message_handler(commands=['start'])


# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'He'


if __name__ == '__main__':
    bot.polling(none_stop=True)
    # app.run()




