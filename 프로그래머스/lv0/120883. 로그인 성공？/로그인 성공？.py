def solution(id_pw, db):
    db_dict = {k:v for k,v in db}
    
    if id_pw[0] in db_dict:
        if id_pw[1] == db_dict[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"