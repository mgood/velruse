"""Error generation and handling"""

ERROR_CODES = {
    0: 'Missing parameter',
    1: 'Error processing authentication credentials',
    2: 'Verification of credentials failed',
    3: 'Network error',
    4: 'Application verification failed',
}

def error_string(error_code):
    """Generates an Error string suitable for storing in a
    key/value store using simplejson"""
    err = {'status': 'fail'}
    err['reason'] = {'code': error_code, 
                     'description': ERROR_CODES[error_code]}
    return json.dumps(err)

# Avoid circular dependeny prob
from velruse.utils import json
