from .. import utility
import json


class GoodsPromotiongoodsinfoQuery:
    def __init__(self, skuIds):
        self.skuIds = skuIds
        self.method = 'jd.union.open.goods.promotiongoodsinfo.query'

    def perform(self):
        return utility.get(method = self.method, param_json = json.dumps({'skuIds': self.skuIds}))
