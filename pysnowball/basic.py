import json
import os
from pysnowball import api_ref
from pysnowball import utls

def list_stock():
    url = api_ref.stock_list_shsz
    return utls.fetch_without_token(url)