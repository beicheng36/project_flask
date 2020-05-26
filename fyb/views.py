from flask import render_template, request, redirect, url_for
from fyb.forms import NEDhfForm
from fyb.controllers import DhfsDao
from fyb import app




# 网页路由
@app.route('/')
def index():

    rdservice = DhfsDao()
    rds = rdservice.list_all()
    return render_template('index.html', rds=rds)


@app.route('/new', methods=['GET', 'POST'])
def new_rd():    
    form = NEDhfForm()

    if request.method == 'POST':
        dservice = DhfsDao()
        dservice.create_rd(request.form['sd'],request.form['tr'], request.form['dx'], request.form['kt'], request.form['yx'], request.form['hj'])
        return redirect(url_for('index'))

    return render_template('new_dhfrd.html', form=form, tls= "新增记录")


@app.route('/edit/<int:rd_sd>', methods=['GET','POST'])
def edit_rd(rd_sd):
    form = NEDhfForm()
    rd = DhfsDao().get_rd(rd_sd)
    if request.method == 'POST':
        rd.tr = request.form['tr']
        rd.dx = request.form['dx']
        rd.kt= request.form['kt']
        rd.yx= request.form['yx']
        rd.hj= request.form['hj']
        DhfsDao().update_rd(rd)
        return redirect(url_for('index'))        
    form.sd.data = rd.sd
    form.tr.data = rd.tr
    form.dx.data = rd.dx
    form.kt.data = rd.kt
    form.yx.data = rd.yx
    form.hj.data = rd.hj
    return render_template('new_dhfrd.html', form=form, tls = "修改记录")


@app.route('/delete/<int:rd_sd>', methods=['GET'])
def delete_rd(rd_sd):
    rdsdao = DhfsDao()
    rd = rdsdao.get_rd(rd_sd)
    rdsdao.delete_rd(rd)
    return redirect(url_for('index'))


@app.route('/loading')
def load1():
    return '此页面,正在开发中.......'
