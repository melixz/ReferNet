# Реферальная Система

Это API реферальной системы, разработанное на Django REST Framework. Оно позволяет пользователям регистрироваться и авторизоваться по номеру телефона, создавать и использовать реферальные коды.

## Функционал

- Авторизация по номеру телефона с имитацией отправки кода.
- Верификация кода, полученного по СМС.
- Создание уникального реферального кода для каждого нового пользователя.
- Возможность активировать реферальный код другого пользователя.
- Просмотр профиля пользователя, включая список номеров телефонов пользователей, которые активировали его реферальный код.
