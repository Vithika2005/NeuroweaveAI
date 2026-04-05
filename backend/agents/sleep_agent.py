from ml.sleep_model import train_sleep_model, predict_sleep_quality

def sleep_agent(sleep_data):
    """
    Sleep Agent:
    - Trains LSTM model
    - Predicts sleep quality
    """

    model = train_sleep_model(sleep_data)
    quality = predict_sleep_quality(model, sleep_data)

    return {
        "agent": "sleep_agent",
        "sleep_quality": quality,
        "input_sequence": sleep_data
    }
