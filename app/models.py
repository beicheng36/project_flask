from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 表单的类
class Dhfs(db.Model):
    """
    电话费表
    """
    __tablename__ = 'dhfs'
    sd = db.Column(db.Integer, primary_key=True)
    tr = db.Column(db.Float())
    dx = db.Column(db.Float())
    kt = db.Column(db.Float())
    yx = db.Column(db.Float())
    hj = db.Column(db.Float())

    def get_columns(self):
        return tuple(col.name for col in self.__table__.columns)

    def to_dict(self):
        return dict([(col, getattr(self, col)) for col in self.get_columns()])

    def __repr__(self):
        return '{0}'.format(self.hj)



class Dyfs(db.Model):
    """
    打印费表
    """
    __tablename__ = 'dyfs'
    sd = db.Column(db.Integer, primary_key=True)
    fy = db.Column(db.Float())
    bz = db.Column(db.String(20))

    def get_columns(self):
        return [col.name for col in self.__table__.columns]

    def to_dict(self):
        return dict([(col, getattr(self, col)) for col in self.get_columns()])
 




class Kdfs(db.Model):
    """
    电信联通表
    """
    __tablename__ = 'kdfs'
    sd = db.Column(db.String(10), primary_key=True)
    fy = db.Column(db.Float())
    bz= db.Column(db.String(15))

    def __repr__(self):
        return '{0}'.format(self.fy)



