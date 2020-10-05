from mongoengine import connect
from fastapi_mail import FastMail
from jinja2 import Environment, FileSystemLoader
import os

email = 'mail'
email_password = 'password'

backend_url = 'http://127.0.0.1:8000'

connection = connect('dbname')

mail = FastMail(email=email,password=email_password,tls=True,port="587",service="gmail")

jinja_env = Environment(
    loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))