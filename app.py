from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from wtforms import Form,IntegerField,FloatField,SubmitField
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://xuheng:Xh1234@192.168.103.126/WHCCDB1'  #'sqlite:///Dhfs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





# 表单的类
class Dhfs(db.Model):
    sd = db.Column(db.Integer, primary_key=True)
    tr = db.Column(db.Float())
    dx = db.Column(db.Float())
    kt = db.Column(db.Float())
    yx = db.Column(db.Float())
    hj = db.Column(db.Float())

    def __repr__(self):
        return '{0},{1},{2},{3},{4},{5}'.format(self.crw[0], self.tr, self.dx, self.kt, self.yx, self.hj)



# 建表
#db.drop_all()
#db.create_all()


# 表的控制函数

class DhfsDao():
    # 新增记录
    def create_rd(self, rd_sd, rd_tr, rd_dx, rd_kt, rd_yx, rd_hj):
        new_rd = Dhfs(sd=rd_sd, tr=rd_tr, dx=rd_dx, kt=rd_kt, yx=rd_yx, hj=rd_hj)
        db.session.add(new_rd)
        db.session.commit()
        return new_rd

    # 删除记录
    def delete_rd(self, rd):
        to_delete_rd = Dhfs.query.get(rd.sd)
        db.session.delete(to_delete_rd)
        db.session.commit()
        return True
    # 编辑记录
    def update_rd(self,rd):
        modified_rd = Dhfs.query.get(rd.sd)
        db.session.commit()
        return modified_rd
 
    # 显示表
    def list_all(self):
        return Dhfs.query.order_by(Dhfs.sd).all()

    # 查询记录
    def get_rd(self, sd):
        return Dhfs.query.get(sd)

# Form单类

class NewDhfForm(Form):
    sd = IntegerField('费用账期:')
    tr = FloatField('天润费用:')
    dx = FloatField('东信费用:')
    kt = FloatField('科天费用:')
    yx = FloatField('颐信费用:')
    hj = FloatField('总计费用:')
    submit = SubmitField('提交:')

class EditNoteForm(Form):
    sd = IntegerField('费用账期:')
    tr = FloatField('天润费用:')
    dx = FloatField('东信费用:')
    kt = FloatField('科天费用:')
    yx = FloatField('颐信费用:')
    hj = FloatField('总计费用:')
    submit = SubmitField('提交:')



# 网页路由
@app.route('/')
def index():

    rdservice = DhfsDao()
    rds = rdservice.list_all()
    return render_template('index.html', rds=rds)


@app.route('/new', methods=['GET', 'POST'])
def new_rd():    
    form = NewDhfForm()

    if request.method == 'POST':
        sd = request.form['sd']
        tr = request.form['tr']
        dx = request.form['dx']
        kt = request.form['kt']
        yx = request.form['yx']
        hj = request.form['hj']
        dservice = DhfsDao()
        dservice.create_rd(sd, tr, dx, kt, yx, hj)
        return redirect(url_for('index'))

    return render_template('new_dhfrd.html', form=form)


@app.route('/edit/<int:rd_sd>', methods=['GET','POST'])
def edit_rd(rd_sd):
    form = EditNoteForm()
    rd = DhfsDao().get_rd(rd_sd)
    if request.method == 'POST':
        tr = request.form['tr']
        dx = request.form['dx']
        kt = request.form['kt']
        yx = request.form['yx']
        hj = request.form['hj']
        rd.tr = tr
        rd.dx = dx
        rd.kt = kt
        rd.yx = yx
        rd.hj = hj
        DhfsDao().update_rd(rd)
        return redirect(url_for('index'))        
    form.sd.data = rd.sd
    form.tr.data = rd.tr
    form.dx.data = rd.dx
    form.kt.data = rd.kt
    form.yx.data = rd.yx
    form.hj.data = rd.hj
    return render_template('edit_rd.html', form=form)


@app.route('/delete/<int:rd_sd>', methods=['GET'])
def delete_rd(rd_sd):
    rdsdao = DhfsDao()
    rd = rdsdao.get_rd(rd_sd)
    rdsdao.delete_rd(rd)
    return redirect(url_for('index'))


@app.route('/loading')
def load1():
    return '此页面,正在开发中.......'

    



