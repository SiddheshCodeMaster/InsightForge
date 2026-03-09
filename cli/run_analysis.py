import sys
from pathlib import Path
from models.context_schema import AnalysisContext
from orchestrator.agent_graph import AgentGraph

from agents.profiler_agent import ProfilerAgent
from agents.trend_agent import TrendAgent
from agents.rootcause_agent import RootCauseAgent
from agents.column_agent import ColumnIntelligenceAgent
from agents.evidence_agent import EvidenceAgent
from agents.visualization_agent import VisualizationAgent
from agents.insight_agent import InsightDiscoveryAgent
from analysis.agent_evaluator import AgentEvaluator

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))


def main():

    graph = AgentGraph()

    graph.add_agent(ProfilerAgent())
    graph.add_agent(ColumnIntelligenceAgent())
    graph.add_agent(InsightDiscoveryAgent())
    graph.add_agent(TrendAgent())
    graph.add_agent(RootCauseAgent())
    graph.add_agent(EvidenceAgent())
    graph.add_agent(VisualizationAgent())

    context = AnalysisContext(dataset_path="datasets/sample-dataset.csv")

    result = graph.run(context)
    evaluator = AgentEvaluator()
    evaluator.evaluate(result)


if __name__ == "__main__":
    main()
