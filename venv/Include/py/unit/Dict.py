class Dict(object):

    def __init__(self,**kw):
        super.__init__(**kw)

    @property
    def attr(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('Dict object has no attr %s' % key)

    @attr.setter
    def attr(self,key,value):
        self[key]=value


        

