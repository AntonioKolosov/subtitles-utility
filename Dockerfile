FROM python:3.8-slim
WORKDIR /home/app
COPY main.py ./
COPY . .
RUN mkdir -m 555 in
RUN mkdir -m 555 out
ENTRYPOINT ["python", "./main.py"]