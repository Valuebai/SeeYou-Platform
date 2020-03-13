import requests
import json
from sklearn.metrics.pairwise import cosine_similarity

class Nlper:

    def __init__(self, bert_client):
        self.bert_client = bert_client

    def get_text_similarity(self, base_text, compared_text):
        tensors = self.bert_client.encode([base_text,compared_text])
        print('2个文本相似度为：',cosine_similarity(tensors)[0][1])
        return cosine_similarity(tensors)[0][1]

    @staticmethod
    # 翻译函数，word 需要翻译的内容
    def translate(word):
        # 有道词典 api
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        # 传输的参数，其中 i 为需要翻译的内容
        key = {
            'type': "AUTO",
            'i': word,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON",
            "typoResult": "true"
        }
        # key 这个字典为发送给有道词典服务器的内容
        response = requests.post(url, data=key)
        # 判断服务器是否相应成功
        if response.status_code == 200:
            # 然后相应的结果
            return json.loads(response.text)['translateResult'][0][0]['tgt']
        else:
            print("有道词典调用失败")
            # 相应失败就返回空
            return None


if __name__ == '__main__':
    from app import nlper
    r = nlper.get_text_similarity('美国','中国')
    print(r)



