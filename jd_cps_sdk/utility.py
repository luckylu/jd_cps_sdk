import hashlib
import requests
import json
from datetime import datetime
from .config import Config

def sign(**kw):
    print(kw)
    sorted_params = dict(sorted(kw.items()))
    flatten_params = "%s%s%s" % ( Config.get_instance().app_secret,
                                 str().join("%s%s" % (key, val) for (key,val) in sorted_params.items()),
                                 Config.get_instance().app_secret
                                 )
    sign = hashlib.md5(flatten_params.encode('utf-8')).hexdigest().upper()
    return sign

def get(**params):
    url = 'https://router.jd.com/api'
    params.update(timestamp = datetime.now().strftime( '%Y-%m-%d %H:%M:%S' ),
      format = 'json', v = '1.0', sign_method = 'md5', app_key = Config.get_instance().app_key)
    sign_str = sign(**params)
    params.update(sign = sign_str)
    r = requests.get(url, params = params)
    return json.loads(r.text)

