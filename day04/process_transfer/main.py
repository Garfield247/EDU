import time
from datetime import datetime
import threading
from utils.rw_redis import RW_redis
from utils.transfer import Transfer
from utils.process_data import Process_data

tra = Transfer()
pre = Process_data()


class myThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.redis_db = RW_redis()
        self.conn = tra.gen_connect()

    def run(self):
        while True:
            while self.redis_db.get_data_count() > 0:
                obj = self.redis_db.get_data()
                if obj:
                    data = pre.process_data(obj)
                    print(data)
                    try:
                        tra.send_item(self.conn,data)
                    except Exception as e:
                        self.redis_db.write_data(obj)
                        if self.conn:
                            self.conn.close()
                        self.conn = tra.gen_connect()
            time.sleep(360)



if __name__ == '__main__':

    for t in [myThread(i) for i in range(2)]:
        t.start()