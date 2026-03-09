from agents.base_agent import BaseAgent


class TrendAgent(BaseAgent):
    def __init__(self):
        super().__init__("TrendAnalysisAgent")

    def run(self, context):

        df = context.dataframe

        trends = {}

        if "revenue" in df.columns:
            grouped = df.groupby(df.columns[0])["revenue"].sum()

            for key, value in grouped.items():
                trends[key] = value

        print("Detected Trends:", trends)

        context.revenue_trends = trends

        return context
