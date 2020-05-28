import os
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://xuheng:Xh1234@192.168.103.126/WHCCDB1'  #'sqlite:///Dhfs.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False