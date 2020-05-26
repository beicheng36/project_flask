from fyb import db


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
        return [col.name for col in self.__table__.columns]

    def to_dict(self):
        return dict([(col, getattr(self, col)) for col in self.get_columns()])


    def __repr__(self):
        return '{0}'.format(self.hj)

#if __name__ == "__main__":
    #db.drop_all()
    #db.create_all()
    #print('Done')
