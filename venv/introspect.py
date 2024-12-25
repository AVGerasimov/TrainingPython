import inspect

def introspection_info(obj):
    descript = {}
    descript =dict(type = type(obj), attribute = getattr(obj, 'intt', 'fault'), methods = getattr(obj,
    'showattr', 'fault'),  module = obj.__module__, name = obj.__name__, )
    return descript

class tst:
    intt = 12
    def showattr():
        print(f'intt = {intt}')
    pass


number_info = introspection_info(tst)
print(number_info)
