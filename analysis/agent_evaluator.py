class AgentEvaluator:
    def evaluate(self, context):

        print("\n========== PIPELINE EVALUATION ==========")

        if context.dataset_profile:
            print("\nDataset Profile OK")

        if context.column_intelligence:
            print("\nColumn Intelligence:")
            print(context.column_intelligence)

        if context.insights:
            print("\nDiscovered Insights:")
            for insight in context.insights:
                print("-", insight)

        if context.hypotheses:
            print("\nGenerated Hypotheses:")
            for h in context.hypotheses:
                print("-", h)

        if context.evidence:
            print("\nEvidence Summary:")
            print(context.evidence)

        print("\n=========================================\n")
