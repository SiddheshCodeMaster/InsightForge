import sys
from pathlib import Path
from models.context_schema import AnalysisContext
from orchestrator.agent_graph import AgentGraph

from agents.profiler_agent import ProfilerAgent
from agents.trend_agent import TrendAgent
from agents.rootcause_agent import RootCauseAgent

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))


def main():

    graph = AgentGraph()

    graph.add_agent(ProfilerAgent())
    graph.add_agent(TrendAgent())
    graph.add_agent(RootCauseAgent())

    context = AnalysisContext(dataset_path="datasets/sample-dataset.csv")

    result = graph.run(context)

    print("\nFinal Analysis Context:")
    print(result)


if __name__ == "__main__":
    main()
