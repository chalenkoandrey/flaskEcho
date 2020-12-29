FROM python:3.7.9-alpine
WORKDIR /usr/src/app
COPY main.py .
ENV FLASK_APP=main.py 
ENV FLASK_RUN_PORT=5000
RUN pip install Flask
CMD ["flask", "run" ,"--host=0.0.0.0"]