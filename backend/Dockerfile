# syntax=docker/dockerfile:1
FROM python:3.9

EXPOSE 80



COPY /backend/requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt


COPY . .

ENTRYPOINT ["python3", "/backend/main.py"]
