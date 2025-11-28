from autogen import ConversableAgent
from feedback_agent.config import LLM_CONFIG

def create_evaluator_agent():

    #TODO: Expand the eval agent when research agent is fixed.
    return ConversableAgent(
        name="Evaluator",
        system_message="""Evaluate if the agent found correct research papers. 
        Output JSON: {'success': boolean, 'reason': 'explanation'}, 
        Then return 'TERMINATE'.""",
        llm_config=LLM_CONFIG,
    )