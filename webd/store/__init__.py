from os import environ as env

from elasticsearch import (
    Elasticsearch,
    helpers,
)

es = Elasticsearch(
    env.get('ES_URL', 'http://localhost:9200')
)

def lucenify(params):
    """ return a string that can be used as a lucene query """
    return ' '.join(['{}:{}'.format(k, v) for k, v in params.items()])


def hits_contents(hits):
    """ extracts the _source objects from elasticsearch search result hit list,
    after copying each hit's _score field into the wrapped _source object. """
    for hit in hits.get('hits', []):
        hit['_source'] = {
            **hit.get('_source'),
            'score': hit.get('_score'),
            'id': hit.get('_id'),
        }
    return [hit.get('_source') for hit in hits.get('hits', [])]



def obj_revision_date(obj):
    """ extract latest revision from (json) object """
    return obj.get('revisions', [])[-1].split('@')[1]


def pagination(page, size, hits):
    """ generates a paginatino object for template use """
    # FIXME move this to seperate presentation module
    pagination_ = {"page": page,
                   "size": size,
                   "count": hits,
                   "offset": size * (page-1),
                   "max_offset": min(size * page, hits)}
    if page > 1:
        pagination_["prev"] = page - 1
        if page > 2:
            pagination_["first"] = 1
    last = hits // size + int(hits % size > 0)
    if page < last:
        pagination_["next"] = page + 1
        if page < last - 1:
            pagination_["last"] = last
    return pagination_


def search(index, query, size=100, offset=0):
    """ performs a search on the given index for documents of the same doc_type
    as the given index and applying a given lucene query. """
    if type(query) is str:
        try:
            res = es.search(
                index=index,
                doc_type=index,
                q=query,
                size=size,
                from_=offset
            )
        except TypeError:
            res = es.search(
                index=index,
                q=query,
                size=size,
                from_=offset
            )
    else:
        res = es.search(
            index=index,
            body=query,
            size=size,
            from_=offset
        )
    return res.get('hits', {})


def get(index, _id):
    """ retrieve document with given id from given index assuming its doctype
    is the same as index.

    .. warn:: does not work for elasticsearch 7
    """
    try:
        res = es.get(
            index=index,
            doc_type=index,
            id=_id,
        )
        if res:
            return res.get('_source')
    except:
        pass


def resolve_name(index, _id=None, obj=None):
    """ takes either an object or an object id to be looked up in a given index and extracts the name field. """
    obj = obj or get(index, _id)
    if obj:
        return obj.get('name')
    else:
        print('obj id does not exist: {}'.format(_id))
        return _id


def get_mappings(index):
    """ extract indexed features from a certain index's mappings

    :rtype: list
    """
    try:
        mappings = es.indices.get_mapping(index).get(index, {}).get('mappings', {}).get(index)
    except:
        return []
    def extract_properties(obj):
        res = []
        if obj is None:
            return res
        for key, values in obj.items():
            if type(values) is dict:
                if key == "properties":
                    return extract_properties(values)
                elif "type" in values and type(values["type"]) is not dict:
                    res.append(key)
                else:
                    res.extend(
                        [
                            '{}.{}'.format(key, remainder)
                            for remainder in extract_properties(values)
                        ]
                    )
        return res
    properties = extract_properties(mappings)
    return properties


def scroll(index, query):
    return helpers.scan(
        es,
        query=query,
        index=index,
        doc_type=index,
    )
