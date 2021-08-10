FROM python:3.8-slim

EXPOSE 80
RUN mkdir /src
COPY requirements.txt /src
WORKDIR /src
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]


