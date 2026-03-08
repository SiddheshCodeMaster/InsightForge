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
        """
        Runs the agents sequentially.
        """
        for agent in self.agents:
            print(f"\n Running {agent.name}...")
            result = agent.run(context)

            if isinstance(result, dict):
                context.update(result)

        return context
