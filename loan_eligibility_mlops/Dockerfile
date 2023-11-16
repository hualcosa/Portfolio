FROM python:3.7.4

WORKDIR /app

COPY booster_vanilla.bst ./booster_vanilla.bst
COPY cat_encoder.joblib ./cat_encoder.joblib
COPY target_encoder.joblib ./target_encoder.joblib
COPY requirements.txt ./requirements.txt
COPY app.py ./app.py

RUN pip install -r requirements.txt

ENV PORT 8080
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app


