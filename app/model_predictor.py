import pickle

# Cargar el modelo entrenado
with open("app/model/nba_draft_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict(data):
    """
    Realiza una predicción basada en los datos preprocesados.
    """
    try:
        prediction = model.predict([data])
        return prediction.tolist()
    except Exception as e:
        raise ValueError(f"Error en la predicción: {e}")
