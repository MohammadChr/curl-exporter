FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip install prometheus_client
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apk --no-cache add curl
EXPOSE 9998

CMD ["python", "script.py"]
