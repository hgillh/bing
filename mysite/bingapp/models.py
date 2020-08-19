'''model of bing search
'''
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from mysite.settings import DYNAMO_DB_HOST, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME


class BingSearch(Model):

    class Meta:
        '''meta class
        '''
        table_name = "bing_search"
        host = DYNAMO_DB_HOST
        aws_access_key_id = AWS_ACCESS_KEY_ID
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        region_name = REGION_NAME

    uid = UnicodeAttribute(hash_key=True)
    url_id = UnicodeAttribute(range_key=True)
    url = UnicodeAttribute()
    name = UnicodeAttribute()
    snippet = UnicodeAttribute()
    crawled_date = UnicodeAttribute()
    keyword = UnicodeAttribute()
    created_at = UnicodeAttribute()
