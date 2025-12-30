from flask_restful import Resource
from flask import request

class Items(Resource):
    # GET /items
    def get(self):                                                
        return {'message': '讀取所有資料'}, 200
    # POST /items
    def post(self):    
        data = request.get_json()   #接收client端傳過來的json資料
                                          
        return {'message': f'新增{data["name"]},{data["email"]}'}, 201

class Item(Resource):
    # GET /items/<id> 
    def get(self, id):                                             
        return {'message': f'根據{id}讀取資料'}, 200
    # PUT /items/<id>
    def put(self, id):     
        data = request.get_json ()                                          
        return {'message': f'根據{id}修改{data["name"]}'}, 200  
    # DELETE /items/<id> 
    def delete(self, id):                                      
        return {'message': f'根據{id}刪除資料'},200
