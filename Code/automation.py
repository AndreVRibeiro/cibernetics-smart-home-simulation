class AutomationTime:
    def __init__(self, when, do, state):
        self.when = when
        self.do = do
        self.state = state


class AutomationDevice:
    def __init__(self, when, state1, do, state2):
        self.when = when
        self.state1 = state1
        self.do = do
        self.state2 = state2


class AutomationSensor:
    def __init__(self, when, do, state):
        self.when = when
        self.do = do
        self.state = state






