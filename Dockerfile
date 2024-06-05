FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Set the environment variables
ENV  CONFIG_MODE = development
ENV DEVELOPMENT_DATABASE_URL = 'postgresql+psycopg2://postgres:password@localhost:5432/reservas'

EXPOSE 5000

CMD ["sh", "-c", "flask db upgrade && flask run --host=0.0.0.0"]