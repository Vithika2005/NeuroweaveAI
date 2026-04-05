import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Normalize data
scaler = MinMaxScaler()

def prepare_data(data, time_steps=3):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:i+time_steps])
        y.append(data[i+time_steps])
    return np.array(X), np.array(y)


def train_sleep_model(data):
    data = np.array(data).reshape(-1, 1)
    data = scaler.fit_transform(data)

    X, y = prepare_data(data)

    model = Sequential([
        LSTM(32, input_shape=(X.shape[1], 1)),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=20, verbose=0)

    return model


def predict_sleep_quality(model, data):
    data = np.array(data).reshape(-1, 1)
    data = scaler.transform(data)

    X, _ = prepare_data(data)
    preds = model.predict(X, verbose=0)

    avg_pred = np.mean(preds)

    if avg_pred < 0.4:
        return "Poor Sleep"
    elif avg_pred < 0.7:
        return "Moderate Sleep"
    else:
        return "Healthy Sleep"
