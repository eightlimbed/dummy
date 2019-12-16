FROM python:3-alpine
RUN pip install -r requirements.txt
WORKDIR /app
COPY . .
CMD python