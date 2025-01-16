from joblib import load

# Cargar el modelo entrenado en formato joblib
model = load("app/model/nba_draft_model.joblib")

def predict(data):
    """
    Realiza una predicción basada en los datos preprocesados.
    """
    try:
        prediction = model.predict([data])
        return prediction.tolist()
    except Exception as e:
        raise ValueError(f"Error en la predicción: {e}")
