def preprocess_input(data):
    """
    Preprocesa los datos de entrada para el modelo.
    """
    try:
        # Normalizar altura (convertir de cm a metros) y peso (mantener en kg)
        height = data.get("player_height", 0) / 100  # Convertir cm a metros
        weight = data.get("player_weight", 0)  # Mantener peso en kg

        # Convertir otras características si se necesitan
        age = data.get("age", 0)
        draft_year = int(data.get("draft_year", 0))

        # Retornar las características procesadas como una lista
        return [height, weight, age, draft_year]
    except Exception as e:
        raise ValueError(f"Error en el preprocesamiento: {e}")
