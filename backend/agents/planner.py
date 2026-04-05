def planner_agent(query):
    """
    Planner Agent:
    Decides which agents to run
    """

    query = query.lower()

    return {
        "run_sleep": "sleep" in query,
        "run_bio": True,
        "run_analysis": True
    }
