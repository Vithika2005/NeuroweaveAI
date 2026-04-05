def report_agent(analysis_output, guardrail_output):
    """
    Report Agent:
    - Final structured response
    """

    return {
        "agent": "report_agent",
        "final_report": analysis_output["analysis"],
        "risk_level": guardrail_output["risk_level"],
        "confidence": 0.85
    }
