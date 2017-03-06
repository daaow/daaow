from cumtbscore import Score


def create_stu(student_id, pswd, user_type="学生", display=False):
    stu = Score(student_id, pswd, user_type=user_type, display=display)
    return stu
