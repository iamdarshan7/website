FROM python:3
Run apt-get update 
copy . .
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --default-timeout=200 -r /requirements.txt \
    && rm -rf /requirements.txt
CMD ["echo" , "Hello my name is Darshan"]
RUN python3 manage.py migrate
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
