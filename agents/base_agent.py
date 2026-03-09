class BaseAgent:
    """
    Base class for all agents.
    """

    def __init__(self, name):
        self.name = name

    def run(self, context):
        raise NotImplementedError
