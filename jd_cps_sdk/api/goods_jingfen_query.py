from .. import utility
import json

class GoodsJingfenQuery:
    def __init__(self, eliteId, pageIndex = 1, pageSize = 20, sortName = 'price', sort = 'desc'):
        self.eliteId = eliteId
        self.pageIndex = pageIndex
        self.pageSize = pageSize
        self.sortName = sortName
        self.sort = sort
        self.method = 'jd.union.open.goods.jingfen.query'

    def perform(self):
        return utility.get(method = self.method,
          param_json=json.dumps({"goodsReq": { 'eliteId': self.eliteId, 'pageIndex': self.pageIndex,
            'pageSize': self.pageSize, 'sortName': self.sortName, 'sort': self.sort}}))
