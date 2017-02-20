import pymongo
from scrapy.conf import settings


class YouyuanPipeline(object):
    def __init__(self):
        self.host = settings['MONGODB_HOST']
        self.port = settings["MONGODB_PORT"]
        self.dbname = settings["MONGODB_DBNAME"]
        self.sheetname = settings["MONGODB_SHEETNAME"]
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.mydb = self.client["youyuan"]
        self.sheet = self.mydb["youyuanwang"]


    def process_item(self, item, spider):

        data = dict(item)
        self.sheet.insert(data)
        return item