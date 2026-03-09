class AgentGraph:
    """
    Simple agent orchestration graph.
    Runs agents sequentially while passing shared context.
    """

    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def run(self, context):

        for agent in self.agents:
            print(f"\nRunning {agent.name}...")

            context = agent.run(context)

        return context
