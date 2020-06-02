from wtforms import Form,FloatField,SubmitField,StringField,IntegerField
from wtforms.validators import DataRequired, Length

class NEDhfForm(Form):
    sd = IntegerField('费用账期:', validators=[DataRequired(), Length(4,6)])
    tr = FloatField('天润费用:', validators=[DataRequired(), Length(6,7)])
    dx = FloatField('东信费用:', validators=[DataRequired(), Length(6,7)])
    kt = FloatField('科天费用:', validators=[DataRequired(), Length(6,7)])
    yx = FloatField('颐信费用:', validators=[DataRequired(), Length(6,7)])
    hj = FloatField('总计费用:', validators=[DataRequired(), Length(6,7)])
    submit = SubmitField('提交:', validators=[DataRequired(), Length(8,10)])

class DyfForm(Form):
    sd = IntegerField('费用账期:', validators=[DataRequired(), Length(4,6)])
    fy = FloatField('打印费用:', validators=[DataRequired(), Length(4,6)])
    bz = StringField('备注信息:', validators=[DataRequired(), Length(1,20)])
    submit = SubmitField('提交:', validators=[DataRequired(), Length(4,6)])


class KdfForm(Form):
    sd = StringField('费用账期:', validators=[DataRequired(), Length(4,6)])
    fy = FloatField('费用明细:', validators=[DataRequired(), Length(8,10)]) 
    bz = StringField('备注信息:', validators=[DataRequired(), Length(1,20)])
    submit = SubmitField('提交:')   
