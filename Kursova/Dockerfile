FROM python:3.11-alpine

WORKDIR /app

COPY Kursova/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install alembic

COPY Kursova/app /app
COPY Kursova/.env /app/.env

EXPOSE 8000

COPY Kursova/app/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
