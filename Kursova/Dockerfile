FROM python:3.11-alpine

WORKDIR /app

COPY Kursova/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install alembic

COPY . .

EXPOSE 8000

COPY Kursova/app/entrypoint.sh Kursova/app/entrypoint.sh
RUN chmod +x Kursova/app/entrypoint.sh

ENTRYPOINT ["Kursova/app/entrypoint.sh"]
