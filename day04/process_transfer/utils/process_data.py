import json
import re
import jieba
from process_transfer.utils.rw_redis import RW_redis
from process_transfer.utils.word_list import stop_word

r = RW_redis()
data = r.get_data()
class Process_data(object):

    def _load(self,item):
        if type(item) == dict:
            for k in list(item.keys()):
                if item[k]:
                    # 去除转义字符
                    item[k] = re.sub(r'[\r|\n|\t]', '', item[k])
                    # 去除长空格
                    item[k] = re.sub(r'\s{2,}', '', item[k])
                    # # 替换|为-
                    # item[k] = re.sub(r'\|', '-', item[k])
        return item

    def process_data(self,item):
        json_context = self._load(item)
        texts = json_context['info']
        words = []
        for word in jieba.cut(texts):
            if word not in stop_word:
                words.append(word)
        json_context['words'] = words
        new_data = json.dumps(json_context,ensure_ascii=False)
        return new_data

