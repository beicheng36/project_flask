from wtforms import Form,IntegerField,FloatField,SubmitField

class NEDhfForm(Form):
    sd = IntegerField('费用账期:')
    tr = FloatField('天润费用:')
    dx = FloatField('东信费用:')
    kt = FloatField('科天费用:')
    yx = FloatField('颐信费用:')
    hj = FloatField('总计费用:')
    submit = SubmitField('提交:')



