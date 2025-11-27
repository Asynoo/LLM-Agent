import warnings
warnings.filterwarnings("ignore", message="flaml.automl is not available")

from agent.research_agent import create_research_agent, create_user_proxy


def main():
    user_proxy = create_user_proxy()
    research_agent = create_research_agent()

    user_proxy.initiate_chat(
        research_agent,
        #TODO: Find some alternate better prompt maybe? A few specific and broad.
        message="Find a research paper on machine learning that was published after 2015 and has at least 50 citations."
    )

    #TODO: Evaluation logic here.

if __name__ == "__main__":
    main()