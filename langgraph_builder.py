import json
from agents.prospect_search import ProspectSearchAgent
from agents.scoring import ScoringAgent
from agents.outreach_content import OutreachContentAgent
from agents.feedback_trainer import FeedbackTrainerAgent

AGENT_MAP = {
    "ProspectSearchAgent": ProspectSearchAgent,
    "ScoringAgent": ScoringAgent,
    "OutreachContentAgent": OutreachContentAgent,
    "FeedbackTrainerAgent": FeedbackTrainerAgent,
}

def run_workflow():
    with open("workflow.json") as f:
        config = json.load(f)

    data_store = {}
    for step in config["steps"]:
        agent_cls = AGENT_MAP[step["agent"]]
        agent = agent_cls(step.get("tools"), step.get("instructions"))

        # Resolve inputs
        inputs = {}
        for key, val in step.get("inputs", {}).items():
            if isinstance(val, str) and val.startswith("{{"):
                ref = val.strip("{}").split(".")
                step_id, _, field = ref[0], ref[1], ref[2]
                inputs[key] = data_store[step_id][field]
            else:
                inputs[key] = val

        output = agent.run(inputs)
        data_store[step["id"]] = output
        print(f"\n--- {step['id']} output ---")
        print(output)

if __name__ == "__main__":
    run_workflow()