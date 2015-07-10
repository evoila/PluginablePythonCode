import abc
import imp
import inspect
import os

class AbstractClass:
    __metaclass__ = abc.ABCMeta
    def getA(self): pass

    def setA(self, a): pass
    a = abc.abstractproperty(getA, setA)
    
    @abc.abstractmethod
    def doSomething(self): pass

path = "PluginsFolder"
for f in os.listdir(path):
    if f.endswith(".py"):
        moduleName = f[:-3]
        f, filename, desc = imp.find_module(moduleName, [path])
        module = imp.load_module(moduleName, f, filename, desc)
        for member in inspect.getmembers(module):
            if inspect.isclass(member[1]) and not inspect.isabstract(member[1]) and issubclass(member[1], AbstractClass):
                AbstractClass.register(member[1])
                object = member[1]()
                object.a = object.__class__.__name__
                print object.a
                object.doSomething()