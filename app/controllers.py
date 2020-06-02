from app.models import db


# 电话费表的控制类
class DhfsDao():
    # 新增记录
    def create_rd(self, new_rd):
        db.session.add(new_rd)
        db.session.commit()
        return new_rd

    # def create_rd(self,rd_sd,rd_tr,rd_dx,rd_kt,rd_yx,rd_hj):
        # new_rd = Dhfs(sd=rd_sd,tr=rd_tr,dx=rd_dx,kt=rd_kt,yx=rd_yx,hj=rd_hj)
        # db.session.add(new_rd)
        # db.session.commit()
        # return new_rd

    # 删除记录
    def delete_rd(self, mds, rd):
        to_delete_rd = mds.query.get(rd.sd)
        db.session.delete(to_delete_rd)
        db.session.commit()
        return True
    # 编辑记录
    def update_rd(self,mds, rd):
        modified_rd = mds.query.get(rd.sd)
        db.session.commit()
        return modified_rd

    # 显示表
    def list_all(self, mds):
        return mds.query.order_by().all()

    # 查询记录
    def get_rd(self, mds, sd):
        return mds.query.get(sd)


