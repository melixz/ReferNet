# Использование официального образа Python как базового
FROM python:3.12

# Установка рабочей директории в контейнере
WORKDIR /app

# Копирование файла зависимостей и установка зависимостей
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальной части приложения в рабочую директорию
COPY . .

# Сообщаем Docker, что контейнер слушает на порту 8000
EXPOSE 8000

# Запуск сервера Django при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
