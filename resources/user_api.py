from flask_restful import Resource

class Users(Resource):
    # 讀取所有資料
    def get(self):
        return {"users":"所有使用者"},200

    def post(self):
        return {"users":"新增使用者"},200

# GET http://127.0.0.1/api/users/8
class User(Resource):
    # 根據 user id 讀取資料
    def get(self, user_id):
        return {"users":user_id},200

    def put(self, user_id):
        return {"users修改":user_id},200

    def delete(self, user_id):
        return {"users刪除":user_id},200