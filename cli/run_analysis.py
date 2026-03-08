import sys
from pathlib import Path
from orchestrator.agent_graph import AgentGraph
from agents.profiler_agent import ProfilerAgent

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))


def main():

    graph = AgentGraph()

    graph.add_agent(ProfilerAgent())

    context = {"dataset_path": "datasets/sample-dataset.csv.csv"}

    result = graph.run(context)

    print("\nFinal Context:")
    print(result)


if __name__ == "__main__":
    main()
