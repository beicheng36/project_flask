from flask import Blueprint, render_template, request, redirect, url_for,flash
from app.forms import NEDhfForm, DyfForm, KdfForm
from app.controllers import DhfsDao
from app.models import Dhfs, Dyfs,Kdfs


# 定义蓝图
fydsbp = Blueprint('fydsbp', __name__, template_folder='templates')



# 电话费表单路由
@fydsbp.route('/')
def index():

    rdservice = DhfsDao()
    rds = rdservice.list_all(Dhfs)
    return render_template('index.html', rds=rds)


@fydsbp.route('/new', methods=['GET', 'POST'])
def new_rd():    
    form = NEDhfForm()

    if request.method == 'POST':
        dservice = DhfsDao()
        new_rd = Dhfs(
            sd = request.form['sd'],
            tr = request.form['tr'],
            dx = request.form['dx'],
            kt = request.form['kt'],
            yx = request.form['yx'],
            hj = request.form['hj']
        )
        dservice.create_rd(new_rd)
        return redirect(url_for('fydsbp.index'))

    return render_template('new_dhfrd.html', form=form, tls= "新增记录")


@fydsbp.route('/edit/<int:rd_sd>', methods=['GET','POST'])
def edit_rd(rd_sd):
    form = NEDhfForm()
    rd = DhfsDao().get_rd(Dhfs, rd_sd)
    if request.method == 'POST':
        rd.tr = request.form['tr']
        rd.dx = request.form['dx']
        rd.kt= request.form['kt']
        rd.yx= request.form['yx']
        rd.hj= request.form['hj']
        DhfsDao().update_rd(Dhfs, rd)
        return redirect(url_for('fydsbp.index'))        
    form.sd.data = rd.sd
    form.tr.data = rd.tr
    form.dx.data = rd.dx
    form.kt.data = rd.kt
    form.yx.data = rd.yx
    form.hj.data = rd.hj
    return render_template('new_dhfrd.html', form=form, tls = "修改记录")


@fydsbp.route('/delete/<int:rd_sd>', methods=['GET'])
def delete_rd(rd_sd):
    rdsdao = DhfsDao()
    rd = rdsdao.get_rd(Dhfs,rd_sd)
    rdsdao.delete_rd(Dhfs, rd)
    flash('Success deletc')
    return redirect(url_for('fydsbp.index'))




# 打印费用表单

@fydsbp.route('/dy', methods=['GET', 'POST'])
def dyfs():
    form = DyfForm()
    rds =DhfsDao().list_all(Dyfs)
    if request.method == 'POST':
        new_rd = Dyfs(
            sd = request.form['sd'],
            fy = request.form['fy'],
            bz = request.form['bz']
        )
        DhfsDao().create_rd(new_rd)
        return redirect(url_for('fydsbp.dyfs'))
    return render_template('dyfs.html', rds=rds, form=form, tls="提交记录")

@fydsbp.route('/del/<int:rd_sd>', methods=['GET'])
def del_rd(rd_sd):
    rdsdao = DhfsDao()
    rd = rdsdao.get_rd(Dyfs,rd_sd)
    rdsdao.delete_rd(Dyfs, rd)
    flash('Success deletc')
    return redirect(url_for('fydsbp.dyfs'))


@fydsbp.route('/editfyd/<int:rd_sd>', methods=['GET','POST'])
def ed_rd(rd_sd):
    form = DyfForm()
    rd = DhfsDao().get_rd(Dyfs, rd_sd)
    rds = DhfsDao().list_all(Dyfs)
    print(rds)
    if request.method == 'POST':
        rd.sd = request.form['sd']
        rd.fy = request.form['fy']
        rd.bz= request.form['bz']
        DhfsDao().update_rd(Dyfs, rd)
        return redirect(url_for('fydsbp.dyfs'))        
    form.sd.data = rd.sd
    form.fy.data = rd.fy
    form.bz.data = rd.bz
    return render_template('dyfs.html',rds=rds,form=form, tls="修改记录")


# 宽带费用表单

@fydsbp.route('/kd', methods=['GET', 'POST'])
def kdfs():
    form = KdfForm()
    rds =DhfsDao().list_all(Kdfs)
    if request.method == 'POST':
        new_rd = Kdfs(
            sd = request.form['sd'],
            fy = request.form['fy'],
            bz = request.form['bz']
        )
        DhfsDao().create_rd(new_rd)
        return redirect(url_for('fydsbp.kdfs'))
    return render_template('kdfs.html', rds=rds, form=form, tls="提交记录")

@fydsbp.route('/del_fyds/<string:rd_sd>', methods=['GET'])
def del_kdrd(rd_sd):
    rdsdao = DhfsDao()
    rd = rdsdao.get_rd(Kdfs,rd_sd)
    rdsdao.delete_rd(Kdfs, rd)
    flash('Success deletc')
    return redirect(url_for('fydsbp.kdfs'))


@fydsbp.route('/editkds/<string:rd_sd>', methods=['GET','POST'])
def ed_kdrd(rd_sd):
    form = KdfForm()
    rd = DhfsDao().get_rd(Kdfs, rd_sd)
    rds = DhfsDao().list_all(Kdfs)
    print(rds)
    if request.method == 'POST':
        rd.sd = request.form['sd']
        rd.fy = request.form['fy']
        rd.bz= request.form['bz']
        DhfsDao().update_rd(Kdfs, rd)
        return redirect(url_for('fydsbp.kdfs'))        
    form.sd.data = rd.sd
    form.fy.data = rd.fy
    form.bz.data = rd.bz
    return render_template('kdfs.html',rds=rds,form=form, tls="修改记录")
