from autogen import ConversableAgent
from feedback_agent.tools.paper_search_tool import search_papers
from feedback_agent.config import LLM_CONFIG

def create_research_agent() -> ConversableAgent:
    agent = ConversableAgent(

        #TODO: We need to formulate a better background for the agent, right now some of the agents doesnt strictly follow user-prompt.
        name="Research Agent",
        system_message="You are a research paper finding specialist. "
                       "When the user asks to find research papers, use the search_papers tool. "
                       "After getting results, summarize the findings and then say 'TERMINATE'. "
                       "ONLY call the search tool ONCE per request. "
                       "After providing the paper results, ALWAYS end with 'TERMINATE'.",
        llm_config=LLM_CONFIG,
    )

    agent.register_for_llm(
        name="search_papers",
        description="Search for research papers. Parameters: topic (string), year_filter (in/before/after), year (number), citation_filter (exactly/at least/at most), citation_count (number)"
    )(search_papers)
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
