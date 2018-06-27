from elasticsearch import Elasticsearch

es = Elasticsearch('http://127.0.0.1:9200')

def get_lemma(_id):
    """ """
    res = es.search(index='lemma', doc_type='lemma', q='_id:{}'.format(_id))
    if res.get('hits', {}).get('total', 0) == 1:
        return res.get('hits', {}).get('hits', {})[0].get('_source')


