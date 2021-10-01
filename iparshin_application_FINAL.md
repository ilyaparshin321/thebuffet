# Паршин Илья - "The Buffet"

### Группа: 10 - МИ - 3
### Электронная почта: elijahparshin@gmail.com
### VK: https://vk.com/ilyaparshin321


**[ НАЗВАНИЕ ПРОЕКТА ]**

**Telegram-бот для сети кофеен “The Buffet”**

**[ ПРОБЛЕМНОЕ ПОЛЕ ]**

Заказчик – развивающаяся сеть кафе - не имеет своего сайта / бота / приложения / любого другого информационного ресурса, который бы облегчил и сделал персонализированным выбор и покупку товаров из существующего меню кафе для посетителей. 

Сейчас у клиентов, фактически, нет возможности легкого и удобного просмотра меню, возможности осуществлять полностью бесконтактные заказы, а также возможности заранее узнавать о скидках на определенные товары, которые могли бы быть им выгодны. Создание бота позволит решить эти проблемы. Открыв телеграм-бота сети, пользователи смогут просмотреть меню кафе, легко осуществить бесконтактный заказ, а также использовать купоны, чтобы получать скидки на акционные товары.

Сейчас у администрации и работников сети нет возможности быстрого информирования клиентов об изменениях в меню, которые могут быть им интересны, а также нет возможности получения дистанционной обратной связи (отзывов) о своей продукции от самих пользователей. Создание телеграм-бота позволит решить эти проблемы. Меню, отображаемое в одном из разделов бота, будет изменяемо, следовательно, используя бота, клиенты всегда будут видеть новейшее меню и доступные сейчас товары. Также, клиенты смогут писать отзывы на товары, а администрация, в свою очередь, читать их, чтобы улучшить сервис.

**[ ЗАКАЗЧИК / ПОТЕНЦИАЛЬНАЯ АУДИТОРИЯ ]**

Заказчик – сеть кафе / кофеен “The Buffet”, точки сети которой расположены в г. Одинцово, Московская Область.
Контактные данные заказчика: номер телефона: 89165701515

**[ АППАРАТНЫЕ ТРЕБОВАНИЯ ]**

Продукт разрабатывается как Telegram-бот. 

**[ ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ ]**

Программный продукт будет предоставлять следующие возможности:
* Показ меню кафе. Будет отображаться полный список товаров, доступных для покупки. Будут доступны различные способы фильтрации меню для более удобного восприятия пользователем. С изменением меню будет изменяться и список товаров в боте.
* Показ информации о каждом продукте. Клиент сможет узнать подробнее о том, что собирается купить: название товара, его описание, фотографии и т. д. 
* Список “Избранное”. Пользователь сможет добавлять понравившиеся товары в отдельный список “Избранное”, чтобы впоследствии с легкостью находить то, что хочет заказать. Сформированный список "Избранное" можно будет оформить как заказ, чтобы, находясь в кофейне, более оперативно и безопасно его сделать и получить. В условиях пандемии это также может быть использовано как технология заказов на вынос.
* Показ акций дня и эксклюзивных скидок по купонам специально для пользователей бота. Пользователям бота будут доступны специальные купоны и акции, которые будут размещаться в специальном разделе этого бота и которые можно будет предъявить (в виде QR-кода, который бариста должен будет просканировать, чтобы проверить актуальность купона) на кассе в самой кофейне, чтобы получить скидку на тот или иной товар.
* Показ расположения точек сети и краткой информации о них вместе с фотографиями. Это позволит клиентам проще сориентироваться и выбрать ближайшую к ним точку сети.
* Обратная связь. У клиентов будет возможность написать отзыв на каждый из товаров. Администраторы кафе также эти отзывы смогут увидеть.
* Персонализация. При первом использовании бота клиенту будет предложено пройти опрос, который определит его вкусовые предпочтения. На основании результатов этого опроса пользователям будут рекомендоваться различные товары.
* Для администраторов: Информация о заказах из списков "Избранное". Администраторы кафе, в своей части бота, смогут видеть заказы клиентоов, сформированные из их списков "Избранное", а также необходимую информацию об этиъ заказах: ФИО покупателя, суммарную цену заказа, пожелания покупателя, номер заказа, список товаров в заказе и т. д.
* Для администраторов: Админ-панель. Через собственное меню администратор сможет: 1) изменять список меню (добавлять новые товары и удалять уже имеющиеся товары; 2) редактировать информацию о товарах (фотографии, название, описание); 3) указывать наличие / отсутствие товаров в каждой из точек сети кафе
* Для администраторов: специальный двухфакторный вход в режим администратора (и админ-панель). Для входа будет необходимо знать специльную команду (о которой не будут знать обычные пользователи) и пароль, который необходимо будет ввести после использования этой команды. Также бот будет пропускать в режим администратора (и админ-панель) только пользователей, чьи имена пользователя указаны в программном коде бота, что позволит обеспечить высокий уровень защищенности режима администратора (и админ-панели) от пользователей, которым этот режим не должен быть доступен.

**[ ПОХОЖИЕ / АНАЛОГИЧНЫЕ ПРОДУКТЫ ]**

Анализ 3 программных продуктов, которые максимально приближены к заданному функционалу, показал, что:
* Приложение “Starbucks”: неудобный дизайн, малая информативность, нет возможности показа меню прямо в приложении. Также, так как это приложение, пользователям может быть неудобно его скачивать и привыкать к его интерфейсу
* Сайт “KFC”:  Неудобная система навигации по сайту, разделенная на две части: всплывающее боковое меню и гиперссылки внизу страницы. Также, так как это сайт, на нем не всегда удобно ориентироваться пользователям, первый раз его посещающим, особенно на мобильных устройствах.
* Бот кафе “Цапа”: Нет аналога списка "Избранное", а также есть разделы, заведомо сомнительно интересные обычному пользователю.
 
**[ ИНСТРУМЕНТЫ РАЗРАБОТКИ ]**

Python 3, pyTelegramBotAPI, SQLite3.

**[ ЭТАПЫ РАЗРАБОТКИ ]**

* Проектирование интерфейса и способов взаимодействия пользователя с ботом.
* Написание кода бота для первичных функций: списка меню, информации о товарах и списка точек.
* Написание кода для расширенных функций: список “Избранное”; меню купонов и акций; персонализация; обратная связь
* Дальнейшая работа над визуализацией и частичное изменение интерфейса и способов взаимодействия в зависимости от написанного кода.
* Тестирование, отладка.
* Подготовка к защите проекта.
 
**[ ВОЗМОЖНЫЕ РИСКИ ]**
* Неверная оценка стека технологий, которые мне нужно будет изучить, следовательно, нехватка времени на изучение необходимых языков программирования на должном уровне.
* Сложность отслеживания и удаления багов в процессе разработки, вследствие чего теоретически возможно, что некоторые баги останутся и к моменту защиты.
* Трудности в работе с базами данных, которые возможно пригодятся для некоторых функций.
