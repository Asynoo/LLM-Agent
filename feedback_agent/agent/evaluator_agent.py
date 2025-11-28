from autogen import ConversableAgent
from feedback_agent.config import LLM_CONFIG

def create_evaluator_agent():

    #TODO: Expand the eval agent when research agent is fixed.
    return ConversableAgent(
        name="EvaluationBot",
        system_message="You are a rigorous AI agent evaluator. "
                       "Evaluate if the agent successfully completed the EXACT TASK provided. "
                       "IMPORTANT: 'at least X citations' means citations ≥ X. "
                       "For example: 65 ≥ 50 is TRUE, 80 ≥ 50 is TRUE, 70 ≥ 50 is TRUE. "
                       "Do basic math correctly. "
                       "Output ONLY valid JSON: {'success': boolean, 'reason': 'detailed explanation'} "
                       "Then return 'TERMINATE'.",
        llm_config=LLM_CONFIG,
    )

#### this is the 
        # name="Evaluator",
        # system_message="""Evaluate if the agent found correct research papers. 
        # Output JSON: {'success': boolean, 'reason': 'explanation'}, 
        # Then return 'TERMINATE'.""",
        # llm_config=LLM_CONFIG,