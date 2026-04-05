from agents.sleep_agent import sleep_agent
from agents.bio_agent import bio_agent
from agents.analyst_agent import analyst_agent
from agents.guardrail_agent import guardrail_agent
from agents.report_agent import report_agent
from agents.planner import planner_agent

#Planner Node
def planner_node(state):
    plan = planner_agent(state["user_input"])
    return {"plan": plan}

# 💤 Sleep Node
def sleep_node(state):
    result = sleep_agent(state["sleep_data"])
    return {"sleep_result": result}


# 🧬 Bio Node
def bio_node(state):
    result = bio_agent(state["bio_data"])
    return {"bio_result": result}


# 🧠 Analyst Node
from tools.llm_tool import call_llm
from tools.analysis_tool import fetch_similar_cases
from tools.data_tool import get_context

def analyst_node(state):
    sleep = state["sleep_result"]["sleep_quality"]
    cluster = state["bio_result"]["cluster"]

    # 🔥 Retrieve memory
    past_cases = fetch_similar_cases(f"{sleep} {cluster}")
    recent_context = get_context()

    prompt = f"""
    You are a biological intelligence analyst.

    Current:
    Sleep: {sleep}
    Cluster: {cluster}

    Past similar cases:
    {past_cases}

    Recent context:
    {recent_context}

    Provide:
    - Insight
    - Risk
    - Recommendation
    """

    response = call_llm(prompt)

    return {"analysis": response}

# ⚠️ Guardrail Node
def guardrail_node(state):
    guard = guardrail_agent(state["analysis"])
    return {"guardrail": guard}


# 📊 Report Node
from tools.storage_tool import store_analysis
from tools.data_tool import store_context

def report_node(state):
    report = {
        "final_report": state["analysis"],
        "risk": state["guardrail"]["risk_level"]
    }

    # 🔥 Store in memory
    store_analysis(state["analysis"])
    store_context(report)

    return {"report": report}
