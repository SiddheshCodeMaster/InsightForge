import pandas as pd
from agents.base_agent import BaseAgent


class InsightDiscoveryAgent(BaseAgent):
    def __init__(self):
        super().__init__("InsightDiscoveryAgent")

    def run(self, context):

        df = context.dataframe
        intelligence = context.column_intelligence

        insights = []

        numeric_cols = intelligence.get("numeric_columns", [])
        text_cols = intelligence.get("text_columns", [])

        # Numeric insights
        for col in numeric_cols:
            mean_val = df[col].mean()
            std_val = df[col].std()

            insights.append(
                f"{col} has mean {round(mean_val, 2)} and standard deviation {round(std_val, 2)}"
            )

        # Categorical dominance
        for col in text_cols[:3]:
            top = df[col].value_counts().iloc[0]
            total = len(df)

            ratio = round((top / total) * 100, 2)

            insights.append(
                f"Category '{col}' has dominant value representing {ratio}% of dataset"
            )

        print("\nInsight Discovery:")
        for i in insights:
            print("-", i)

        context.insights = insights

        return context
