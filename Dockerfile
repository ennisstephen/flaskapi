FROM python:3.9-slim-bookworm
WORKDIR /app
COPY . /app
RUN pip3 install Flask
RUN pip3 install Flask_RESTful
EXPOSE 5000
CMD python3 ./main.py
