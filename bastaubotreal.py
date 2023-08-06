import telebot
from telebot import types

bot = telebot.TeleBot('6245253315:AAEEp1TWAFtEcAM6EG3j__rM9zwJFw81V-U')


@bot.message_handler(commands=["start"])
def start(message):
    mess = f'Салем,{message.from_user.first_name} егер бір нәрсе түсініксіз болса - MENU-ға кіріп komek басыңыз, ал егер бәрі түсінікті болса 😃 басыңыз!'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1 = types.KeyboardButton(text="😃")
    markup.add(keyboard1)
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "😃":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard2 = types.KeyboardButton('✅')
        keyboard3 = types.KeyboardButton('❌')
        markup.add(keyboard2, keyboard3)
        bot.send_message(message.chat.id, "Онда видео сабақтар көргіңіз келеді ма ия болса ✅, жоқ болса ❌", reply_markup=markup, parse_mode='html')
    if message.text == "✅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1 = types.KeyboardButton('1️⃣')
        keyboard2 = types.KeyboardButton('2️⃣')
        keyboard3 = types.KeyboardButton('3️⃣')
        keyboard4 = types.KeyboardButton('4️⃣')
        keyboard5 = types.KeyboardButton('')
        keyboard6 = types.KeyboardButton('')
        markup.add(keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6)
        bot.send_message(message.chat.id, "Видео сабақ тақырыбын таңдаңыз және сол тандаған тақырыбының санын чатқа енгізіңіз! ", reply_markup=markup, parse_mode='html')
        photo = open(r"https://drive.google.com/file/d/13kV-XdLk0evE0sSeHpTu8gLdTMvqAJGg/view?usp=drive_link", 'rb')
        bot.send_photo(message.chat.id, photo=photo)

    if message.text == "/komek":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard2 = types.KeyboardButton('😃')
        markup.add(keyboard2)
        photo = open(r"https://drive.google.com/file/d/190LT0vPELxdX8F8XD8AW47fClMJS5_wQ/view?usp=drive_link", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
        bot.send_message(message.chat.id, "Егер бәрі түсінікті болса 😃 басыңыз!", reply_markup=markup, parse_mode='html')
    if message.text == "/formula":
        photo = open(r"https://drive.google.com/file/d/1jK20gsCah537293F3PH0T-I6bG9DSaIx/view?usp=drive_link", 'rb')
        bot.send_photo(message.chat.id, photo=photo)

    if message.text == "1️⃣":
        video = open(r"https://drive.google.com/file/d/1ExqQn9gCYf2OgB9DNg8mpq_ZoNeO7kYL/view?usp=drive_link", 'rb')
        bot.send_video(message.chat.id, video=video)
    if message.text == "2️⃣":
        video = open(r"https://drive.google.com/file/d/1DPr1UHmySN8MWWyD9gUMzB5Py7vwTWJG/view?usp=drive_link", 'rb')
        bot.send_video(message.chat.id, video=video)
    if message.text == "3️⃣":
        video = open(r"https://drive.google.com/file/d/1m8ODhFOnd5FGhH1XChyeahkRI3dnPYwH/view?usp=drive_link", 'rb')
        bot.send_video(message.chat.id, video=video)
    if message.text == "4️⃣":
        video = open(r"https://drive.google.com/file/d/1FXg5Aijp3sj7URoYNS6iGnnwMVFr7wmx/view?usp=drive_link", 'rb')
        bot.send_video(message.chat.id, video=video)

    if message.text == "❌":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1 = types.KeyboardButton('💭')
        keyboard2 = types.KeyboardButton('⚙️')
        keyboard3 = types.KeyboardButton('🔰')
        keyboard4 = types.KeyboardButton('🌍')
        markup.add(keyboard1, keyboard2, keyboard3, keyboard4)
        bot.send_message(message.chat.id, "Ендеше тест тақырыптарын таңдаңыз  1-💭, 2-⚙️, 3-🔰, 4-🌍, ",
                         reply_markup=markup, parse_mode='html')
        photo = open(r"https://drive.google.com/file/d/13kV-XdLk0evE0sSeHpTu8gLdTMvqAJGg/view?usp=drive_link", 'rb')
        bot.send_photo(message.chat.id, photo=photo)

    if message.text == "💭":
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton('1.1', callback_data='button1')
        item2 = types.InlineKeyboardButton('1.2', callback_data='button2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Есеп таңдаңыз!", reply_markup=markup)

    if message.text == "Жауабы1.1":
        markup = types.InlineKeyboardMarkup(row_width=1)
        answer1 = types.InlineKeyboardButton('S)-1; -2,5; 5; 5; 2,5; 1', callback_data='button3')
        answer2 = types.InlineKeyboardButton('A)-11; -2,5; -5; 5; 2,5; 1', callback_data='button4')
        answer3 = types.InlineKeyboardButton('I)-1; -2,5; 5; -5; 2,5; 1', callback_data='button5')
        answer4 = types.InlineKeyboardButton('D)-1; -2,5; -5; 5; 2,5; 1', callback_data='button6')
        markup.add(answer1, answer2, answer3, answer4)
        bot.send_message(message.chat.id, "Қай жауап дұрыс?", reply_markup=markup)
        item1 = types.InlineKeyboardButton('Жауабы1.1', callback_data='answer1.1')
        markup.add(item1)

    if message.text == "1.2":
        photo = open(r"https://drive.google.com/file/d/1pY2IM7im87RgIwDTqUoghuF5RSs3Z675/view?usp=drive_link", 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    if message.text == "Жауабы1.2":
        markup = types.InlineKeyboardMarkup(row_width=1)
        answer1 = types.InlineKeyboardButton('S)-1', callback_data='button7')
        answer2 = types.InlineKeyboardButton('A)1', callback_data='button8')
        answer3 = types.InlineKeyboardButton('I)3', callback_data='button9')
        answer4 = types.InlineKeyboardButton('D)дұрыс жауап жоқ', callback_data='button10')
        markup.add(answer1, answer2, answer3, answer4)
        bot.send_message(message.chat.id, "Қай жауап дұрыс?", reply_markup=markup)

    if message.text == "⚙️":
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton('2.1', callback_data='button11')
        item2 = types.InlineKeyboardButton('2.2', callback_data='button12')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Есеп таңдаңыз!", reply_markup=markup)

    if message.text == "Жауабы2.1":
        markup = types.InlineKeyboardMarkup(row_width=1)
        answer1 = types.InlineKeyboardButton('S)x^2-2xy+y^2', callback_data='button13')
        answer2 = types.InlineKeyboardButton('A)x^2-xy-y^2', callback_data='button14')
        answer3 = types.InlineKeyboardButton('I)x^2-2xy-y^2', callback_data='button15')
        answer4 = types.InlineKeyboardButton('D)x^2+2xy+y^2', callback_data='button16')
        markup.add(answer1, answer2, answer3, answer4)
        bot.send_message(message.chat.id, "Қай жауап дұрыс?", reply_markup=markup)
    if message.text == "Жауабы2.2":
        markup = types.InlineKeyboardMarkup(row_width=1)
        answer1 = types.InlineKeyboardButton('S)75', callback_data='button17')
        answer2 = types.InlineKeyboardButton('A)70', callback_data='button18')
        answer3 = types.InlineKeyboardButton('I)125', callback_data='button19')
        answer4 = types.InlineKeyboardButton('D)25', callback_data='button20')
        markup.add(answer1, answer2, answer3, answer4)
        bot.send_message(message.chat.id, "Қай жауап дұрыс?", reply_markup=markup)

    if message.text == "🔰":
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton('3.1', callback_data='button21')
        item2 = types.InlineKeyboardButton('3.2', callback_data='button22')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Есеп таңдаңыз!", reply_markup=markup)

    if message.text == "Жауабы3.1":
        markup = types.InlineKeyboardMarkup(row_width=1)
        answer1 = types.InlineKeyboardButton('S)x^2-12xy+xy^2', callback_data='button23')
        answer2 = types.InlineKeyboardButton('A)x^2+12x+y^2', callback_data='button24')
        answer3 = types.InlineKeyboardButton('I)x^2+12x+36', callback_data='button25')
        answer4 = types.InlineKeyboardButton('D)x+2xy+y', callback_data='button26')
        markup.add(answer1, answer2, answer3, answer4)
        bot.send_message(message.chat.id, "Қай жауап дұрыс?", reply_markup=markup)
    if message.text == "Жауабы3.2":
        markup = types.InlineKeyboardMarkup(row_width=1)
        answer1 = types.InlineKeyboardButton('S)x^2-14xy+49', callback_data='button27')
        answer2 = types.InlineKeyboardButton('A)x^2+14x+y^2', callback_data='button28')
        answer3 = types.InlineKeyboardButton('I)x^2-14y^2-y^2', callback_data='button29')
        answer4 = types.InlineKeyboardButton('D)x+14xy+y', callback_data='button30')
        markup.add(answer1, answer2, answer3, answer4)
        bot.send_message(message.chat.id, "Қай жауап дұрыс?", reply_markup=markup)

    if message.text == "🌍":
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton('4.1', callback_data='button31')
        item2 = types.InlineKeyboardButton('4.2', callback_data='button32')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Есеп таңдаңыз!", reply_markup=markup)
    if message.text == "Жауабы4.1":
        markup = types.InlineKeyboardMarkup(row_width=1)
        answer1 = types.InlineKeyboardButton('S)a^3-15+xy^2', callback_data='button33')
        answer2 = types.InlineKeyboardButton('A)a^3+15a^2+75a^3-125', callback_data='button34')
        answer3 = types.InlineKeyboardButton('I)a^3+5a+75a^2-125', callback_data='button35')
        answer4 = types.InlineKeyboardButton('D)a^3+15a^2+75a-125', callback_data='button36')
        markup.add(answer1, answer2, answer3, answer4)
        bot.send_message(message.chat.id, "Қай жауап дұрыс?", reply_markup=markup)
    if message.text == "Жауабы4.2":
        markup = types.InlineKeyboardMarkup(row_width=1)
        answer1 = types.InlineKeyboardButton('S)a^3+6a+12a-8', callback_data='button37')
        answer2 = types.InlineKeyboardButton('A)a^3+6a^2+12a+8', callback_data='button38')
        answer3 = types.InlineKeyboardButton('I)a^3+a^2-12a-8', callback_data='button39')
        answer4 = types.InlineKeyboardButton('D)a^2-6a^2+12a+8', callback_data='button40')
        markup.add(answer1, answer2, answer3, answer4)
        bot.send_message(message.chat.id, "Қай жауап дұрыс?", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call, message=None):
        if call.data == "button1":
            photo = open(r"https://drive.google.com/file/d/1E62rwbFG76fDIODSdzSbSqtAW9koC0u5/view?usp=drive_link", 'rb')
            bot.send_photo(call.message.chat.id, photo=photo)
            bot.send_message(call.message.chat.id, 'Жауабын көріп белгілегіңіз келсе Жауабы1.1 деп жазыңыз')
        if call.data == "button2":
            photo = open(r"https://drive.google.com/file/d/1pY2IM7im87RgIwDTqUoghuF5RSs3Z675/view?usp=drive_link", 'rb')
            bot.send_photo(call.message.chat.id, photo=photo)
            bot.send_message(call.message.chat.id, 'Жауабын көріп белгілегіңіз келсе Жауабы1.2 деп жазыңыз')
        if call.data == "button3":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!",
                             parse_mode='html')
        if call.data == "button5":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!",
                             parse_mode='html')
        if call.data == "button6":
            bot.send_message(call.message.chat.id, '👍🏻')
            bot.send_message(call.message.chat.id, "Өте жақсы, жарайсыз келесі есептерді шығара беріңіз",
                             parse_mode='html')
        if call.data == "button7":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!",
                             parse_mode='html')
        if call.data == "button8":
            bot.send_message(call.message.chat.id, '👍🏻')
            bot.send_message(call.message.chat.id, "Өте жақсы, жарайсыз келесі есептерді шығара беріңіз",
                             parse_mode='html')
        if call.data == "button9":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button10":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button11":
            photo = open(r"https://drive.google.com/file/d/1r29UKH1v-7MMiJNrhHFDp3Ui0baA_MYu/view?usp=drive_link", 'rb')
            bot.send_photo(call.message.chat.id, photo=photo)
            bot.send_message(call.message.chat.id, 'Жауабын көріп белгілегіңіз келсе Жауабы2.1 деп жазыңыз')
        if call.data == "button12":
            photo = open(r"https://drive.google.com/file/d/1fWtS4u5ddUXbMgogTCRKaZQWkabRyC9K/view?usp=drive_link", 'rb')
            bot.send_photo(message.chat.id, photo=photo)
            bot.send_message(call.message.chat.id, 'Жауабын көріп белгілегіңіз келсе Жауабы2.2 деп жазыңыз')
        if call.data == "button13":
            bot.send_message(call.message.chat.id, '👍🏻')
            bot.send_message(call.message.chat.id, "Өте жақсы, жарайсыз келесі есептерді шығара беріңіз",
                             parse_mode='html')
        if call.data == "button14":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button15":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button16":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button17":
            bot.send_message(call.message.chat.id, '👍🏻')
            bot.send_message(call.message.chat.id, "Өте жақсы, жарайсыз келесі есептерді шығара беріңіз",
                             parse_mode='html')
        if call.data == "button18":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button19":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button20":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button21":
            photo = open(r"https://drive.google.com/file/d/1z2kcsTfXtT_k3ahgdkYeNQjDrLnnmaLR/view?usp=drive_link", 'rb')
            bot.send_photo(message.chat.id, photo=photo)
            bot.send_message(call.message.chat.id, 'Жауабын көріп белгілегіңіз келсе Жауабы3.1 деп жазыңыз')
        if call.data == "button22":
            photo = open(r"https://drive.google.com/file/d/1nFQ9hqBqODAWtFtk8zdTzyx8Hv5jS7Ph/view?usp=drive_link", 'rb')
            bot.send_photo(message.chat.id, photo=photo)
            bot.send_message(call.message.chat.id, 'Жауабын көріп белгілегіңіз келсе Жауабы3.2 деп жазыңыз')
        if call.data == "button23":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button24":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button25":
            bot.send_message(call.message.chat.id, '👍🏻')
            bot.send_message(call.message.chat.id, "Өте жақсы, жарайсыз келесі есептерді шығара беріңіз",
                             parse_mode='html')
        if call.data == "button26":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button27":
            bot.send_message(call.message.chat.id, '👍🏻')
            bot.send_message(call.message.chat.id, "Өте жақсы, жарайсыз келесі есептерді шығара беріңіз",
                             parse_mode='html')
        if call.data == "button28":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button29":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button30":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button31":
            photo = open(r"https://drive.google.com/file/d/1in4saQE9mJ4UhDW4qXdBeOx5Xd5p3LLk/view?usp=drive_link", 'rb')
            bot.send_photo(message.chat.id, photo=photo)
            bot.send_message(call.message.chat.id, 'Жауабын көріп белгілегіңіз келсе Жауабы4.1 деп жазыңыз')
        if call.data == "button32":
            photo = open(r"https://drive.google.com/file/d/1_WYkS3TrRO3S1Hb9RdfNmOjk8kG0Eh7D/view?usp=drive_link", 'rb')
            bot.send_photo(message.chat.id, photo=photo)
            bot.send_message(call.message.chat.id, 'Жауабын көріп белгілегіңіз келсе Жауабы4.2 деп жазыңыз')
        if call.data == "button33":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button34":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button35":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button36":
            bot.send_message(call.message.chat.id, '👍🏻')
            bot.send_message(call.message.chat.id, "Өте жақсы, жарайсыз келесі есептерді шығара беріңіз",
                             parse_mode='html')
        if call.data == "button37":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button38":
            bot.send_message(call.message.chat.id, '👍🏻')
            bot.send_message(call.message.chat.id, "Өте жақсы, жарайсыз келесі есептерді шығара беріңіз",
                             parse_mode='html')
        if call.data == "button39":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")
        if call.data == "button40":
            bot.send_message(call.message.chat.id, '🙅🏻‍♂')
            bot.send_message(call.message.chat.id, "ӨКІНІШКЕ ОРАЙ СІЗ ЖАУАП БЕРЕ АЛМАДЫҢЫЗ ОЙЛАНЫҢЫЗ!")



bot.polling(none_stop=True)
