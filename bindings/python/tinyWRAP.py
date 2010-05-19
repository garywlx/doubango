# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.39
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        try:
            fp, pathname, description = imp.find_module('_tinyWRAP', [dirname(__file__)])
            _mod = imp.load_module('_tinyWRAP', fp, pathname, description)
        finally:
            if fp is not None: fp.close()
        return _mod
    _tinyWRAP = swig_import_helper()
    del swig_import_helper
else:
    import _tinyWRAP
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


class SipUri(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SipUri, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SipUri, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _tinyWRAP.new_SipUri(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tinyWRAP.delete_SipUri
    __del__ = lambda self : None;
    def isValid(self, *args): return _tinyWRAP.SipUri_isValid(self, *args)
SipUri_swigregister = _tinyWRAP.SipUri_swigregister
SipUri_swigregister(SipUri)

class SipEvent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SipEvent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SipEvent, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _tinyWRAP.new_SipEvent()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tinyWRAP.delete_SipEvent
    __del__ = lambda self : None;
    def getCode(self): return _tinyWRAP.SipEvent_getCode(self)
    def getPhrase(self): return _tinyWRAP.SipEvent_getPhrase(self)
    def getBaseSession(self): return _tinyWRAP.SipEvent_getBaseSession(self)
SipEvent_swigregister = _tinyWRAP.SipEvent_swigregister
SipEvent_swigregister(SipEvent)

class SipSession(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SipSession, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SipSession, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _tinyWRAP.new_SipSession(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tinyWRAP.delete_SipSession
    __del__ = lambda self : None;
    def addHeader(self, *args): return _tinyWRAP.SipSession_addHeader(self, *args)
    def removeHeader(self, *args): return _tinyWRAP.SipSession_removeHeader(self, *args)
    def addCaps(self, *args): return _tinyWRAP.SipSession_addCaps(self, *args)
    def removeCaps(self, *args): return _tinyWRAP.SipSession_removeCaps(self, *args)
    def setExpires(self, *args): return _tinyWRAP.SipSession_setExpires(self, *args)
    def setFromUri(self, *args): return _tinyWRAP.SipSession_setFromUri(self, *args)
    def setToUri(self, *args): return _tinyWRAP.SipSession_setToUri(self, *args)
    def setPayload(self, *args): return _tinyWRAP.SipSession_setPayload(self, *args)
SipSession_swigregister = _tinyWRAP.SipSession_swigregister
SipSession_swigregister(SipSession)

class RegistrationEvent(SipEvent):
    __swig_setmethods__ = {}
    for _s in [SipEvent]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RegistrationEvent, name, value)
    __swig_getmethods__ = {}
    for _s in [SipEvent]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, RegistrationEvent, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _tinyWRAP.new_RegistrationEvent()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tinyWRAP.delete_RegistrationEvent
    __del__ = lambda self : None;
    def getType(self): return _tinyWRAP.RegistrationEvent_getType(self)
    def getSession(self): return _tinyWRAP.RegistrationEvent_getSession(self)
RegistrationEvent_swigregister = _tinyWRAP.RegistrationEvent_swigregister
RegistrationEvent_swigregister(RegistrationEvent)

class RegistrationSession(SipSession):
    __swig_setmethods__ = {}
    for _s in [SipSession]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RegistrationSession, name, value)
    __swig_getmethods__ = {}
    for _s in [SipSession]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, RegistrationSession, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _tinyWRAP.new_RegistrationSession(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tinyWRAP.delete_RegistrationSession
    __del__ = lambda self : None;
    def Register(self): return _tinyWRAP.RegistrationSession_Register(self)
    def UnRegister(self): return _tinyWRAP.RegistrationSession_UnRegister(self)
RegistrationSession_swigregister = _tinyWRAP.RegistrationSession_swigregister
RegistrationSession_swigregister(RegistrationSession)

class SubscriptionEvent(SipEvent):
    __swig_setmethods__ = {}
    for _s in [SipEvent]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SubscriptionEvent, name, value)
    __swig_getmethods__ = {}
    for _s in [SipEvent]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, SubscriptionEvent, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _tinyWRAP.new_SubscriptionEvent()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tinyWRAP.delete_SubscriptionEvent
    __del__ = lambda self : None;
    def getType(self): return _tinyWRAP.SubscriptionEvent_getType(self)
    def getSession(self): return _tinyWRAP.SubscriptionEvent_getSession(self)
SubscriptionEvent_swigregister = _tinyWRAP.SubscriptionEvent_swigregister
SubscriptionEvent_swigregister(SubscriptionEvent)

class SubscriptionSession(SipSession):
    __swig_setmethods__ = {}
    for _s in [SipSession]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SubscriptionSession, name, value)
    __swig_getmethods__ = {}
    for _s in [SipSession]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, SubscriptionSession, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _tinyWRAP.new_SubscriptionSession(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tinyWRAP.delete_SubscriptionSession
    __del__ = lambda self : None;
    def Subscribe(self): return _tinyWRAP.SubscriptionSession_Subscribe(self)
    def UnSubscribe(self): return _tinyWRAP.SubscriptionSession_UnSubscribe(self)
SubscriptionSession_swigregister = _tinyWRAP.SubscriptionSession_swigregister
SubscriptionSession_swigregister(SubscriptionSession)

class SipCallback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SipCallback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SipCallback, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == SipCallback:
            _self = None
        else:
            _self = self
        this = _tinyWRAP.new_SipCallback(_self, )
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tinyWRAP.delete_SipCallback
    __del__ = lambda self : None;
    def OnRegistrationChanged(self, *args): return _tinyWRAP.SipCallback_OnRegistrationChanged(self, *args)
    def OnSubscriptionChanged(self, *args): return _tinyWRAP.SipCallback_OnSubscriptionChanged(self, *args)
    def __disown__(self):
        self.this.disown()
        _tinyWRAP.disown_SipCallback(self)
        return weakref_proxy(self)
SipCallback_swigregister = _tinyWRAP.SipCallback_swigregister
SipCallback_swigregister(SipCallback)

class SafeObject(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SafeObject, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SafeObject, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _tinyWRAP.new_SafeObject()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tinyWRAP.delete_SafeObject
    __del__ = lambda self : None;
    def Lock(self): return _tinyWRAP.SafeObject_Lock(self)
    def UnLock(self): return _tinyWRAP.SafeObject_UnLock(self)
SafeObject_swigregister = _tinyWRAP.SafeObject_swigregister
SafeObject_swigregister(SafeObject)

class SipStack(SafeObject):
    __swig_setmethods__ = {}
    for _s in [SafeObject]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SipStack, name, value)
    __swig_getmethods__ = {}
    for _s in [SafeObject]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, SipStack, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _tinyWRAP.new_SipStack(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tinyWRAP.delete_SipStack
    __del__ = lambda self : None;
    def start(self): return _tinyWRAP.SipStack_start(self)
    def setRealm(self, *args): return _tinyWRAP.SipStack_setRealm(self, *args)
    def setIMPI(self, *args): return _tinyWRAP.SipStack_setIMPI(self, *args)
    def setIMPU(self, *args): return _tinyWRAP.SipStack_setIMPU(self, *args)
    def setPassword(self, *args): return _tinyWRAP.SipStack_setPassword(self, *args)
    def setProxyCSCF(self, *args): return _tinyWRAP.SipStack_setProxyCSCF(self, *args)
    def setLocalIP(self, *args): return _tinyWRAP.SipStack_setLocalIP(self, *args)
    def setLocalPort(self, *args): return _tinyWRAP.SipStack_setLocalPort(self, *args)
    def addHeader(self, *args): return _tinyWRAP.SipStack_addHeader(self, *args)
    def removeHeader(self, *args): return _tinyWRAP.SipStack_removeHeader(self, *args)
    def addDnsServer(self, *args): return _tinyWRAP.SipStack_addDnsServer(self, *args)
    def isValid(self): return _tinyWRAP.SipStack_isValid(self)
    def stop(self): return _tinyWRAP.SipStack_stop(self)
SipStack_swigregister = _tinyWRAP.SipStack_swigregister
SipStack_swigregister(SipStack)

tsip_event_invite = _tinyWRAP.tsip_event_invite
tsip_event_message = _tinyWRAP.tsip_event_message
tsip_event_options = _tinyWRAP.tsip_event_options
tsip_event_publish = _tinyWRAP.tsip_event_publish
tsip_event_register = _tinyWRAP.tsip_event_register
tsip_event_subscribe = _tinyWRAP.tsip_event_subscribe
tsip_event_dialog = _tinyWRAP.tsip_event_dialog
tsip_i_register = _tinyWRAP.tsip_i_register
tsip_ai_register = _tinyWRAP.tsip_ai_register
tsip_o_register = _tinyWRAP.tsip_o_register
tsip_ao_register = _tinyWRAP.tsip_ao_register
tsip_i_unregister = _tinyWRAP.tsip_i_unregister
tsip_ai_unregister = _tinyWRAP.tsip_ai_unregister
tsip_o_unregister = _tinyWRAP.tsip_o_unregister
tsip_ao_unregister = _tinyWRAP.tsip_ao_unregister
tsip_i_subscribe = _tinyWRAP.tsip_i_subscribe
tsip_ai_subscribe = _tinyWRAP.tsip_ai_subscribe
tsip_o_subscribe = _tinyWRAP.tsip_o_subscribe
tsip_ao_subscribe = _tinyWRAP.tsip_ao_subscribe
tsip_i_unsubscribe = _tinyWRAP.tsip_i_unsubscribe
tsip_ai_unsubscribe = _tinyWRAP.tsip_ai_unsubscribe
tsip_o_unsubscribe = _tinyWRAP.tsip_o_unsubscribe
tsip_ao_unsubscribe = _tinyWRAP.tsip_ao_unsubscribe
tsip_i_notify = _tinyWRAP.tsip_i_notify
tsip_ai_notify = _tinyWRAP.tsip_ai_notify
tsip_o_notify = _tinyWRAP.tsip_o_notify
tsip_ao_notify = _tinyWRAP.tsip_ao_notify


