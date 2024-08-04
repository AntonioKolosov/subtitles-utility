FROM python:3.10-slim
WORKDIR /home/app
COPY main.py ./
COPY . .
ENTRYPOINT ["python", "./main.py"]