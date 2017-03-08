from cumtbscore import Score


def create_stu(student_id, pswd, user_type="学生", display=False):
    stu = Score(student_id, pswd, user_type=user_type, display=display)
    return stu

def info_to_json(info):
    info_json = {}
    info_json['name'] = info.get("a.姓名")
    info_json['college'] = info.get("e.院系")
    info_json['class'] = info.get("d.班级")
    info_json['student_id'] = info.get("c.学号")
    info_json['idcard'] = info.get("b.身份证号")
    return info_json

