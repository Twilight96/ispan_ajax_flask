from flask_restful import Resource
from flask import request
from sqlalchemy import or_, desc, asc, func
from models import db
from models.category_model import SpotsCategory
from models.spot_model import Spot

class Spots(Resource):
    def get(self):
        # 1. 取得 QueryString 參數
        keyword = request.args.get('keyword', '').strip()
        category_id = request.args.get('category_id')
        page = int(request.args.get('page', 1))
        per_page = max(3, min(int(request.args.get('per_page', 9)), 45))
        sort_by = request.args.get('sort_by', 'SpotId')
        sort_order = request.args.get('sort_order', 'asc').lower()

        # 2. 驗證與設定動態排序
        valid_sort_fields = {'SpotId': Spot.SpotId, 'SpotTitle': Spot.SpotTitle, 'CategoryId': Spot.CategoryId}
        sort_column = valid_sort_fields.get(sort_by, Spot.SpotId)
        sort_expr = sort_column.asc() if sort_order == 'asc' else sort_column.desc()

        # 3. 建立查詢基礎 (Query Object)
        query = Spot.query

        # 4. 動態增加篩選條件
        if keyword:
            query = query.filter(
                or_(
                    Spot.SpotTitle.contains(keyword),
                    Spot.SpotDescription.contains(keyword)
                )
            )
        if category_id and category_id != "0":
            query = query.filter(Spot.CategoryId == category_id)

        # 5. 使用 Flask-SQLAlchemy 內建的 paginate 處理分頁 (最推薦的 ORM 做法)
        pagination = query.order_by(sort_expr).paginate(page=page, per_page=per_page, error_out=False)

        # 將物件轉為字典
        data = [{
            "SpotId": s.SpotId,
            "SpotTitle": s.SpotTitle,
            "CategoryId": s.CategoryId,
            "SpotDescription": s.SpotDescription,
            "SpotImage": s.SpotImage,
            "Address": s.Address
            # ... 根據需求列出其他欄位
        } for s in pagination.items]

        return {
            'total_pages': pagination.pages,
            'total_count': pagination.total,
            'data': data
        }, 200

class SpotCategoryStats(Resource):
    def get(self):
        # ORM Join 與 Group By
        results = db.session.query(
            SpotsCategory.CategoryName,
            func.count(Spot.SpotId).label("count")
        ).join(Spot, Spot.CategoryId == SpotsCategory.CategoryId)\
         .group_by(SpotsCategory.CategoryName)\
         .order_by(SpotsCategory.CategoryId).all()

        data = [{"category": row.CategoryName, "count": row.count} for row in results]
        return {"data": data}, 200

class SpotsByDistrict(Resource):
    def get(self):       
        district = request.args.get('district')  
        
        # ORM 篩選特定欄位
        results = Spot.query.with_entities(Spot.SpotTitle, Spot.Longitude, Spot.Latitude)\
                    .filter(Spot.Address.contains(district))\
                    .all()

        data = [
            {
                "title": row.SpotTitle,
                "lng": float(row.Longitude),
                "lat": float(row.Latitude)
            }
            for row in results if row.Longitude and row.Latitude
        ]
        return data, 200

class SpotTitleSearch(Resource):
    def get(self):
        keyword = request.args.get('keyword', '')

        # ORM Like 查詢與限制筆數
        results = Spot.query.filter(Spot.SpotTitle.like(f'%{keyword}%'))\
                    .order_by(Spot.SpotId.asc())\
                    .limit(10).all()

        return [row.SpotTitle for row in results], 200