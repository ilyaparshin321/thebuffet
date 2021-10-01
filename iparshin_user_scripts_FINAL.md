# Паршин Илья - "The Buffet"
# Пользовательские сценарии
**Группа: 10 - И - 3**

**Электронная почта: elijahparshin@gmail.com**

**VK: https://vk.com/ilyaparshin321**

### [Сценарий 1 - Добавление товара в избранное]
1. Пользователь заходит в раздел «Меню»
2. Пользователь ищет товар, который хочет добавить в избранное 
3. Пользователь выбирает этот товар
4. Пользователь видит кнопку, на которой находится надпись “Добавить {название товара} в избранное”
5. Пользователь нажимает на эту кнопку
6. Товар добавляется в избранное
7. Пользователь может нажать на кнопку столько раз, сколько товаров выбранного вида он хочет добавить в избранное

### [Сценарий 2 - Настройка списка товаров в меню]
1. Пользователь заходит в раздел «Меню»
2. Сортировка:
	1. Пользователь нажимает на кнопку с надписью «Сортировка»
	2. Пользователь выбирает один из вариантов сортировки: по цене по убыванию / по цене по возрастанию / по наименованию товара в алфавитном порядке
	3. Пользователь попадает обратно в раздел «Меню», где товары отсортированы выбранным им способом.
3. Фильтрация:
	1. Пользователь нажимает на кнопку с надписью «Фильтр»
	2. Пользователь выбирает параметры фильтрации по виду товара: горячий напиток / холодный напиток / основное блюдо / десерт
	3. Пользователь попадает обратно в раздел «Меню», где товары отфильтрованы выбранным им способом.
4. Поиск:
	1. Пользователь нажимает на кнопку с надписью "Поиск по названию"
	2. Пользователь вводит название товара в поле для поиска
	3. Если товар с таким названием есть в меню: пользователь попадает на страницу с информацией об этом товаре
	4. Если товара с таким названием нет в меню: Бот отправляет пользователю сообщение о том, что товара, который ищет пользователь, в меню на данный момент нет

### [Сценарий 3 - Использование купонов при заказе]
1. Пользователь заходит в раздел “Акции и купоны” 
2. Пользователь ищет необходимый ему купон, листая страницу
3. Пользователь выбирает этот купон
4. Пользователю отображается QR-код
5. Пользователь показывает этот QR-код бариста
6. Бариста сканирует QR-код
7. Система проверяет действительность QR-кода 
8. В случае действительности QR-кода бариста выдает пользователю товар с обозначенной на купоне скидкой.
9. В случае недействительности QR-кода товар не выдается.

### [Сценарий 4 - Получение информации о точках кофеен]
1. Пользователь заходит в раздел «Кофейни»
2. Пользователь ищет кофейню, информацию о которой хочет посмотреть
3. Пользователь выбирает эту кофейню
4. Если пользователю нужны фотографии, пользователь сразу нажимает на уже присланные фотографии, чтобы их просмотреть
5. Если пользователю нужна информация о времени работы кофейни:
	1. Пользователь ищет подраздел “Время работы”
	2. Пользователь видит указанное время работы кофейни
6. Если пользователю нужна информация о расположении кофейни:
	1. Пользователь заходит в раздел “Местоположение {название кофейни}”
	2. Пользователю открывается карта, где он может видеть место расположения данной кофейни
7. Если пользователю нужна информация о контактах кофейни:
	1. Пользователь ищет подраздел “Контакты”
	2. Пользователь видит контакты данной кофейни

### [Сценарий 5 - Просмотр информации о товаре]
1. Пользователь заходит в раздел «Меню»
2. Пользователь ищет товар, информацию о котором хочет посмотреть
3. Пользователь выбирает этот товар
4. Пользователь получает от бота сообщение с описанием этого товара
5. Пользователь попадает в раздел товара
6. Пользователь видит фотографии
7. Также ользователь сможет просмотреть прочую информацию о товаре: описание, его пищевую ценность и т. д. 

### [Сценарий 6 - Написание отзыва о товаре]
1. Пользователь заходит в раздел «Меню»
2. Пользователь ищет товар, отзыв на который хочет написать, и переходит на страницу с описанием этого товара
3. Снизу от основной информации пользователю отображается кнопка «Написать отзыв»
4. Пользователь нажимает на эту кнопку
5. Пользователь пишет отзыв
6. Пользователь нажимает кнопку «Отправить»
7. Отправленный отзыв: Пользователь видит свой только что отправленный отзыв.

### [Сценарий 7 - Просмотр списка рекомендованных товаров]
1. Пользователь заходит в раздел «Рекомендации»
2. Пользователь видит сообщение «Рекомендации»
3. Пользователь пролистывает это сообщение ниже до подзаголовка "Товары, подобранные специально для вас:"
4. Пользователь пролистывает чуть ниже, чтобы увидеть сам список
5. Пользователю отображается список рекомендованных ему товаров
6. Пользователь прочитывает этот список
7. Пользователь переходит в раздел меню, чтобы почитать об этих товарах побольше и, возможно, добавить их в избранное, в последствии используя для этого сценарий №1

### [Сценарий 8 - Проверка предоставленного QR-кода бариста]
1. Пользователь предоставляет бариста QR-код
2. Бариста сканирует этот QR-код
3. Если QR-код содержал информацию об акции или купоне
	1. Бариста выводится документ с наименованиями товаров, на которые предоставляется скидка, и с их ценами с учетом этой скидки
	2. Бариста прочитывает информацию в документе
	3. Бариста добавляет в заказ акционный товар по указанной в документе цене
	4. Бариста готовит этот заказ и выдает его пользователю с учетом цен, указанных в документе
5. Если QR-код не действителен, бариста не будет перенаправлен ни на один из перечисленных выше документов.