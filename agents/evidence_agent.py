import pandas as pd
from agents.base_agent import BaseAgent


class EvidenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("EvidenceAgent")

    def run(self, context):

        df = context.dataframe
        intelligence = context.column_intelligence
        hypotheses = context.hypotheses

        numeric_cols = intelligence.get("numeric_columns", [])

        evidence_results = {}

        if len(numeric_cols) >= 2:
            corr_matrix = df[numeric_cols].corr()

            evidence_results["correlation_matrix"] = corr_matrix.to_dict()

            print("\nCorrelation Matrix:")
            print(corr_matrix)

        else:
            evidence_results["note"] = (
                "Not enough numeric columns for correlation analysis"
            )

        context.evidence = evidence_results

        return context
