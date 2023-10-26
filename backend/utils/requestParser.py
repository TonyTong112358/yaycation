import json

from exceptions import inputExceptions

def validate_post_field(body,requirements = None):
    '''
    A simple functionm to detemine if the parameters in body are all fullfiled
    
    '''
    if requirements is None:
        requirements = {}

    #body: is either of type binary or of type dictionary
    # the request call was through a raw json file as django converts those into bytes
    
    if isinstance(body,bytes):
        
        body = json.loads(body.decode('utf-8'))
    body = dict(body)
    keys = set(body.keys())
    for required in requirements:
        if required not in keys:
            raise inputExceptions.invalidJsonFormatException

    return body





