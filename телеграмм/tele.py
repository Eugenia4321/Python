import logging
from telegram import Update
from config import TOKEN,ERROR_MESSAGE
#from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler
from anecAPI import anecAPI
from operations import tele_sum, tele_div, tele_mult,tele_sub,tele_complex,check_digit

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='py_log.log', filemode='w',encoding='UTF-8')
#logging.debug("A DEBUG Message")
#logging.info("An INFO")
#logging.warning("A WARNING")
#logging.error("An ERROR")
#logging.critical("A message of CRITICAL severity")
logger =logging.getLogger(__name__)


#async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #await update.message.reply_text(f'Hello {update.effective_user.first_name}')
#app = ApplicationBuilder().token("").build()
#app.add_handler(CommandHandler("hello", hello))
#app.run_polling()


def make_joke(update: Update,context:CallbackContext):       #апдейт последнее сообщение   контекст - доступно на весь чат
    after_command = context.args                             #  возвращает текст после команды
    print(after_command)                                     #
    update.message.reply_text(anecAPI.modern_joke())         #anecAPI.modern_joke() вовращающийся текст

def get_massage(update: Update,context:CallbackContext):
    message = update.message.text
    print(message)
    if 'прив' in message:
        update.message.reply_text(f'Привет!')
        return None
    update.message.reply_text(f'Вы ввели "{message}" и я пока не знаю такой команды!')
    logging.info(f'ввод незнакомой команды"{message}"')  # c русским языком проблемы почему то

def start_bot(update: Update,context:CallbackContext):
    after_command = context.args                            
    print(after_command)                                     
    update.message.reply_text(
        'Добро пожаловать в бот из домашнего задания 9 семинара!\n'
        'Я умею складывать, умножать, вычитать и делить целые числа\n'
        'Введи /menu что бы узнать какие команды я знаю'
        )
def menu_bot(update: Update,context:CallbackContext):
    after_command = context.args                            
    print(after_command)                                     
    update.message.reply_text(
        '/menu  -- посмотреть на мое меню\n'
        '/sum A B - введи два числа без "+" между ними, что бы я смог их сложить\n'
        '/div A B - введи два числа без "/" между ними, что бы я смог их разделить\n'
        '/mult A B - введи два числа без "*" между ними, что бы я смог их умножить\n'
        '/sub A B - введи два числа без "-" между ними, что бы я смог их вычесть\n'
        '/complex a+bi"знак операции"c+di - введи комплексные числа и операцию между ними, что бы я вычислил результат  \n'
        '/help - раздел помощи с примерами \n'
        )
def help_bot(update: Update,context:CallbackContext):
    after_command = context.args                            
    print(after_command)                                     
    update.message.reply_text(
        '/menu  -- посмотреть на мое меню\n'
        '/sum A B  -- пример: "/sum 11 -1" мой ответ:"11 + -1 = 10" \n'
        '/div A B -  пример: "/sum 11 -1" мой ответ:"11 + -1 = 10"\n'
        '/mult A B -  пример: "/mult 10 5" мой ответ:"10 * 5 = 50"\n'
        '/sub A B -  пример: "/sub 5 5" мой ответ:"5 - 5 = 0"\n'
        '/complex a+bi/c+di пример: "/complex -9-7i/(-1+i)"\nмой ответ:"1.0+8.0i"  \n'
        '/complex a+bi*c+di пример: "/complex -9-7i*(-1+i)" \nмой ответ:"16+(-2i)"  \n'
        '/complex a+bi-c+di пример: "/complex -9-7i-(-1+i)" \nмой ответ:"-8 + (-8i)"  \n'
        '/complex a+bi-c+di пример: "/complex -9-7i+(-1+i)" \nмой ответ:"-10 + (-6i)"  \n'
        )        
def sum_bot(update: Update,context:CallbackContext):
    after_command = context.args 
    print(after_command) 
    update.message.reply_text(tele_sum(after_command)) 
    logging.info(f'сложение"{after_command}"') 
          
def div_bot(update: Update,context:CallbackContext):
    after_command = context.args                            
    print(after_command)                                     
    update.message.reply_text(tele_div(after_command)) 
    logging.info(f'деление"{after_command}"')  
def mult_bot(update: Update,context:CallbackContext):
    after_command = context.args                            
    print(after_command)                                     
    update.message.reply_text(tele_mult(after_command))  
    logging.info(f'умножение"{after_command}"') 
def sub_bot(update: Update,context:CallbackContext):
    after_command = context.args                            
    print(after_command)                                     
    update.message.reply_text(tele_sub(after_command))   
    logging.info(f'вычитание"{after_command}"')   

def complex_bot(update: Update,context:CallbackContext):
    after_command = context.args                            
    print(after_command)                                     
    update.message.reply_text(tele_complex(after_command))
    logging.info(f'комплексные"{after_command}"') 

updater = Updater(TOKEN)
dispetcher = updater.dispatcher

help_bot_handler = CommandHandler('help',help_bot)
menu_bot_handler = CommandHandler('menu',menu_bot)
complex_handler = CommandHandler('complex',complex_bot)
sub_handler = CommandHandler('sub',sub_bot)
mult_handler = CommandHandler('mult',mult_bot)
div_handler = CommandHandler('div',div_bot)
sum_handler = CommandHandler('sum',sum_bot)
start_handler = CommandHandler('start',start_bot)
joke = CommandHandler('joke',make_joke)
messege_handler = MessageHandler(Filters.text,get_massage)

dispetcher.add_handler(help_bot_handler)
dispetcher.add_handler(menu_bot_handler)
dispetcher.add_handler(complex_handler)
dispetcher.add_handler(joke)
dispetcher.add_handler(start_handler)
dispetcher.add_handler(sum_handler)
dispetcher.add_handler(mult_handler)
dispetcher.add_handler(div_handler)
dispetcher.add_handler(sub_handler)
dispetcher.add_handler(messege_handler)         #месседж хендлер после всех команд или хендлеры не сработают



print('старт')
updater.start_polling() #получать сообщения
updater.idle() #стоп