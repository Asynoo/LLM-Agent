import warnings
warnings.filterwarnings("ignore", message="flaml.automl is not available")

from agent.research_agent import create_research_agent, create_user_proxy
from agent.evaluator_agent import create_evaluator_agent

def main():
    user_proxy = create_user_proxy()
    research_agent = create_research_agent()

    #task = "Find a research paper on skin cancer that was published after 2022 and has at least 120 citations."
    #task = "Find a research paper on machine learning that was published after 2020 and has at least 100 citations."
    #task = "Locate a research paper about cybersecurity that was published after 2017 and has at least 250 citations."

    #task = "Find a research paper on cybersecurity that was published after 2017 and has at least 250 citations."
    #task = "Find research papers on cybersecurity that were published after 2017 and have at least 250 citations."
    task = "Find 3 research papers on cybersecurity that were published after 2017 and have at least 50 citations each."

    user_proxy.initiate_chat(research_agent, message=task)
    result = user_proxy.last_message(research_agent)["content"]

    evaluator = create_evaluator_agent()
    eval_proxy = create_user_proxy()

    #eval_proxy.initiate_chat(evaluator, message=f"Task: {task} \nAgent Result: {result} \nDid the agent succeed?", max_turns=2)

    eval_proxy.initiate_chat(
            evaluator,
            message=f"""
            TASK: {task}

            AGENT RESULT: {result}

            EVALUATION CRITERIA:
            
            1. Did the agent find REAL research papers (not fabricated)?
            2. Are papers relevant to the topic specified in the TASK?
            3. Were papers published after the year specified in the TASK?
            4. Do papers have at least the citation count specified in the TASK?
            5. Did the agent properly use search tools?

            Be strict - if papers look fabricated, mark as failure.
            """
            , max_turns=2)


    evaluation = eval_proxy.last_message(evaluator)["content"]

    print("Research Agent Results:")
    print(result)

    print("Evaluation Agent Results:")
    print(evaluation)

if __name__ == "__main__":
    main()