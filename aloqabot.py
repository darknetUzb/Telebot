import telebot


bot = telebot.TeleBot('5263064696:AAFJZPsPCB6ilttPH3lK9yvfFLahCgPxfnw')


@bot.message_handler(commands=['start'])
def start_cmd(message):
	bot.send_message(message.chat.id, '💌Salom %s\n🔱Savolingiz bolsa yozib qoldiring\n🔰Yoki Nimadadir hatolik qilgan bolsangiz screenshot tashlang\n✅Barcha savollaringizga 24 soat ichida javob olasiz\n🦾kanallarimizga obuna boling..\n@magicbot_uz\n@darknet7719\n@darknet_off1cial\n@darknet_hacking_books ' % message.from_user.username)




bot.polling(none_stop=True)