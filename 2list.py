'''
Transform data to list
'''
lst = '''
Красноярск
Алматы
Барнаул
Барнаул
Ставрополь
Омск
Омск
Арзамас
Сургут
Владимир
Вологда
Волгоград
Вологда
Улан-Удэ
Улан-Удэ
Королёв
Королёв
Глазов
Спб
Санкт-Петербург
Санкт-Петербург
Санкт-Петербург
Димитровград
Елец
Елец
Елец
Калининград
Зеленодольск
Заречный
Иваново
ИВаново
Иваново
Ижевск
Ижевск
Ижевск
Ижевск
Краснодар
Набережные Челны
Иркутск
Таганрог
Курган
Курган
Кемерово
Курган
Симферополь
Лысьва
Лысьва
Магнитогорск
Магнитогорск
Магнитогорск
Магнитогорск
Москва
Магнитогорск
Москва
Магнитогорск
Москва
Москва
Москва
Набережные Челны
Набережные Челны
Нижний Тагил
Нижний Новгород
Нижний Новгород
Нижний Новгород
Нижний Новгород
Нижний Новгород
Нижний Новгород
Нижний Новгород
Нижний Новгород
Нижний Новогрод
Нижний Новгород
Нижний Новгород
Казань
Нижний Тагил
Нижний Тагил
Нидний Тагил
Смоленск
Смоленск
Смоленск
Нижний Новгород
Нижний Новгород
Нижний Новгород
Нижний Новгород
Орёл
Пермь
Самара
Пермь
Пермь
Пермь
Чайковский
Уссурийск
Самара
Санкт-Петербург
Южно-Сахалинск
Якутск
Сыктывкар
Севастополь
Ставрополь
Смоленск
Санкт-Петербург
Санкт-Петербург
Нижний Новгород
Нижний Новгород
Симферополь
Лесной
Москва
Москва
Оренбург
Ярославль
Москва
Екатеринбург
Екатеринбург
Екатеринбург
Заречный
Заречный, Свердловская область
Биробиджан
Набережные Челны
Набережные Челны
Набережные челны
Набережные Челны
Благовещенск
Иркутск
Москва
Ижевск
Самара
Елец
Ижевск
Ижевск
Иркутск
Магнитогорск
Магнитогорск
Самара
Пермь
Самара
Самара
Сыктывкар
Сыктывкар
Ставрополь
Ульяновск
Екатеринбург
Пермь
САМАРА
Ярославль
Сатка
Симферополь
Хабаровск
Хабаровск
Чебоксары
Чебоксары
Чистополь
Челябинск
Челябинск
Челябинс
Челябинск
Ярославль
Ярославль
Ярославль
Россия
Россия
Санкт-Петербургский горный университет
Москва
Алматы
Клин
Барнаул
Калининград
Зюкайка
Пермь
Астрахань
Архангельск
Барнаул
Калининград
Калининград
Оренбург
Вологда
Ижевск
Ижевск
Ангарск
Астрахань
Ханты-Мансийск
Красноярск
Уфа
Уфа
Уфа
Белово
Калининград
Братск
Омск
Омск
Омск
Великий Устюг
Великий Устюг
Великий Утюг
Великий Устюг
Сокол
Череповец
Череповец
Череповец
Великий Устюг
Великий устюг
ВеликийУстюг
Омск
Орёл
Омск
Омск
Сарапул
Хоринск
Нижневартовск
Нягань
Советский
г.Урай
Югорск
Югорск
Советский
Уфа
Череповец
Омск
Орёл
Воронёж
Витебск
Владивосток
Владимир
Владимир
Верхняя Пышма
Вольск
Верхняя Пышма
ст. Вознесенская
Великий Устюг
Гавар
Чистополь
Чистополь
Альметьевск
Бугульма
Бугульма
Ангарск
Казань
Казань
Казань
Мамадыш
Мамадыш РТ
Мензелинск
Мензелинск
Мензелинск
Набережные Челны
Чистополь
Чистополь
Чистополь
Заинск
Мензелинск
Котлас
Бугуруслан
Вязники
Москва
Чита
Ишимбай
Ангарск
город Ангарск
Ангарск
Ишимбай
Краснодар
Кировск
Кандалакша
Мурманск
Мурманск
Электроугли
Казань
Кузнецк
Кузнецк
Самара
Стерлитамак
Артемовский
Артёмовский
Алапаевск
Алапаевск
Асбест
Кушва
Вольск
Вольск
Екатеринбург
Ирбит
Ирбит
Каменск-Уральский
Каменск-Уральскйи
Каменск-Уральский
Каменск-Уральский
Нижний Тагил
Нижний Тагил
Нижний Тагил
Балаково
Балаково
Ревда
Михайловск
Туринская Слобода
Тольятти Самарская область
Тольятти Самарская область
Тольятти
Тольятти Самарская область
Екатеринбург
Екатеринбург
Екатеринбург
Энгельс
Артемовский
Каменск-Уральский
Тольятти Самарская область
Алапаевск
пос. Баранчинский
Екатеринбург
Жигулевск
Краснотурьинск
Краснотуринск
Н-Тагил
Балаково
Первоуральск
Ревда
Реж
Михайловск
Михайловск
Тольятти
Екатеринбург
Энгельс
Каменск-Уральский
Стерлитамак
ГАПОУ Стерлитамакский колледж
р.п. Голышманово
Тюмень
Тюмень
Тюмень
Тюмень
Анадырь
Чистополь
Чистополь
Чистополь
Чебоксары
Якутск
Чистополь
Чистополь
Гатчина
Гатчина
Калининград
Калининград
Мыски
Волжский
Мыски
Мыскм
Ставрополь
Бутурлиновка
Тверь
Тверь
Тверь
Тверь
Тверь
Серпухов
Курган
Котово
Чернушка
Ангарск
с. Хоринск
Улан-Удэ
Волгоград
Волгоград
с.Московское
Заволжье
Заволжье
Иркутск
Нальчик
Катав-Ивановск
Москва
Котово
Котово
Чернушка
Чернушка
Чернушка
Чернушка
Лысьва
Нижний Новгород
Самара
г.Коркино пос.Первомайский
Пермь
Пермь
Пермь
Соликамск
Соликамск
Сызрань, Самарской области
Южно-Сахалинск
Ставрополь
Ставрополь
Тверь
Тверь
Тверь
п.Железнодорожный
Москва
Чайковский
Челябинск
Черемхово
Челябинск
Челябинкс
Челябинск
Чайковский
Челябинск
Шумиха
Челябинск
Котово
Чернушка
Челябинск
с. Долгодеревеннское
Астрахань
Астрахань
Астрахань
Астрахань
Астрахань
Белебей
Благовещенск
Владмир
п.Зюкайка
Зюкайка
Владимир
Ковров
Богучар
Богучар
Борисоглебск
Бутурлиновка
Бутурлиновка
Владимир
Воронеж
Воронеж
Россошь
Муром
Острогожск
Владимир
Воронеж
Ковров
Владимир
Владимир
Ковров
Острогожск
Острогожск
Волгоград
Москва
Москва
Георгиевск
Георгиевск
Георгиевск
Дзержинск
Дзержинск
Иркутск
Иркутск
Иркутск
Шелехов
Шелехов
иркутск
иркутск
Иркутск
Иркутск
Москва
Москва
Тихорецк
Армавир
ст.Вознесенская
ст. Вознесенская
Новороссийск
Тихорецк
Тихорецкий район поселок Парковый
Тихорецк
п.Парковый
Кушнаренково
село Кушнаренково
с. Кушнаренково
уфа
Калуга
Сосенский
Сосенский
Москва
Москва
Копейск
Копейск
Котово
Чернушка
Москва
Кушнаренково
Гатчина
Гатчина
Подпорожье
Гатчина
Междуреченск
Междуреченск
Миасс
Миасс Челябинской области
Муравленко
Жуковский
Дмитров
Коломна
Клин
Краснозаводск
Луховицы
Серпухов
Дмитров
Месягутово
Нефтекамск
Нефтекумск
Нефтекамск
Новосибирск
Ангарск
Братск
Москва
г Сердобск
г.Коркино п.Первомайский
Коркино. п.Первомайский
Челябинск
Коркинский район, поселок Первомайский
П. Первомайский
Коркинский район, поселок Первомайский
Пермь
Пермь
Пермь
Пермь
Пермь
Ставрополь
Йошкар-ола
Йошкар-Ола
Йошкар-Ола
Саранск
Саранск
Саранск
Йошкар-Ола
Белая Калитва
Батайск
Каменск-Шахтинский
Каменск-Шахтинский
Каменск-Шахтинский
Новочеркасск
Новочеркаск
Ростов-на-Дону
Ростов-на-Дону
Россия
Ростов-на-Дону
Сальск
Таганрог
Таганрог
Каменск-Шахтинский
Новочеркасск
Ростов-на-Дону
Ростов-на-Дону
Ростов-на-Дону
Таганрог
Черногорск
Ставрополь
Красноуфимск
Серов
Сухой Лог
Екатеринбург
Чапаевск
Сухой Лог
Чапаевск
город Светлоград
Стерлитамак
Ставрополь
Ставрополь
Сызрань
Тверь
Уфа
Уфа
Уфа
Уфа
Москва
Чайковский
Челябинск
Южноуральск
Салехард
Котово
Заволжье
Чернушка
Пермь
Челябинск
Иркутск
Клин
Тверь
Тверь
Уфа
Миасс
Калининград
Междуреенск
Липецк
Липецк
Гатчина
Энгельс
Талица
Гатчина
Гатчина
Москва
Москва
Республика Башкортостан, с.Кушнаренково
Междуреченск
Белово
Муравленко
Уфа
Кушнаренково
Гатчина
Белово
Воркута
Инта
Новокузнецк
Полысаево
Прокопьевск
Чита
Юрга
Гурьевск
Инта
Новокузнецк
Новокузнецк
Прокопьевск
Тольятти
Тульская область, Щекинский район, с.Селиваново
Таштагол
Юрга
Юрга
Юрга
Юрга
Рыбинск
Ярославль
Ярославль
Ярославль
Дзержинск
Екатеринбург
Краснодар
Златоуст
Набережные челны
Набережные Челны
Набережные Челны
Набережные Челны
Набережные Челны
Набережные Челны
Набережные Челны
Иркутск
Иркустк
Набережные Челны
Йошкар-Ола
Калуга
Камышлов
Камышлов
камышлов
Канаш
Канаш
Канаш
Владивосток
Владивосток
Владивосток
Уссурийск
Владивосток
Набережные Челны
Набережные Челны
Набережные Челны
Набережные Челны
Владивосток
Комсомольск-на-Амуре
Находка
Хабаровск
Комсомольск-на-Амуре
Красноярск
Комсомольск-на-Амуре
Спасск-Дальний
Спасск-Дальний
Хабаровск
Хабаровск
Хабаровск
Барнаул
Барнаул
Барнаул
Барнаул
Барнаул
Барнаул
Барнаул
Барнаул
Бийск
Барнаул
Енисейск
Канск
Канск
Красноярск
Красноярск
с. Павловск
Барнаул
Барнаул
Канск
Красноярск
Красноярск
Вилючинск
Краснодар
Якутск
Якутск
Красноярск
Челябинск
Екатеринбург
Красноярск
Красноярск
Краснодар
Красноярск
Кушнаренково
село Кушнаренково
с.Кушнаренково
краснодар
Омутнинск
Омутнинск
Омутнинск, Кировская Область, Российская Федерация
Омутнинск
Вятские Поляны
Омутнинск
Омутнинск
Омутнинск
Москва
Москва
Клин
Москва
Якутск
Якутск
Якутск
Пермь
Калининград
Набережные Челны
Пермь
Пермь
Пермь
Саратов
Якутск
Новосибирск
Пенза
Пенза
Москва
Москва
Сыктывкар
Екатеринбург
Екатеринбург
Комсомольск-на-Амуре
Пермь
Ковров
Пермь
Пермь
Комсомольск-на-Амуре
Комсомольск-на-Амуре
Краснодар
Красноярск
Красноярск
Красноярск
Красноярск
Саратов
Саратов
Саратов
Саратов
Саратов
Саратов
Саратов
Саратов
Саратов
Красноярск
Новосибирск
Калуга
Краснодар
Камышлов
Камылов
Красноярск
г. Москва
Екатеринбург
Краснодар
Краснодар
Курск
Курск
Курск
г.Куртамыш,
Каменск-Уральский
Кушнаренково
Качканар
Сыктывкар
Майкоп
Миасс
Междуреченск
Магнитогорск
Москва
п. Плещеево
Канаш
Мурманск
Tyumen
МОСКВА
Москва
Москва
Москва
Москва
Москва
Москва
Москва
Москва
Чебоксары
Чебоксары
Чебоксары
Казань
Казань
Чебоксары
Чебоксары
Чебоксары
Казань
Чебоксары
Чебоксары
Чебоксары
Чебоксары
Чебоксары
Омск
Арзамас
Новосибирск
Новочебоксарск
Челябинск
Якутск
Нижний Новгород
Nizhny Novgorod
Nizhny Novgorod
Нижний Новгород
Нижневартовск
Новосибирск
Нижний Тагил
Нижний Тагил
Набережные Челны
Омск
Боровичи
Железногорск (Курская обл.)
Курск
Курск
Курск
Боровичи
Боровичи
Белгород
Старый Оскол
г. Галич
Галич
Кострома
Кострома
Томск
Томск
Кострома
Смоленск
Томск
Омск
Озёрск
Озерск
Омск
Омск
Старый Оскол
Старый Оскол
Старый Оскол
Острогожск
Пермь
Пермь
Пермь
Пермь
Пермь
Санкт-Петербург
г. Петропавловск
Пенза
Балаково
Екатенринбург
Брянск
Саратов
Пермь
Пермь
Пермь
Саратов
Сыктывкар
Краснодар
Южно-Сахалинск
птг.Первомайский
г. Коркино, Пос. Первомайский
Санкт-Петербург
Комсомольск-на-Амуре
Ростов-на-Дону
Россошь
Рязань
Рязань
Санкт-Петербург
Саранск
Якутск
Красноярск
Саратов
Саратов
Смоленск
Смоленск
Смоленск
Смоленск
Смоленск
Смоленск
Смоленск
Нижний Новгород
Санкт-Петербург
Санкт-Петербург
Санкт-Петербург
Ставрополь
Ставрополь
Ставрополь
Ступино
Архангельск
Таганрог
Симферополь
Симферополь
Тверь
Димитровград
Кемерово
Кемерово
Кемерово
Кемерово
Кемерово
Кемерово
Кемерово
Кемерово
Кемерово
Кемерово
Кемерово
Пермь
Улан-Удэ
Улан-Уэ
Улан-Удэ
Ханты-Мансийск
Улан-Удэ
Тюмень
Талица
тамбов
томск
Томск
Томск
Тверь
Тверь
Тверь
Уфа
Екатеринбург
Екатеринбург
Екатеринбург
Екатеринбург
Екатеринбург
Екатеринбург
Екатеринбург
Уфа
Уфа
Витебск
Минск
Елец
Екатеринбург
Екатеринбург
Екатеринбург
Екатеринбург
Екатеринбург
Екатеринбург
Сургут
Москва
Екатеринбург
Екатеринбург
Екатеринбург
Екатеринбург
Полевской
Екатеринбург
Самара
Екатеринбург
Екатеринбург
Москва
Gghgg
Набережные Челны
Курск
Санкт-Петербург
Саратов
Самара
Витебск
Минск
Шелехов
Иркутск
Шелехов
Томск
Новокузнецк
Мичуринск
Черемхово
Челябинск
Черногорск
Краснодар
Чебоксары
Югорск
Челябинск
Юрга
Челябинск
Якутск
Якутск
Якутск
Якутск
Якутск
Якутск
Якутск
Якутск
Россия
Технологический колледж ВСГУТУ
Россия
Россия
Москва
Санкт-Петербург
г. Елец
Елец
Чудово
Екатеринбург
Екатеринбург
Екатеринбург
Ижевск
Тарко-Сале
г. Красногорск, Московская область
Ижевск
г. Красногорск, Московская область
Ижевск
Ижевск
Сочи
Сочи
Петрозаводск
Екатеринбург
Биробиджан
Омск
Ижевск
Ижевск
Екатеринбург
Екатеринбург
Екатеринбург
Миасс
Камышлов
.
Казань
Краснодар
Москва
кОНЧЕНЫЙ
Алматы
Твики
Красноярск
Ханарав
Краси
Екатеринбург
фывфыв
Сочи
Москва
dada
bdfogn
dadada
bdkl
dfgdf
dfgdfg
cbcbcbc
Pleasantville
sdf
Екатеринбург
sgw
fsfsfs
sfsf
gffgf
fgjfg
Springfield
Springfield
Hill Valley
Pleasantville
Pleasantville
gsrgvs
хоринск
vbdsrv
'''

print(lst.replace('\n','\',\n\''))