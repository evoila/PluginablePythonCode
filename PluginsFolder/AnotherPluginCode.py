from PluginableCode import AbstractClass

class AnotherImplementationOfAbstractClass(AbstractClass):
    
    _a = None
    
    def doSomething(self):
        print "something else" 
    
    def getA(self):
        return self._a

    def setA(self, a):
        self._a = a
        
    a = property(getA, setA)