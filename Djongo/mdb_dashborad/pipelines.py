import pymongo

class QuotetutorialPipeline(object):
    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost'
            '27017'
        )
        db = self.conn['myquotes']
        self.collection = db['quotes_tb']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
