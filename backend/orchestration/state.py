from typing import TypedDict, List, Dict, Any

class NeuroState(TypedDict):
    user_input: str
    plan: dict
    
    sleep_data: List[float]
    bio_data: List[float]

    sleep_result: Dict[str, Any]
    bio_result: Dict[str, Any]

    analysis: str
    report: Dict[str, Any]
    guardrail: Dict[str, Any]
