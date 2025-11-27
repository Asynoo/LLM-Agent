from autogen import ConversableAgent
from feedback_agent.tools.paper_search_tool import search_papers
from feedback_agent.config import LLM_CONFIG

def create_research_agent() -> ConversableAgent:
    agent = ConversableAgent(
        name="Research Agent",
        system_message="You are a helpful AI assistant. "
                      "You can help find research papers using the search_papers tool. "
                      "Return 'TERMINATE' when the task is done.",
        llm_config=LLM_CONFIG,
    )

    agent.register_for_llm(name="search_papers", description="Search for research papers")(search_papers)
    return agent

def create_user_proxy():
    user_proxy = ConversableAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
    )
    user_proxy.register_for_execution(name="search_papers")(search_papers)
    return user_proxy