from fastapi import FastAPI
from orchestration.graph import build_graph

app = FastAPI()
graph = build_graph()

@app.post("/analyze")
def analyze():
    initial_state = {
        "user_input": "analyze sleep",
        "plan": {},

        "sleep_data": [6, 5, 7, 4, 6],
        "bio_data": [6, 7, 5],

        "sleep_result": {},
        "bio_result": {},
        "analysis": "",
        "report": {},
        "guardrail": {}
    }

    result = graph.invoke(initial_state)
    return result
