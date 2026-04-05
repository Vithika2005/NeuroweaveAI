def guardrail_agent(analysis_text):
    """
    Guardrail Agent:
    - Checks for unsafe / low confidence outputs
    """

    if "High risk" in analysis_text:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "agent": "guardrail_agent",
        "risk_level": risk,
        "status": "SAFE"
    }
