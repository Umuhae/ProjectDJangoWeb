FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Umuhae/ProjectDJangoWeb.git

WORKDIR /home/ProjectDJangoWeb/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=_6igx5=9*k0v)i1ph3#g4)8*3-n6a%$3g_*wdd2o0$%pygi0x4" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

