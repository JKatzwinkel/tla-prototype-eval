from elasticsearch import Elasticsearch

es = Elasticsearch('http://127.0.0.1:9200')


def search_lemma(query, size=100, offset=0):
    """ """
    res = es.search(index='lemma', doc_type='lemma', q=query, size=size, from_=offset)
    return res.get('hits', {})


def get(index, _id):
    """ retrieve document with given id from given index assuming its doctype is same as index. """
    res = es.search(index=index, doc_type=index, q='_id:{}'.format(_id))
    if res.get('hits', {}).get('total', 0) == 1:
        return res.get('hits', {}).get('hits', [])[0].get('_source')
    

