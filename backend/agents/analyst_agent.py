def analyst_agent(sleep_output, bio_output):
    """
    Analyst Agent:
    - Combines sleep + bio insights
    - Generates interpretation
    """

    sleep = sleep_output["sleep_quality"]
    cluster = bio_output["cluster"]

    analysis = f"""
    Sleep Status: {sleep}
    Biological Group: {cluster}
    """

    # Reasoning layer
    if sleep == "Poor Sleep" and "Stress" in cluster:
        analysis += "\n⚠️ High risk detected: Poor sleep aligns with stress cluster."

    elif sleep == "Healthy Sleep" and "Balanced" in cluster:
        analysis += "\n✅ Optimal condition: Stable sleep and balanced biology."

    else:
        analysis += "\nℹ️ Mixed signals: Monitor trends over time."

    return {
        "agent": "analyst_agent",
        "analysis": analysis.strip()
    }
