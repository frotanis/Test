# Беремо офіційний образ Python
FROM python:3.13-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Забороняємо Пітону створювати зайві файли кешу (.pyc)
ENV PYTHONDONTWRITEBYTECODE 1
# Забороняємо буферизацію виводу (щоб логи одразу йшли в термінал)
ENV PYTHONUNBUFFERED 1

# Копіюємо файл залежностей і встановлюємо їх
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копіюємо весь код проєкту в контейнер
COPY . /app/