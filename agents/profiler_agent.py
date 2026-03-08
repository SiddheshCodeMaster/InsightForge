import pandas as pd
from agents.base_agent import BaseAgent


class ProfilerAgent(BaseAgent):
    def __init__(self):
        super().__init__("DataProfilerAgent")

    def run(self, context):
        dataset_path = context.get("dataset_path")
        df = pd.read_csv(dataset_path)

        profile = {
            "num_rows": len(df),
            "num_columns": len(df.columns),
            "columns": list(df.columns),
            "missing_values": df.isna().sum().to_dict(),
        }

        print("Dataset profile: ", profile)

        return {"dataset_profile": profile, "dataframe": df}
