from elasticsearch import Elasticsearch

es = Elasticsearch('http://127.0.0.1:9200')


def lucenify(params):
    """ return a string that can be used as a lucene query """
    return ' '.join(['{}:{}'.format(k, v) for k, v in params.items()])


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
    """ performs a search on the given index for documents of the same doc_type as
    the given index and applying a given lucene query. """
    res = es.search(index=index, doc_type=index, q=query, size=size, from_=offset)
    return res.get('hits', {})


def get(index, _id):
    """ retrieve document with given id from given index assuming its doctype is the
    same as index. """
    res = es.get(index, index, _id)
    if res:
        return res.get('_source')


def resolve_name(index, _id=None, obj=None):
    """ takes either an object or an object id to be looked up in a given index and extracts the name field. """
    obj = obj or get(index, _id)
    if obj:
        return obj.get('name')
    else:
        print('obj id does not exist: {}'.format(_id))
        return _id



