import os
import matplotlib.pyplot as plt
import seaborn as sns

from agents.base_agent import BaseAgent


class VisualizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("VisualizationAgent")

    def run(self, context):

        df = context.dataframe
        intelligence = context.column_intelligence

        numeric_cols = intelligence.get("numeric_columns", [])
        text_cols = intelligence.get("text_columns", [])

        os.makedirs("outputs/charts", exist_ok=True)

        # Numeric distributions
        for col in numeric_cols:
            plt.figure()
            sns.histplot(df[col])
            plt.title(f"Distribution of {col}")
            plt.savefig(f"outputs/charts/{col}_distribution.png")
            plt.close()

        # Categorical counts
        for col in text_cols[:3]:  # limit to first few
            plt.figure()
            df[col].value_counts().head(10).plot(kind="bar")
            plt.title(f"Top categories in {col}")
            plt.savefig(f"outputs/charts/{col}_categories.png")
            plt.close()

        print("\nCharts saved to outputs/charts")

        return context
