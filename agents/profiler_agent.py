import pandas as pd
from agents.base_agent import BaseAgent

import pandas as pd
from agents.base_agent import BaseAgent


class ProfilerAgent(BaseAgent):
    def __init__(self):
        super().__init__("DataProfilerAgent")

    def run(self, context):

        df = pd.read_csv(context.dataset_path)

        profile = {
            "num_rows": len(df),
            "num_columns": len(df.columns),
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
        }

        print("Dataset Profile:", profile)

        context.dataset_profile = profile
        context.dataframe = df

        return context
