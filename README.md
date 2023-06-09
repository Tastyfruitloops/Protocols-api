# Protocols-api
Вывод друзей пользователя с помощью инструментов VK API

## Задача:
По ссылке на страницу ВК данного пользователя вывести список друзей.

## Принцип работы VK API
VK API предоставляет набор методов для взаимодействия с социальной сетью ВКонтакте. Для использования VK API необходимо иметь токен доступа, который выдается при регистрации приложения на платформе VK.

При помощи GET запросов данная программа получает данные о пользователе и списке друзей


## Получение доступа к VK API
 Чтобы пользоваться VK API, нужно зарегистрировать приложение.
 Если у вас его нет, следуйте инструкции: https://vk.com/dev/first_guide.

 После успешной регистрации и авторизации вы будете иметь токен вашего приложения.
 
Токен нужно вставить в соотетсвующее поле в файле config.json

## Запуск

Запуск происходит через командную строку в следующем формате:

```
python vk_friends.py -link "profile link"
```

## Вывод

В консоль выводится список друзей в следующем формате

![image](https://github.com/Tastyfruitloops/Protocols-api/blob/main/assets/sample.jpeg)
