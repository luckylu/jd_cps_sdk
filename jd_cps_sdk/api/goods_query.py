from .. import utility
import json

class GoodsQuery:
    def __init__(self, keyword, pageIndex = 1, pageSize = 20, sortName = 'price', sort = 'desc'):
        self.keyword = keyword
        self.pageIndex = pageIndex
        self.pageSize = pageSize
        self.sortName = sortName
        self.sort = sort
        self.method = 'jd.union.open.goods.query'

    def perform(self):
        return utility.get(method = self.method,
          param_json=json.dumps({"goodsReqDTO": { 'keyword': self.keyword, 'pageIndex': self.pageIndex,
            'pageSize': self.pageSize, 'sortName': self.sortName, 'sort': self.sort}}))
