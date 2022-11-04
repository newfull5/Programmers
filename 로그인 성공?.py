def solution(id_pw, db):
    id_list = [(id) for id, pw in db]
    id, pw = id_pw
    for i in range(len(id_list)):
        if id_list[i] == id:
            if db[i][-1] == pw:
                return 'login'
            return 'wrong pw'
    return 'fail'
