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

def weighted_average(lessons):
    filter_cet = filter(lambda x: len(x) > 7, lessons)#剔除四六级
    scores = [[item[4], item[7]] for item in filter_cet]#成绩学分二维数组
    _lst = map(lambda x: float(x[0]) * float(x[1]), scores)
    _tmp = map(lambda x: float(x[0]), scores)
    return sum(_lst) / sum(_tmp)
