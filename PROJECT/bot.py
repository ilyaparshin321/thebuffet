import telebot
import config
import random
import sqlite3
import sql_etc as s
import os
import sys
import base64

from telebot import types as ty


admin_list = ["ilyaparshin321", "paulparshin"]
bot = telebot.TeleBot(config.TOKEN)

class cafe: # класс для информации о точках сети
    name = ""
    description = ""
    location = ""
    photo = ""

    def __init__(self, n, d, l, p):
        self.name = n
        self.description = d
        self.location = l
        self.photo = p


class markup: # класс для удобного объявления объектов типа types.ReplyKeyboardMarkup в некоторых подходящих для этого случаях
    m = ty.ReplyKeyboardMarkup()
    def __init__(self, a):
        self.m = ty.ReplyKeyboardMarkup()
        for i in a: self.m.add(ty.KeyboardButton(str(i)))


class good: # класс для информации о товаре
    name = ""
    description = ""
    price = ""
    ex_ln = ""
    ex_m55 = ""
    cat = ""

    def __init__(self, n, d, p, e1, e2, c):
        self.name = n
        self.description = d
        self.price = p
        self.ex_ln = e1
        self.ex_m55 = e2
        self.cat = c

    def description_info(self): # функция для вывода информации о товаре
        n1 = ""
        n2 = ""
        if self.ex_ln == "Есть": n1 = "Есть в наличии"
        if self.ex_ln == "Нет": n1 = "Нет в наличии"
        if self.ex_m55 == "Есть": n2 = "Есть в наличии"
        if self.ex_m55 == "Нет": n2 = "Нет в наличии"

        s_description = f"<b>Название товара: </b>{self.name}\n\n<b>Описание: </b>{self.description}" + "\n\n<b>Стоимость: </b>" + str(self.price) + "\n\n<b>Наличие на Бульваре Любы Новоселовой, 18: </b>" + n1 + "\n<b>Наличие на Можайском Шоссе, 55: </b>" + n2
        return s_description


right_now_rek_test = []
binary_markup = ty.ReplyKeyboardMarkup()
binary_markup.add("Да", "Нет")
rek_passed_users = {}
che1 = False
new_good_info = []
global new_good_to_review
new_good_to_review = [""]
rev_check_markup_array = []
markup_admin_wishlists_array = []
markup_admin_delete_order_list = []
checker_for_restart1 = False
markup_for_a_menu_array = []
markup_to_del_good_menu_array = []
markup_to_red_good_menu_array = []
markup_put_smth_in_wishlist = []
additional_markup_put_etc = []
new_menu_markup_in_array = []
comment1 = ['здесь будет комментарий']
markup5 = ty.ReplyKeyboardMarkup(row_width=1)
m5b1 = ty.KeyboardButton("Одинцово, Бульвар Любы Новоселовой, 18")
m5b2 = ty.KeyboardButton("Одинцово, Можайское Шоссе, 55")
markup5.add(m5b1, m5b2)
just_lk_markup = ty.ReplyKeyboardMarkup(row_width=1)
just_lk_markup.add(ty.KeyboardButton("Вернуться в Личный Кабинет"))
recommend_users = [str(i[1]) for i in s.f]

def writeTofile(data, filename):  # запись BLOB в файл-изображение
    with open(filename, 'wb') as file:
        file.write(data)
    print("Data placed in: ", filename, "\n")

def check_username_wishlist(message):  # проверка того, есть ли user_id пользователя в таблице БД для виш-листов
    checker1 = False
    for i in s.w:
        if i[1] == message.from_user.id:
            checker1 = True
            break
    if checker1 == True:
        return True
    else:
        return False

def check_username_order(message):  # проверка того, есть ли у пользователя активный заказ
    checker1 = False
    for i in s.o:
        if i[1] == message.from_user.id:
            checker1 = True
            break
    if checker1 == True:
        return True
    else:
        return False

def search_username_wishlist(message):  # поиск номера строки в таблице БД для виш-листов по user_id пользователя
    for i in s.w:
        if i[1] == message.from_user.id:
            return s.w.index(i)

def search_good_line_in_menu(something):  # поиск номера строки в таблице БД для товаров по названию товара
    for i in s.d:
        if i[1] == something:
            return s.d.index(i)

def search_username_order(message):  # поиск номера строки в таблице БД для заказов по user_id пользователя
    for i in s.o:
        if i[1] == message.from_user.id: return s.o.index(i)

def search_for_last_free_db_space(message):  # поиск последней свободной ячейки в строке таблицы БД для виш-листов для конкретного пользователя
    the_checker = False
    what_to_find = 2
    for i in s.w[search_username_wishlist(message)]:
        if i == '':
            the_checker = True
            what_to_find = s.w[search_username_wishlist(message)].index(i)
    print(what_to_find)
    if the_checker == False:
        what_to_find = 2
    if what_to_find == 2: return 'good1'
    if what_to_find == 3: return 'good2'
    if what_to_find == 4: return 'good3'
    if what_to_find == 5: return 'good4'
    if what_to_find == 6: return 'good5'
    if what_to_find == 7: return 'good6'
    if what_to_find == 8: return 'good7'
    if what_to_find == 9: return 'good8'
    if what_to_find == 10: return 'good9'
    if what_to_find == 11: return 'good10'
    else: return 'good1'

def clear_wishlist(message):  # очистка виш-листа
    string_about_goods = 'good1'
    for i in range(2, 12):
        if i == 2: string_about_goods = 'good1'
        if i == 3: string_about_goods = 'good2'
        if i == 4: string_about_goods = 'good3'
        if i == 5: string_about_goods = 'good4'
        if i == 6: string_about_goods = 'good5'
        if i == 7: string_about_goods = 'good6'
        if i == 8: string_about_goods = 'good7'
        if i == 9: string_about_goods = 'good8'
        if i == 10: string_about_goods = 'good9'
        if i == 11: string_about_goods = 'good10'

        s.sql.execute(f"""UPDATE wishlist SET '{string_about_goods}' = '' WHERE username = '{message.from_user.id}'""")
        s.db.commit()

def comments_handler(message): # функиця, принимающая комментарии пользователя к заказу
    comment1.clear()
    comment1.append(message.text)
    bot.send_message(message.chat.id, "Выберите точку сети, в которой вам будет удобно забрать заказ", reply_markup=markup5)

def new_o(message): # название для нового товара
    s.a = (s.sql.execute("SELECT * FROM goods"))
    s.d = s.sql.fetchall()

    new_good_info.clear()
    new_good_info.append(s.d[-1][0] + 1)
    new_good_info.append(message.text)
    p2 = bot.send_message(message.chat.id, "Введите описание товара")
    bot.register_next_step_handler(p2, new_price)

def new_price(message): # описание для нового товара
    new_good_info.append(message.text)
    p3 = bot.send_message(message.chat.id, "Введите цену товара")
    bot.register_next_step_handler(p3, new_pic)

def new_pic(message): # цена для нового товара
    new_good_info.append(message.text)
    p_any = bot.send_message(message.chat.id, "Отправьте фото товара")
    bot.register_next_step_handler(p_any, new_ex1)

def new_ex1(message): # фото для нового товара
    new_good_info.append(photo_downloader(message))
    new_ex_mark = markup(["Есть", "Нет"])
    p4 = bot.send_message(message.chat.id, "Введите статус наличия товара по адресу Бульвар Любы Новоселовой, 18", reply_markup=new_ex_mark.m)
    bot.register_next_step_handler(p4, new_ex2)

def new_ex2(message): # наличие в точке 1 для нового товара
    new_good_info.append(message.text)
    new_ex_mark = markup(["Есть", "Нет"])
    p5 = bot.send_message(message.chat.id,
                          "Введите статус наличия товара по адресу Можайское Шоссе, 55", reply_markup=new_ex_mark.m)
    bot.register_next_step_handler(p5, before_fin)

def before_fin(message): # наличие в точке 2 для нового товара
    new_good_info.append(message.text)
    category_good_markup = ty.ReplyKeyboardMarkup()
    category_good_markup.add("Горячий напиток", "Холодный напиток", "Основное блюдо", "Десерт")
    p6 = bot.send_message(message.chat.id, "Выберите категорию товара:", reply_markup=category_good_markup)
    bot.register_next_step_handler(p6, fin)

def fin(message): # категория для нового товара и добавление в таблицу БД для товаров строки нового товара
    new_good_info.append(message.text)
    final_markup = markup(["Вернуться в Админ-Панель"])

    s.sql.execute(f"""INSERT INTO goods(id, good_name, good_description, good_price, good_photo, good_existence_ln, good_existance_m55, category) 
                                   VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", (new_good_info[0], new_good_info[1], new_good_info[2], new_good_info[3], new_good_info[4], new_good_info[5], new_good_info[6], new_good_info[7]))
    s.db.commit()

    bot.send_message(message.chat.id, "Товар успешно добавлен в меню!", reply_markup=final_markup.m)
    os.execv(sys.executable, [sys.executable] + sys.argv)

def red_good_name(message):  # новое название для изменяемого товара
    s.sql.execute(
        f"""UPDATE goods SET good_name = '{message.text}' WHERE good_name = '{good_red_name}'""")
    s.db.commit()
    markup_admin_1 = ty.ReplyKeyboardMarkup(row_width=1)
    admin_btn1 = ty.KeyboardButton("Редактировать меню")
    admin_btn2 = ty.KeyboardButton("Редактировать информацию о товарах")
    admin_btn3 = ty.KeyboardButton("Заказы виш-листов")
    admin_btn4 = ty.KeyboardButton("Отзывы")
    markup_admin_1.add(admin_btn1, admin_btn2, admin_btn3, admin_btn4, ty.KeyboardButton("Вернуться в Личный Кабинет"))

    bot.send_message(message.chat.id, 'Название изменено'.format(message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup_admin_1)

    os.execv(sys.executable, [sys.executable] + sys.argv)

def red_good_desc(message):  # новое описание для изменяемого товара
    s.sql.execute(
        f"""UPDATE goods SET good_description = '{message.text}' WHERE good_name = '{good_red_name}'""")
    s.db.commit()
    markup_admin_1 = ty.ReplyKeyboardMarkup(row_width=1)
    admin_btn1 = ty.KeyboardButton("Редактировать меню")
    admin_btn2 = ty.KeyboardButton("Редактировать информацию о товарах")
    admin_btn3 = ty.KeyboardButton("Заказы виш-листов")
    admin_btn4 = ty.KeyboardButton("Отзывы")
    markup_admin_1.add(admin_btn1, admin_btn2, admin_btn3, admin_btn4, ty.KeyboardButton("Вернуться в Личный Кабинет"))

    bot.send_message(message.chat.id, 'Описание изменено'.format(message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup_admin_1)

    os.execv(sys.executable, [sys.executable] + sys.argv)

def red_good_price(message):  # новая цена для изменяемого товара
    s.sql.execute(
        f"""UPDATE goods SET good_price = '{message.text}' WHERE good_name = '{good_red_name}'""")
    s.db.commit()
    markup_admin_1 = ty.ReplyKeyboardMarkup(row_width=1)
    admin_btn1 = ty.KeyboardButton("Редактировать меню")
    admin_btn2 = ty.KeyboardButton("Редактировать информацию о товарах")
    admin_btn3 = ty.KeyboardButton("Заказы виш-листов")
    admin_btn4 = ty.KeyboardButton("Отзывы")
    markup_admin_1.add(admin_btn1, admin_btn2, admin_btn3, admin_btn4, ty.KeyboardButton("Вернуться в Личный Кабинет"))

    bot.send_message(message.chat.id, 'Цена изменена'.format(message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup_admin_1)

    os.execv(sys.executable, [sys.executable] + sys.argv)

def red_good_ex1(message):  # новое наличие в точке 1 для изменяемого товара
    s.sql.execute(
        f"""UPDATE goods SET good_existence_ln = '{message.text}' WHERE good_name = '{good_red_name}'""")
    s.db.commit()
    markup_admin_1 = ty.ReplyKeyboardMarkup(row_width=1)
    admin_btn1 = ty.KeyboardButton("Редактировать меню")
    admin_btn2 = ty.KeyboardButton("Редактировать информацию о товарах")
    admin_btn3 = ty.KeyboardButton("Заказы виш-листов")
    admin_btn4 = ty.KeyboardButton("Отзывы")
    markup_admin_1.add(admin_btn1, admin_btn2, admin_btn3, admin_btn4, ty.KeyboardButton("Вернуться в Личный Кабинет"))

    bot.send_message(message.chat.id, 'Статус наличия товара изменен'.format(message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup_admin_1)

    os.execv(sys.executable, [sys.executable] + sys.argv)

def red_good_ex2(message):  # новое наличие в точке 2 для изменяемого товара
    s.sql.execute(
        f"""UPDATE goods SET good_existance_m55 = '{message.text}' WHERE good_name = '{good_red_name}'""")
    s.db.commit()
    markup_admin_1 = ty.ReplyKeyboardMarkup(row_width=1)
    admin_btn1 = ty.KeyboardButton("Редактировать меню")
    admin_btn2 = ty.KeyboardButton("Редактировать информацию о товарах")
    admin_btn3 = ty.KeyboardButton("Заказы виш-листов")
    admin_btn4 = ty.KeyboardButton("Отзывы")
    markup_admin_1.add(admin_btn1, admin_btn2, admin_btn3, admin_btn4, ty.KeyboardButton("Вернуться в Личный Кабинет"))

    bot.send_message(message.chat.id, 'Статус наличия товара изменен'.format(message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup_admin_1)

    os.execv(sys.executable, [sys.executable] + sys.argv)

def red_good_cat(message):  # новая категория для изменяемого товара
    s.sql.execute(
        f"""UPDATE goods SET category = '{message.text[12:]}' WHERE good_name = '{good_red_name}'""")
    s.db.commit()
    markup_admin_1 = ty.ReplyKeyboardMarkup(row_width=1)
    admin_btn1 = ty.KeyboardButton("Редактировать меню")
    admin_btn2 = ty.KeyboardButton("Редактировать информацию о товарах")
    admin_btn3 = ty.KeyboardButton("Заказы виш-листов")
    admin_btn4 = ty.KeyboardButton("Отзывы")
    markup_admin_1.add(admin_btn1, admin_btn2, admin_btn3, admin_btn4, ty.KeyboardButton("Вернуться в Личный Кабинет"))

    bot.send_message(message.chat.id, 'Категория товара изменена'.format(message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup_admin_1)

    os.execv(sys.executable, [sys.executable] + sys.argv)

def search_function1(message): # функция поиска товара по его названию
    markup_for_search_function1 = ty.ReplyKeyboardMarkup()
    markup_for_search_function1.add(ty.KeyboardButton("Вернуться в Меню"))
    message_formated = str(message.text[0].upper() + message.text[1:].lower())


    if message_formated in markup_for_a_menu_array:  # раздел товара
        markup_for_every_good = ty.ReplyKeyboardMarkup(row_width=1)
        markup_for_every_good.add(ty.KeyboardButton(f"Добавить {message_formated} в виш-лист"),
                                  ty.KeyboardButton(f"Написать отзыв про {message_formated}"),
                                  ty.KeyboardButton("Вернуться в Меню"),
                                  ty.KeyboardButton("Вернуться в Личный Кабинет"))

        if s.d[search_good_line_in_menu(message_formated)][4] != None:
            photoimage = s.d[search_good_line_in_menu(message_formated)][4]
            writeTofile(photoimage, 'pics/photoo_image.jpg')
            bot.send_photo(message.chat.id, open('pics/photoo_image.jpg', 'rb'))

        i_current = search_good_line_in_menu(message_formated)
        good_n = good(message_formated, s.d[i_current][2], s.d[i_current][3], s.d[i_current][5], s.d[i_current][6],
                      s.d[i_current][7])
        bot.send_message(message.chat.id, good_n.description_info(), reply_markup=markup_for_every_good,
                         parse_mode="html")
    else:
        bot.send_message(message.chat.id, "К сожалению, товара с таким названием в нашем меню нет. Но вы можете зайти в раздел меню и выбрать что-нибудь похожее :)", reply_markup=markup_for_search_function1)

def reply_to_review(message): # сохранение отзыва в БД
    s.sql.execute(f"""INSERT INTO reviews(id, good, text) 
                                       VALUES('{s.r[-1][0] + 1}', '{new_good_to_review[0]}', '{message.text}');""")
    s.db.commit()

    bot.send_message(message.chat.id, "Отзыв успешно отправлен! :)")
    os.execv(sys.executable, [sys.executable] + sys.argv)

def rek_step1(message):  # 1 вопрос опроса для рекомендаций
    polniy_markup = ty.ReplyKeyboardMarkup(row_width=1)
    polniy_markup.add("Полным приемом пищи", "Быстрым утолением голода")
    right_now_rek_test.clear()
    right_now_rek_test.append(message.text)

    rek2 = bot.send_message(message.chat.id,
                            "Следующий вопрос: Если вы решаете перекусить в кафе или кофейне, то этот перекус является полным приемом пищи или быстрым утолением голода?",
                            reply_markup=polniy_markup)
    bot.register_next_step_handler(rek2, rek_step2)

def rek_step2(message):  # 2 вопрос опроса для рекомендаций
    right_now_rek_test.append(message.text)
    rek3 = bot.send_message(message.chat.id, "Третий вопрос: Вы любите сладкое?", reply_markup=binary_markup)
    bot.register_next_step_handler(rek3, rek_step3)

def rek_step3(message):  # 3 вопрос опроса для рекомендаций
    right_now_rek_test.append(message.text)
    rek4 = bot.send_message(message.chat.id, "И последний вопрос: Любите ли вы кофе?", reply_markup=binary_markup)
    bot.register_next_step_handler(rek4, rek_step_last)

def rek_step_last(message):  # последний вопрос опроса для рекомендаций
    right_now_rek_test.append(message.text)

    rek_pre_insertion = [0]*4
    if right_now_rek_test[0] == "Да": rek_pre_insertion[0] = 1
    else: rek_pre_insertion[0] = 0

    if right_now_rek_test[1] == "Полным приемом пищи": rek_pre_insertion[1] = 1
    else: rek_pre_insertion[1] = 0

    if right_now_rek_test[2] == "Да": rek_pre_insertion[2] = 1
    else: rek_pre_insertion[2] = 0

    if right_now_rek_test[3] == "Да": rek_pre_insertion[3] = 1
    else: rek_pre_insertion[3] = 0

    s.sql.execute(f"""INSERT INTO recommend(id, username, healthy, full, sweet, coffee) 
                                           VALUES('{s.f[-1][0] + 1}', '{message.from_user.id}', '{rek_pre_insertion[0]}', '{rek_pre_insertion[1]}', '{rek_pre_insertion[2]}', '{rek_pre_insertion[3]}');""")
    s.db.commit()

    only_rek_markup = ty.ReplyKeyboardMarkup()
    only_rek_markup.add("Рекомендации")
    bot.send_message(message.chat.id, "Предлагаю зайти в рекомендации, чтобы посмотреть, какие товары для вас подобрали мои алгоритмы! :)", reply_markup=only_rek_markup)
    os.execv(sys.executable, [sys.executable] + sys.argv)

def search_for_username_in_rek(message): # поиск строки в таблице БД для рекомендаций по user_id пользователя
    for i in range(len(s.f)):
        if str(s.f[i][1]) == str(message.from_user.id):
            return i


def photo_downloader(message): # функция для скачивания присылаемых пользователем фотографий и возврата их BLOB-формата
    f_id = message.photo[2].file_id
    file_got = bot.get_file(f_id)
    the_file = bot.download_file(file_got.file_path)
    writeTofile(the_file, 'pics/the_new_good_photo.jpg')
    return the_file

def red_good_photo(message): # новое фото для изменяемого товара
    the_ph = photo_downloader(message)

    j_current = search_good_line_in_menu(good_red_name)

    s.sql.execute(f"""INSERT INTO goods(id, good_name, good_description, good_price, good_photo, good_existence_ln, good_existance_m55, category) 
                                       VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", (max([i[0] for i in s.d]) + 1, s.d[j_current][1], s.d[j_current][2], s.d[j_current][3], the_ph, s.d[j_current][5],
    s.d[j_current][6], s.d[j_current][7]))

    s.sql.execute(f"""DELETE FROM goods WHERE id = '{s.d[j_current][0]}';""")
    s.db.commit()

    markup_admin_1 = ty.ReplyKeyboardMarkup(row_width=1)
    admin_btn1 = ty.KeyboardButton("Редактировать меню")
    admin_btn2 = ty.KeyboardButton("Редактировать информацию о товарах")
    admin_btn3 = ty.KeyboardButton("Заказы виш-листов")
    admin_btn4 = ty.KeyboardButton("Отзывы")
    markup_admin_1.add(admin_btn1, admin_btn2, admin_btn3, admin_btn4, ty.KeyboardButton("Вернуться в Личный Кабинет"))

    bot.send_message(message.chat.id, 'Фотография изменена'.format(message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup_admin_1)

    os.execv(sys.executable, [sys.executable] + sys.argv)

def sum_price(array_of_goods_ordered): # функция для подсчета итоговой суммы заказа для администратора
    summary = 0
    for i in array_of_goods_ordered:
        if str(i) == "" or str(i) == " ": continue
        if '/' in str(s.d[search_good_line_in_menu(i)][3]):
            return int(0)
    for i in array_of_goods_ordered:
        if str(i) == "" or str(i) == " ": continue
        summary += int(s.d[search_good_line_in_menu(i)][3])
    return summary

def good_name_by_id(id1): # поиск названия товара по его id в таблице БД для товаров
    for i in s.d:
        if str(i[0]) == str(id1): return i[1]
    return 0


@bot.message_handler(commands=['start'])
def start_message(a):  # реакиця на команду start
    markup1 = ty.ReplyKeyboardMarkup(row_width=3)
    menu1 = ty.KeyboardButton("Меню")
    menu2 = ty.KeyboardButton("Точки")
    menu3 = ty.KeyboardButton("Виш-лист")
    menu4 = ty.KeyboardButton("Акции")
    menu5 = ty.KeyboardButton("Рекомендации")
    markup1.add(menu1, menu2, menu3, menu4, menu5)
    bot.send_message(a.chat.id, 'Привет, {0.first_name}! Я - телеграм-бот сети кофеен <b>The Buffet</b>. Добро пожаловать в чат со мной. Надеюсь, я буду полезен :)\n\nСейчас Вы находитесь в Личном Кабинете. Здесь по кнопкам навигации, расположенным внизу экрана, можно выбрать один из разделов. В них можно посмотреть меню, увидеть свой виш-лист, почитать про наши кофейни и сделать многое другое'.format(a.from_user, bot.get_me()), parse_mode="html", reply_markup=markup1) # второй аргумент - то, что отправляет бот.

@bot.message_handler(commands=['admin'])
def admin_panel(m): # реакция на команду admin
    bot.send_message(m.chat.id, "Введите пароль администратора:".format(m.from_user, bot.get_me()))
    markup_admin_wishlists = ty.ReplyKeyboardMarkup(row_width=1)
    for i in range(len(list(s.o))):
        markup_admin_wishlists.add(ty.KeyboardButton(f"Заказ №{s.o[i][0]} - {s.o[i][12]}"))
    markup_admin_wishlists.add(ty.KeyboardButton("Вернуться в Админ-Панель"))



@bot.message_handler(content_types=['text'])
def reply_to_text(message): # реакция на любой текст, присылаемый пользователем
    global che1
    markup2 = ty.ReplyKeyboardMarkup(row_width=1)
    wishlist_string_id = 3

    markup2.add(ty.KeyboardButton("Поиск по названию товара"))
    markup2.add(ty.KeyboardButton("Фильтр"))
    markup2.add(ty.KeyboardButton("Сортировка"))
    for i in s.d:
        markup_for_a_menu_array.append(ty.KeyboardButton(f"{str(i[1])}").text)
        markup2.add(ty.KeyboardButton(str(i[1])))
        markup_put_smth_in_wishlist.append(ty.KeyboardButton(f"Добавить {str(i[1])} в виш-лист").text)
    markup2.add(ty.KeyboardButton("Вернуться в Личный Кабинет"))
    address = [message.from_user.id, '']

    if message.chat.type == 'private':
        if message.text == "Получить номер заказа": # подтверждение заказа
            p_markup = ty.ReplyKeyboardMarkup()
            p_markup.add("Вернуться в Личный Кабинет")
            bot.send_message(message.chat.id,
                             f"Номер вашего заказа - {s.o[search_username_order(message)][0]}! Администратор вскоре его рассмотрит и приготовит :)", reply_markup=p_markup)
        if message.text == "Меню" or message.text == "Вернуться в Меню": # раздел меню
            s.a = (s.sql.execute("SELECT * FROM goods ORDER BY good_name"))
            s.d = s.sql.fetchall()

            new_menu_markup = ty.InlineKeyboardMarkup(row_width=2)
            new_everything_else_in_menu_markup = markup(
                ["Поиск по названию товара", "Фильтр", "Сортировка", "Вернуться в Личный Кабинет"])
            for i in s.d:
                new_menu_markup.add(ty.InlineKeyboardButton(str(i[1]), callback_data=str(i[0])))
                new_menu_markup_in_array.append(str(i[0]))

            bot.send_message(message.chat.id, "Вот меню нашей сети:", reply_markup=new_menu_markup)
            bot.send_message(message.chat.id,
                             "Вы также можете настроить список товаров или найти конкретный товар с помощью кнопок в нижней части экрана :)",
                             reply_markup=new_everything_else_in_menu_markup.m)

            wishlist_string_id += 1
            if check_username_wishlist(message) == False:
                s.sql.execute(f"""INSERT INTO wishlist(id, username, good1, good2, good3, good4, good5, good6, good7, good8, good9, good10) 
                               VALUES('{s.w[-1][0] + 1}', '{message.from_user.id}', '', '', '', '', '', '', '', '', '', '');""")
                s.db.commit()
                os.execv(sys.executable, [sys.executable] + sys.argv)

        elif message.text == "Рекомендации": # раздел рекомендаций
            recommend_users = [str(i[1]) for i in s.f]
            if str(message.from_user.id) not in recommend_users:
                rek_markup1 = markup(["Я за!", "Вернуться в Личный Кабинет"])
                bot.send_message(message.chat.id, "Вы зашли в рекомендации впервые, поэтому предлагаем вам пройти опрос, результаты которого помогут вам выбрать товар, который вам подойдет. Что думаете? :)", reply_markup=rek_markup1.m)
            else:
                healthy, full, sweet, coffee = [], [], [], []

                if s.f[search_for_username_in_rek(message)][2] == 1:
                    healthy.append('Вода "Аква-Минерале"')
                    healthy.append('Творожная запеканка')
                    healthy.append('Сок Rich')

                if s.f[search_for_username_in_rek(message)][3] == 1:
                    full.append('Бургер Chicken')
                    full.append('Сэндвич с ветчиной')
                else:
                    full.append('Орешки')
                    full.append('Бутербродик')
                    full.append('Пирожное')

                if s.f[search_for_username_in_rek(message)][4] == 1:
                    sweet.append('Орешки в шоколаде')
                    sweet.append('Маффин с голубикой')
                    sweet.append('Картошка')
                    sweet.append('Кейк-попс')
                    sweet.append('Шоколадная колбаска')
                    sweet.append('Сливочно-арахисовая колбаска')
                    sweet.append('Шоколадная шарлотка')
                    sweet.append('Французская меренга')

                if s.f[search_for_username_in_rek(message)][5] == 1:
                    coffee.append('Эспрессо')
                    coffee.append('Американо')
                    coffee.append('Капучино s')
                    coffee.append('Капучино m')
                    coffee.append('Капучино l')
                    coffee.append('Латте s')
                    coffee.append('Латте m')
                    coffee.append('Латте l')
                    coffee.append('Флэт Уайт')
                    coffee.append('Раф')

                res_rek = healthy + full + sweet + coffee
                res_rek_markup = ty.InlineKeyboardMarkup()
                for i in res_rek: res_rek_markup.add(ty.InlineKeyboardButton(str(i), callback_data=str(s.d[search_good_line_in_menu(i)][0])))

                bot.send_message(message.chat.id, "Вот товары, которые мои алгоритмы подобрали специально для вас :)", reply_markup=res_rek_markup)
                bot.send_message(message.chat.id, "Если вы хотите вернуться в меню, нажмите кнопку в нижней части экрана", reply_markup=just_lk_markup)



        elif message.text == "Я за!": # начало опроса для рекомендаций
            rek1 = bot.send_message(message.chat.id,
                                    "Первый вопрос: Вы стараетесь всегда придерживаться здорового образа жизни и питаться максимально правильно?",
                                    reply_markup=binary_markup)
            bot.register_next_step_handler(rek1, rek_step1)



        elif message.text[:18] == "Написать отзыв про": # написание отзыва о товаре
            text_of_review = bot.send_message(message.chat.id, "Напишите ваш отзыв и отправьте его мне :)")
            new_good_to_review[0] = message.text[19:]
            bot.register_next_step_handler(text_of_review, reply_to_review)

        elif message.text == "Поиск по названию товара":  # начало поиска по названию товара
            search_p1 = bot.send_message(message.chat.id, "Введите название товара, который вы хотите найти")
            bot.register_next_step_handler(search_p1, search_function1)

        elif message.text == "Сортировка": # выбор вариантов сортировки в меню
            sort_markup = markup(["В алфавитном порядке", "По убыванию цены", "По возрастанию цены", "Вернуться в Меню"])
            bot.send_message(message.chat.id, "Как вы хотите отсортировать меню?", reply_markup=sort_markup.m)

        elif message.text == "Фильтр": # выбор вариантов фильтрации в меню
            fltr_markup = markup(["Горячие напитки", "Холодные напитки", "Основные блюда", "Десерты", "Вернуться в Меню"])
            bot.send_message(message.chat.id, "Выберите категорию товаров, которую вы хотели бы увидеть :)", reply_markup=fltr_markup.m)

        elif message.text == "Горячие напитки": # отфильтрованное меню из горячих напитков
            menu_markup_f1 = ty.InlineKeyboardMarkup()
            for i in s.d:
                if str(i[7]) == "Горячий напиток": menu_markup_f1.add(ty.InlineKeyboardButton(str(i[1]), callback_data=str(i[0])))
            bot.send_message(message.chat.id, "Вот отфильтрованное по вашим параметрам меню :)", reply_markup=menu_markup_f1)

        elif message.text == "Холодные напитки": # отфильтрованное меню из холодных напитков
            menu_markup_f1 = ty.InlineKeyboardMarkup()
            for i in s.d:
                if str(i[7]) == "Холодный напиток": menu_markup_f1.add(
                    ty.InlineKeyboardButton(str(i[1]), callback_data=str(i[0])))
            bot.send_message(message.chat.id, "Вот отфильтрованное по вашим параметрам меню :)",
                             reply_markup=menu_markup_f1)

        elif message.text == "Основные блюда": # отфильтрованное меню из основных блюд
            menu_markup_f1 = ty.InlineKeyboardMarkup()
            for i in s.d:
                if str(i[7]) == "Основное блюдо": menu_markup_f1.add(
                    ty.InlineKeyboardButton(str(i[1]), callback_data=str(i[0])))
            bot.send_message(message.chat.id, "Вот отфильтрованное по вашим параметрам меню :)",
                             reply_markup=menu_markup_f1)

        elif message.text == "Десерты": # отфильтрованное меню из десертов
            menu_markup_f1 = ty.InlineKeyboardMarkup()
            for i in s.d:
                if str(i[7]) == "Десерт": menu_markup_f1.add(
                    ty.InlineKeyboardButton(str(i[1]), callback_data=str(i[0])))
            bot.send_message(message.chat.id, "Вот отфильтрованное по вашим параметрам меню :)",
                             reply_markup=menu_markup_f1)

        elif message.text == "В алфавитном порядке": # отсортированное в алфавитном порядке меню
            s.a = (s.sql.execute("SELECT * FROM goods ORDER BY good_name"))
            s.d = s.sql.fetchall()
            new_menu_markup = ty.InlineKeyboardMarkup(row_width=2)
            new_everything_else_in_menu_markup = markup(
                ["Поиск по названию товара", "Фильтр", "Сортировка", "Вернуться в Личный Кабинет"])
            for i in s.d:
                new_menu_markup.add(ty.InlineKeyboardButton(str(i[1]), callback_data=str(i[0])))
                new_menu_markup_in_array.append(str(i[0]))

            bot.send_message(message.chat.id, "Вот отсортированное по вашим параметрам меню:", reply_markup=new_menu_markup)
            bot.send_message(message.chat.id,
                             "Вы также можете настроить список товаров или найти конкретный товар с помощью кнопок в нижней части экрана :)",
                             reply_markup=new_everything_else_in_menu_markup.m)


        elif message.text == "По убыванию цены": # отсортированное по убыванию цены меню
            s.a = (s.sql.execute("SELECT * FROM goods ORDER BY good_price DESC"))
            s.d = s.sql.fetchall()
            new_menu_markup = ty.InlineKeyboardMarkup(row_width=2)
            new_everything_else_in_menu_markup = markup(
                ["Поиск по названию товара", "Фильтр", "Сортировка", "Вернуться в Личный Кабинет"])
            for i in s.d:
                new_menu_markup.add(ty.InlineKeyboardButton(str(i[1]), callback_data=str(i[0])))
                new_menu_markup_in_array.append(str(i[0]))

            bot.send_message(message.chat.id, "Вот отсортированное по вашим параметрам меню:",
                             reply_markup=new_menu_markup)
            bot.send_message(message.chat.id,
                             "Вы также можете настроить список товаров или найти конкретный товар с помощью кнопок в нижней части экрана :)",
                             reply_markup=new_everything_else_in_menu_markup.m)

        elif message.text == "По возрастанию цены": # отсортированное по возрастанию цены меню
            s.a = (s.sql.execute("SELECT * FROM goods ORDER BY good_price ASC"))
            s.d = s.sql.fetchall()
            new_menu_markup = ty.InlineKeyboardMarkup(row_width=2)
            new_everything_else_in_menu_markup = markup(
                ["Поиск по названию товара", "Фильтр", "Сортировка", "Вернуться в Личный Кабинет"])
            for i in s.d:
                new_menu_markup.add(ty.InlineKeyboardButton(str(i[1]), callback_data=str(i[0])))
                new_menu_markup_in_array.append(str(i[0]))

            bot.send_message(message.chat.id, "Вот отсортированное по вашим параметрам меню:",
                             reply_markup=new_menu_markup)
            bot.send_message(message.chat.id,
                             "Вы также можете настроить список товаров или найти конкретный товар с помощью кнопок в нижней части экрана :)",
                             reply_markup=new_everything_else_in_menu_markup.m)

        elif message.text == "Вернуться в Личный Кабинет": # возвращение в личный кабинет
            markup1 = ty.ReplyKeyboardMarkup(row_width=3)
            menu1 = ty.KeyboardButton("Меню")
            menu2 = ty.KeyboardButton("Точки")
            menu3 = ty.KeyboardButton("Виш-лист")
            menu4 = ty.KeyboardButton("Акции")
            menu5 = ty.KeyboardButton("Рекомендации")
            markup1.add(menu1, menu2, menu3, menu4, menu5)
            bot.send_message(message.chat.id, "Вы зашли в Личный Кабинет. Здесь по кнопкам навигации, расположенным внизу экрана, можно выбрать один из разделов. В них можно посмотреть меню, увидеть свой виш-лист, почитать про наши кофейни и сделать многое другое", parse_mode="html", reply_markup=markup1)
        elif message.text == "Точки": # раздел точек сети
            point_info_m = markup(["Одинцово, Бульвар Любы Новоселовой, 18 - Информация", "Одинцово, Можайское Шоссе, 55 - Информация", "Вернуться в Личный Кабинет"])
            bot.send_message(message.chat.id, "Выберите точку :)".format(message.from_user, bot.get_me()), parse_mode="html", reply_markup=point_info_m.m)
        elif message.text == "Одинцово, Бульвар Любы Новоселовой, 18 - Информация": # информация о точке 1
            luba = cafe("Одинцово, Бульвар Любы Новоселовой, 18", "Эта точка - первая точка сети, которая была открыта в городе Одинцово в 2019 году. Именно там в невероятно уютной атмосфере, наслаждаясь чашечкой кофе, вы можете провести очень приятные несколько минут или часов :) \n \n<b>Время работы:</b> \n08:00-21:00 \n \n<b>Контакты:</b> \nНомер телефона: 8 (916) 429-55-22",
                        open("pics/luba loc.jpg", "rb"), open("pics/luba ph.jpeg", "rb"))
            bot.send_photo(message.chat.id, luba.location)
            bot.send_photo(message.chat.id, luba.photo)
            bot.send_message(message.chat.id, luba.description, parse_mode="html", reply_markup=just_lk_markup)
        elif message.text == "Одинцово, Можайское Шоссе, 55 - Информация": # информация о точке 2
            m55 = cafe("Одинцово, Можайское Шоссе, 55", "Эта точка - вторая из точек сети, которая так же, как и первая, была открыта в Одинцово. Она располагается внутри медицинского центра, поэтому там вы можете не только перекусить и выпить кофе, но и подумать о своем здоровье :) \n \n<b>Время работы:</b> \n08:00-21:00 \n \n<b>Контакты:</b> \nНомер телефона: 8 (916) 429-55-22",
                       open("pics/m55 loc.jpg", "rb"), open("pics/m55 ph.jpeg", "rb"))
            bot.send_photo(message.chat.id, m55.location)
            bot.send_photo(message.chat.id, m55.photo)
            bot.send_message(message.chat.id, m55.description, parse_mode="html", reply_markup=just_lk_markup)

        elif message.text == "Акции": # раздел акций и купонов
            kupon_markup = markup(['Купон "Завтрак": Эспрессо + Творожная запеканка', 'Купон №2: Какао + Шоколадная шарлотка', 'Вернуться в Личный Кабинет'])
            bot.send_message(message.chat.id, "Выберите нужный купон :)".format(message.from_user, bot.get_me()), parse_mode="html", reply_markup=kupon_markup.m)

        elif message.text == 'Купон "Завтрак": Эспрессо + Творожная запеканка': # информация о купоне 1
            bot.send_photo(message.chat.id, open('pics/Купон - "Завтрак".png', 'rb'))

        elif message.text == 'Купон №2: Какао + Шоколадная шарлотка': # информация о купоне 2
            bot.send_photo(message.chat.id, open('pics/Купон 2.png', 'rb'))


        elif message.text == 'Виш-лист': # раздел виш-листа (списка "избранное")
            markup4 = markup(["Очистить виш-лист", "Сделать заказ виш-листа", "Вернуться в Личный Кабинет"])
            wishlist_in_string = ''
            just_menu_markup = markup(["Меню", "Вернуться в Личный Кабинет"])
            for i in s.w[search_username_wishlist(message)][2:]:
                if i == '' or i == ' ': continue
                wishlist_in_string += str(i)
                wishlist_in_string += '\n'
            if wishlist_in_string == '' or wishlist_in_string == ' ':
                bot.send_message(message.chat.id, 'Ваш виш-лист пуст :(\nЕсли хотите это исправить, зайдите в раздел "Меню" и выберите товар, который вам по душе!', reply_markup=just_menu_markup.m)
            bot.send_message(message.chat.id, wishlist_in_string, reply_markup=markup4.m)

        elif message.text in markup_put_smth_in_wishlist: # добавление товара в виш-лист
            s.sql.execute(
                f"""UPDATE wishlist SET {search_for_last_free_db_space(message)} = '{message.text[9:-11]}' WHERE username = '{message.from_user.id}'""")
            s.db.commit()
            bot.send_message(message.chat.id, "Готово!")
            os.execv(sys.executable, [sys.executable] + sys.argv)

        elif message.text == "Очистить виш-лист": # начало процесса очистки виш-листа
            clear_wishlist(message)
            bot.send_message(message.chat.id, "Виш-лист очищен :)", reply_markup=just_lk_markup)
            os.execv(sys.executable, [sys.executable] + sys.argv)
        elif message.text == "Сделать заказ виш-листа": # начало заказа виш-листа
            if check_username_order(message) == False:
                s.order_string_id += 1
                peremennaya = bot.send_message(message.chat.id, "Есть ли у вас дополнительные комментарии к заказу?")
                bot.register_next_step_handler(peremennaya, comments_handler)
            else: bot.send_message(message.chat.id, "Вы уже сделали заказ! Пожалуйста, подождите, пока он будет готов, и тогда вы сможете сделать следующий :)")
        elif message.text == "Одинцово, Бульвар Любы Новоселовой, 18" or message.text == "Одинцово, Можайское Шоссе, 55": # обработка выбранной точки выдачи и получения заказа и оформление заказа
            for i in [s.w[search_username_wishlist(message)][2], s.w[search_username_wishlist(message)][3],
                      s.w[search_username_wishlist(message)][4], s.w[search_username_wishlist(message)][5],
                      s.w[search_username_wishlist(message)][6], s.w[search_username_wishlist(message)][7],
                      s.w[search_username_wishlist(message)][8], s.w[search_username_wishlist(message)][9],
                      s.w[search_username_wishlist(message)][10], s.w[search_username_wishlist(message)][11]]:
                if i == "": break
                if message.text == "Одинцово, Бульвар Любы Новоселовой, 18" and s.d[search_good_line_in_menu(i)][5] == 0:
                    wrong_point = ty.ReplyKeyboardMarkup()
                    wrong_point.add(ty.KeyboardButton("Вернуться в Личный Кабинет"), ty.KeyboardButton("Одинцово, Можайское Шоссе, 55"))
                    bot.send_message(message.chat.id, "К сожалению, один из товаров в вашем виш-листе в данный момент недоступен для покупки в выбранной вами точке. Пожалуйста, выберите другую точку или вернитесь в личный кабинет, чтобы скорректировать ваш виш-лист :)", reply_markup=wrong_point)
                    che1 = True
                    break
                if message.text == "Одинцово, Можайское Шоссе, 55" and s.d[search_good_line_in_menu(i)][6] == 0:
                    che1 = True
                    wrong_point = ty.ReplyKeyboardMarkup()
                    wrong_point.add(ty.KeyboardButton("Вернуться в Личный Кабинет"), ty.KeyboardButton("Одинцово, Бульвар Любы Новоселовой, 18"))
                    bot.send_message(message.chat.id, "К сожалению, один из товаров в вашем виш-листе в данный момент недоступен для покупки в выбранной вами точке. Пожалуйста, выберите другую точку или вернитесь в личный кабинет, чтобы скорректировать ваш виш-лист :)", reply_markup=wrong_point)
                    break
                if message.text == "Одинцово, Бульвар Любы Новоселовой, 18" and s.d[search_good_line_in_menu(i)][5] == 0:
                    che1 = True
                    wrong_point = ty.ReplyKeyboardMarkup()
                    wrong_point.add(ty.KeyboardButton("Вернуться в Личный Кабинет"),
                                        ty.KeyboardButton("Одинцово, Можайское Шоссе, 55"))
                    bot.send_message(message.chat.id, "К сожалению, один из товаров в вашем виш-листе в данный момент недоступен для покупки в выбранной вами точке. Пожалуйста, выберите другую точку или вернитесь в личный кабинет, чтобы скорректировать ваш виш-лист :)", reply_markup=wrong_point)
                    break
                if message.text == "Одинцово, Можайское Шоссе, 55" and s.d[search_good_line_in_menu(i)][6] == 1 and che1 == True:
                    che1 = False
                    break
                if message.text == "Одинцово, Бульвар Любы Новоселовой, 18" and s.d[search_good_line_in_menu(i)][5] == 1 and che1 == True:
                    che1 = False
                    break

            if not che1:
                g_1 = s.w[search_username_wishlist(message)][2]
                g_2 = s.w[search_username_wishlist(message)][3]
                g_3 = s.w[search_username_wishlist(message)][4]
                g_4 = s.w[search_username_wishlist(message)][5]
                g_5 = s.w[search_username_wishlist(message)][6]
                g_6 = s.w[search_username_wishlist(message)][7]
                g_7 = s.w[search_username_wishlist(message)][8]
                g_8 = s.w[search_username_wishlist(message)][9]
                g_9 = s.w[search_username_wishlist(message)][10]
                g_10 = s.w[search_username_wishlist(message)][11]
                address[1] = message.text
                s.sql.execute(
                    f"""UPDATE order_string_id SET only = '{s.order_string_id}' WHERE only = '{s.order_string_id - 1}'""")
                s.sql.execute(f"""INSERT INTO orders(id, username, good1, good2, good3, good4, good5, good6, good7, good8, good9, good10, real_name, surplus, cafe_adress) 
                                               VALUES('{str(s.order_string_id)}', '{message.from_user.id}', '{g_1}', '{g_2}', '{g_3}', '{g_4}', '{g_5}', '{g_6}', '{g_7}', '{g_8}', '{g_9}', '{g_10}', '{message.from_user.full_name}', '{str(comment1[0])}', '{address[1]}');""")
                s.db.commit()

                number_of_order_markup = markup(["Получить номер заказа"])
                bot.send_message(message.chat.id, 'Заказ сделан! Чтобы получить номер заказа, нажмите на кнопку в нижней части экрана', reply_markup=number_of_order_markup.m)

                os.execv(sys.executable, [sys.executable] + sys.argv)

        elif message.text == "Редактировать меню": # выбор способа изменения меню
            red_menu_m = ty.ReplyKeyboardMarkup()
            red_menu_m.add(ty.KeyboardButton("Удалить один из существующих товаров"), ty.KeyboardButton("Добавить новый товар"), ty.KeyboardButton("Вернуться в Админ-Панель"))
            bot.send_message(message.chat.id, "Как конкретно вы хотите изменить меню?", reply_markup=red_menu_m)

        elif message.text == "Удалить один из существующих товаров": # выбор товара для удаления
            markup_del_from_menu = ty.InlineKeyboardMarkup()
            just_to_admin_panel_markup = markup(["Вернуться в Админ-Панель"])
            for i in s.d:
                markup_del_from_menu.add(ty.InlineKeyboardButton(("Удалить " + str(i[1])), callback_data=str("del" + str(i[0]))))
                markup_to_del_good_menu_array.append(str("del" + str(i[0])))

            bot.send_message(message.chat.id, "Выберите товар, который необходимо удалить из меню: ".format(message.from_user, bot.get_me()), reply_markup=markup_del_from_menu)
            bot.send_message(message.chat.id, "Если хотите вернуться в админ-панель, нажмите кнопку в нижней части экрана", reply_markup=just_to_admin_panel_markup.m)

        elif message.text == "Добавить новый товар": # начало добавления нового товара в меню
            p1 = bot.send_message(message.chat.id, "Введите название товара")
            bot.register_next_step_handler(p1, new_o)

        elif message.text == "Редактировать информацию о товарах":  # выбор товара, информацию о котором необходимо изменить
            markup_red_in_menu = ty.InlineKeyboardMarkup()
            just_to_admin_panel_markup = markup(["Вернуться в Админ-Панель"])
            for i in s.d:
                markup_red_in_menu.add(ty.InlineKeyboardButton(("Редактировать " + str(i[1])), callback_data=str("red" + str(i[0]))))
                markup_to_red_good_menu_array.append(str("red" + str(i[0])))
            bot.send_message(message.chat.id,
                             "Выберите товар, информацию о котором необходимо изменить: ".format(message.from_user,
                                                                                           bot.get_me()), reply_markup=markup_red_in_menu)
            bot.send_message(message.chat.id,
                             "Если хотите вернуться в админ-панель, нажмите кнопку в нижней части экрана",
                             reply_markup=just_to_admin_panel_markup.m)

        elif message.text == "Изменить фотографию":  # начало изменения фотографии товара
            r12 = bot.send_message(message.chat.id, "Отправьте новую фотографию товара :)")
            bot.register_next_step_handler(r12, red_good_photo)

        elif message.text == "Изменить категорию товара":  # начало изменения категории товара
            category_good_markup1 = ty.ReplyKeyboardMarkup()
            category_good_markup1.add("Изменить на Горячий напиток", "Изменить на Холодный напиток", "Изменить на Основное блюдо", "Изменить на Десерт")
            r10 = bot.send_message(message.chat.id, "Выберите категорию товара:", reply_markup=category_good_markup1)
            bot.register_next_step_handler(r10, red_good_cat)

        elif message.text == "Изменить название":  # начало изменения названия товара
            r1 = bot.send_message(message.chat.id, "Введите новое название товара")
            bot.register_next_step_handler(r1, red_good_name)

        elif message.text == "Изменить описание":  # начало изменения описания товара
            r2 = bot.send_message(message.chat.id, "Введите новое описание товара")
            bot.register_next_step_handler(r2, red_good_desc)

        elif message.text == "Изменить цену":  # начало изменения цены товара
            r3 = bot.send_message(message.chat.id, "Введите новую цену товара")
            bot.register_next_step_handler(r3, red_good_price)

        elif message.text == "Изменить статус наличия по адресу Бульвар Любы Новоселовой, 18":  # начало изменения статуса наличия товара в точке 1
            r4 = bot.send_message(message.chat.id, "Введите новый статус наличия товара по адресу Бульвар Любы Новоселовой, 18")
            bot.register_next_step_handler(r4, red_good_ex1)

        elif message.text == "Изменить статус наличия по адресу Можайское Шоссе, 55":  # начало изменения статуса наличия товара в точке 2
            r5 = bot.send_message(message.chat.id, "Введите новый статус наличия товара по адресу Можайское Шоссе, 55")
            bot.register_next_step_handler(r5, red_good_ex2)

        elif (message.text == "Завершить редактирование информации о товаре" or message.text == "Вернуться в Админ-Панель") and message.from_user.username in admin_list:  # возврат в админ-панель
            markup_admin_1 = ty.ReplyKeyboardMarkup(row_width=1)
            admin_btn1 = ty.KeyboardButton("Редактировать меню")
            admin_btn2 = ty.KeyboardButton("Редактировать информацию о товарах")
            admin_btn3 = ty.KeyboardButton("Заказы виш-листов")
            admin_btn4 = ty.KeyboardButton("Отзывы")
            markup_admin_1.add(admin_btn1, admin_btn2, admin_btn3, admin_btn4, ty.KeyboardButton("Вернуться в Личный Кабинет"))

            bot.send_message(message.chat.id, 'Хорошо, снова открываю админ-панель'.format(message.from_user, bot.get_me()),
                             parse_mode="html", reply_markup=markup_admin_1)

            os.execv(sys.executable, [sys.executable] + sys.argv)


        elif message.text == "1234567890" and message.from_user.username in admin_list:  # вход в админ-панель по паролю и проверке username пользователя (администратора)
            markup_admin_1 = ty.ReplyKeyboardMarkup(row_width=1)
            admin_btn1 = ty.KeyboardButton("Редактировать меню")
            admin_btn2 = ty.KeyboardButton("Редактировать информацию о товарах")
            admin_btn3 = ty.KeyboardButton("Заказы виш-листов")
            admin_btn4 = ty.KeyboardButton("Отзывы")
            markup_admin_1.add(admin_btn1, admin_btn2, admin_btn3, admin_btn4, ty.KeyboardButton("Вернуться в Личный Кабинет"))


            bot.send_message(message.chat.id, 'Добро пожаловать в админ-панель, <i>{0.first_name}</i>! :)'.format(message.from_user, bot.get_me()), parse_mode="html", reply_markup=markup_admin_1)

        elif message.text == "Отзывы" and message.from_user.username in admin_list:  # просмотр списка отзывов
            rev_check_markup = ty.ReplyKeyboardMarkup(row_width=1)
            for i in s.r:
                rev_check_markup.add(f"Отзыв №{i[0]}")
                rev_check_markup_array.append(f"Отзыв №{i[0]}")
            rev_check_markup.add("Вернуться в Админ-Панель")
            bot.send_message(message.chat.id, "Вот все отправленные на данный момент отзывы пользователей :)", reply_markup=rev_check_markup)
        elif message.text in rev_check_markup_array:  # просмотр выбранного отзыва
            index_of_review = int(message.text[7:])
            bot.send_message(message.chat.id, f"<b>Название товара:</b> {s.r[index_of_review-1][1]}\n\n<b>Текст отзыва:</b> {s.r[index_of_review-1][2]}", parse_mode="html")
        elif message.text == "Заказы виш-листов" and message.from_user.username in admin_list:  # просмотр списка заказов виш-листов
            markup_admin_wishlists = ty.ReplyKeyboardMarkup(row_width=1)
            for i in range(len(list(s.o))):
                markup_admin_wishlists.add(ty.KeyboardButton(f"Заказ №{s.o[i][0]} - {s.o[i][12]}"))
                markup_admin_wishlists_array.append(ty.KeyboardButton(f"Заказ №{s.o[i][0]} - {s.o[i][12]}").text)
                markup_admin_delete_order_list.append(f"Удалить Заказ №{s.o[i][0]}")
            markup_admin_wishlists.add("Вернуться в Админ-Панель")
            bot.send_message(message.chat.id, "Вот список заказанных на данный момент виш-листов:", reply_markup=markup_admin_wishlists)
        elif message.text in markup_admin_wishlists_array:  # просмотр выбранного заказа виш-листа
            full_order_info = ""
            for i in s.o[markup_admin_wishlists_array.index(message.text)]:
                markup_admin_for_order_list = ty.ReplyKeyboardMarkup(row_width=1)
                markup_admin_for_order_list.add(ty.KeyboardButton(f"Удалить Заказ №{s.o[markup_admin_wishlists_array.index(message.text)][0]}"))
                if (i == "" or i == " ") and (s.o[markup_admin_wishlists_array.index(message.text)].index(i) != 11): continue
                if s.o[markup_admin_wishlists_array.index(message.text)].index(i) == 0:
                    full_order_info += "<b>Номер заказа:</b> "
                    full_order_info += str(i)
                if s.o[markup_admin_wishlists_array.index(message.text)].index(i) == 1:
                    full_order_info += "<b>ID пользователя:</b> "
                    full_order_info += str(i)
                    full_order_info += "\n"
                    full_order_info += "\n"
                    full_order_info += "<b>Список заказанных товаров:</b>"
                if s.o[markup_admin_wishlists_array.index(message.text)].index(i) >= 2 and s.o[markup_admin_wishlists_array.index(message.text)].index(i) <= 11:
                    full_order_info += str(i)
                if s.o[markup_admin_wishlists_array.index(message.text)].index(i) == 12:
                    full_order_info += ("\n")
                    if sum_price([i for i in s.o[markup_admin_wishlists_array.index(message.text)][2:12]]) == 0: full_order_info += "Общая стоимость заказа будет уточнена в зависимости от выбранных пользователем объемов напитков"
                    else: full_order_info += f"Общая стоимость заказа: {sum_price([i for i in s.o[markup_admin_wishlists_array.index(message.text)][2:12]])}"
                    full_order_info += ("\n")
                    full_order_info += "<b>Имя и фамилия, указанные в Telegram-аккаунте:</b> "
                    full_order_info += str(i)
                if s.o[markup_admin_wishlists_array.index(message.text)].index(i) == 13:
                    full_order_info += "<b>Комментарии к заказу:</b> "
                    full_order_info += str(i)
                if s.o[markup_admin_wishlists_array.index(message.text)].index(i) == 14:
                    full_order_info += "<b>Точка выдачи заказа:</b> "
                    full_order_info += str(i)

                full_order_info += "\n"
            markup_admin_for_order_list.add("Вернуться в Админ-Панель")
            bot.send_message(message.chat.id, full_order_info, parse_mode="html", reply_markup=markup_admin_for_order_list)
        elif message.text in markup_admin_delete_order_list:  # Удаление выданного заказа после его выдачи
            s.sql.execute(f"""DELETE FROM orders WHERE ID = '{s.o[markup_admin_delete_order_list.index(message.text)][0]}';""")
            s.db.commit()
            bot.send_message(message.chat.id, "Выбранный заказ удален :)")
            os.execv(sys.executable, [sys.executable] + sys.argv)


@bot.callback_query_handler(func=lambda call: True)
def inline_markups(call):  # реакция бота на нажатия пользователем кнопок на клавиатурах внутри сообщений (под сообщениями)
    try:
        if call.message:
            print(call.data)
            print(markup_to_del_good_menu_array)
            if str(call.data) in new_menu_markup_in_array: # отображение страницы (раздела) товара
                good_n_name = good_name_by_id(call.data)
                markup_for_every_good = ty.ReplyKeyboardMarkup(row_width=1)
                markup_for_every_good.add(ty.KeyboardButton(f"Добавить {good_n_name} в виш-лист"),
                                          ty.KeyboardButton(f"Написать отзыв про {good_n_name}"),
                                          ty.KeyboardButton("Вернуться в Меню"),
                                          ty.KeyboardButton("Вернуться в Личный Кабинет"))

                if s.d[search_good_line_in_menu(good_n_name)][4] != None:
                    photoimage = s.d[search_good_line_in_menu(good_n_name)][4]
                    writeTofile(photoimage, 'pics/photoo_image.jpg')
                    bot.send_photo(call.message.chat.id, open('pics/photoo_image.jpg', 'rb'))

                i_current = search_good_line_in_menu(good_n_name)
                print(i_current)
                good_n = good(good_n_name, s.d[i_current][2], s.d[i_current][3], s.d[i_current][5], s.d[i_current][6],
                              s.d[i_current][7])

                bot.send_message(call.message.chat.id, good_n.description_info(), reply_markup=markup_for_every_good,
                                 parse_mode="html")
            elif str(call.data) in markup_to_del_good_menu_array:  # удаление выбранного товара
                just_to_admin_panel_markup = markup(["Вернуться в Админ-Панель"])
                s.sql.execute(f"""DELETE FROM goods WHERE id = '{call.data[3:]}';""")
                s.db.commit()
                bot.send_message(call.message.chat.id, "Товар успешно удален!", reply_markup=just_to_admin_panel_markup.m)
                os.execv(sys.executable, [sys.executable] + sys.argv)
            elif call.data in markup_to_red_good_menu_array: # выбор способа изменения определенного товара
                global good_red_name
                good_red_name = good_name_by_id(call.data[3:])
                red_good_info = ty.ReplyKeyboardMarkup(row_width=1)
                red_good_info.add(ty.KeyboardButton(f"Изменить название"), ty.KeyboardButton(f"Изменить описание"),
                                  ty.KeyboardButton("Изменить фотографию"), ty.KeyboardButton(f"Изменить цену"),
                                  ty.KeyboardButton(f"Изменить статус наличия по адресу Бульвар Любы Новоселовой, 18"),
                                  ty.KeyboardButton(f"Изменить статус наличия по адресу Можайское Шоссе, 55"),
                                  ty.KeyboardButton("Изменить категорию товара"))
                red_good_info.add(ty.KeyboardButton("Завершить редактирование информации о товаре"))
                bot.send_message(call.message.chat.id, "Что конкретно вы хотите изменить?", reply_markup=red_good_info)

    except: pass

bot.polling(none_stop=True)
