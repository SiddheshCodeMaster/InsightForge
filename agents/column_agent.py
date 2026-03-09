import pandas as pd
from agents.base_agent import BaseAgent


class ColumnIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("ColumnIntelligenceAgent")

    def run(self, context):

        df = context.dataframe

        numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
        text_columns = df.select_dtypes(include=["object"]).columns.tolist()
        datetime_columns = []

        for col in df.columns:
            try:
                pd.to_datetime(df[col])
                datetime_columns.append(col)
            except:
                pass

        intelligence = {
            "numeric_columns": numeric_columns,
            "text_columns": text_columns,
            "datetime_columns": datetime_columns,
        }

        print("\nColumn Intelligence:")
        print(intelligence)

        context.column_intelligence = intelligence

        return context
