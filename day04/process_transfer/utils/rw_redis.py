# -*- coding: utf-8 -*-
import redis
import json
from process_transfer.utils.config import REDIS_HOST, REDIS_PORT, REDIS_KEY_DATA


class RW_redis(object):
    def __init__(self):
        self.redis_cli = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
        self.key = REDIS_KEY_DATA

    def get_data_count(self):
        # 获取data的数量
        try:
            # print(self.key)
            count = self.redis_cli.llen(self.key)
            print(count)
            return count
        except:
            return 0

    def get_data(self):
        # 从左端出队一条数据
        json_obj = self.redis_cli.lpop(self.key)
        if json_obj:
            data = json.loads(json_obj)
            # print(data)
            return data
        else:
            return None

    def write_data(self, item):
        data = json.dumps(item)
        self.redis_cli.rpush(self.key, data)

# r = RW_redis()
# r.get_data()