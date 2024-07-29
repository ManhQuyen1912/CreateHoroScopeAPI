from flask import Flask
from decouple import config
from flask_restx import Api

#tạo 1 web page
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version = 1.0,
    title = 'Horoscope API',
    description= 'Get horoscope data easily using the below APIs',
    license= 'MIT',
    contact= 'Manh Quyen',
    contact_email= '20521819@gm.uit.edu.vn',
    doc='/',
    prefix= '/api/v1'
)

from core import routes