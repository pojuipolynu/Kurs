#!/bin/sh

if [ -f "/app/alembic.ini" ]; then
    alembic upgrade head
else
    echo "Alembic configuration file not found at /app/alembic.ini"
    exit 1
fi

if [ -f "/app/main.py" ]; then
    python /app/main.py
else
    echo "Main application file not found at /app/main.py"
    exit 2
fi
