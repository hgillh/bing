'''view bing app
'''
import uuid
from datetime import datetime

from django.shortcuts import render

from bingapp.models import BingSearch
from bingapp.bing_handler import BingHelper
from time import sleep

BingSearch.create_table(read_capacity_units=50, write_capacity_units=50)


def home(request):
    '''method to render home page

    Args:
        request ([object]): http request object
    '''

    return render(request, 'home.html', {})


def search(request):
    '''method to render search page and get bing results

    Args:
        request ([object]): http request object
    '''
    keyword = request.GET.get('keyword', None)
    data_list = []
    if keyword:
        uid = uuid.uuid4().hex
        obj_bh = BingHelper()
        result = obj_bh.bing_search(keyword)
        for dataset in result['webPages']['value']:

            bing_search = BingSearch(uid, url_id=dataset['id'], url=dataset['url'],
                                     name=dataset['name'], snippet=dataset['snippet'],
                                     crawled_date=dataset['dateLastCrawled'],
                                     keyword=keyword, created_at=str(datetime.now()))

            # Save results in DynamoDB
            bing_search.save()
            data_list.append({
                'uid': uid,
                'url': dataset['url'],
                'keyword': keyword,
                'name': dataset['name'],
                'crawled_date': dataset['dateLastCrawled']
            })

    return render(request, 'search.html', {
        'data_list': data_list
    })


def search_list(request):
    '''method to render serve saved results

    Args:
        request ([object]): http request object
    '''

    data_list = BingSearch.scan()
    return render(request, 'records.html', {
        'data_list': data_list
    })


def get_details(request):
    '''method to get detail of single record

    Args:
        request ([object]): http request object
    '''
    result_set = {}
    uid = request.GET.get('uid', None)
    for result in BingSearch.query(uid):
        for key, val in result.__dict__['attribute_values'].items():
            result_set.update({key: val})
    return render(request, 'record_detail.html', {
        'result_set': result_set
    })
