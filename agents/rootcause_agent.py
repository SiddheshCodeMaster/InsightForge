import json
import litellm
from agents.base_agent import BaseAgent


class RootCauseAgent(BaseAgent):
    def __init__(self):
        super().__init__("RootCauseAgent")

    def run(self, context):

        trends = context.revenue_trends
        profile = context.dataset_profile

        prompt = f"""
You are a senior business data analyst.

Dataset profile:
{profile}

Detected trends:
{trends}

Generate 5 possible business hypotheses explaining these trends.

Focus on:
- market factors
- pricing
- product mix
- demand shifts
- operational factors

Return JSON list of hypotheses.
"""

        response = litellm.completion(
            model="ollama/phi3", messages=[{"role": "user", "content": prompt}]
        )

        hypotheses_text = response.choices[0].message.content

        try:
            hypotheses = json.loads(hypotheses_text)
        except:
            hypotheses = [hypotheses_text]

        print("Generated Hypotheses:", hypotheses)

        context.hypotheses = hypotheses

        return context
