class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None
        
    def getLabel(self):
        return self.label
        
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output
        
class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        #super(BinaryGate, self).__init__(n)
        
        self.pinA = None
        self.pinB = None
        
    def get_pinA(self):
        return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        
    def get_pinB(self):
        return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        
class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        #super(UnaryGate, self).__init__(n)
        
        self.pin = None
        
    def get_pin(self):
        return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        
        
class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        #super(BinaryGate, self).__init__(self, n)
        
    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        
        if a == 1 and b == 1:
            return 1
        return 0
        
class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        
        tgate.set_next_pin(self)
        
    def get_from(self):
        return self.fromgate
        
    def get_to(self):
        return self.togate
        
    def set_next_pin(self, source):
        if not self.pinA:
            self.pinA = source
        else:
            if not self.pinB:
                self.pinB = source
            else:
                raise RuntimeError("ERROR: No empty pins")