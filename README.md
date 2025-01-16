# Inferencia del Modelo del Draft de la NBA

Este proyecto demuestra una secuencia de inferencia Dockerizada para predecir los resultados del draft de la NBA utilizando un modelo de aprendizaje automático entrenado.

## Características
- Preprocesa los datos de los jugadores (por ejemplo, altura, peso, estadísticas).
- Predice la probabilidad de que un jugador sea seleccionado en el draft de la NBA.
- Dockerizado para facilitar la implementación y las pruebas.

## Cómo Ejecutarlo

### Paso 1: Construir la Imagen Docker
```bash
docker build -t nba-draft-inference .
```

### Paso 2: Ejecutar el Contenedor Docker
```bash
docker run -p 5000:5000 nba-draft-inference
```

### Paso 3: Enviar una Solicitud
Utiliza la siguiente entrada de ejemplo:
```json
{
  "height": 205,
  "weight": 100
}
```

### Respuesta de Ejemplo
```json
{
  "prediction": [1]
}
```

## Archivos y Directorios
- `app/`: Contiene el código fuente de la aplicación.
  - `model/`: Archivo del modelo entrenado (`nba_draft_model.pkl`).
  - `preprocessing/`: Scripts para el preprocesamiento de datos de entrada.
  - `inference/`: Lógica para la inferencia del modelo.
- `data/`: Contiene ejemplos de entrada para pruebas.
- `Dockerfile`: Configuración para Dockerizar la aplicación.
- `requirements.txt`: Dependencias para Python.

## Dataset y Entrenamiento del Modelo
El modelo entrenado (`nba_draft_model.pkl`) se crea utilizando un dataset de prospectos del draft de la NBA. Las características incluyen altura y peso. Puedes reemplazar o reentrenar el modelo con tu propio dataset siguiendo estos pasos:

1. Prepara un dataset con las características necesarias (por ejemplo, altura, peso, resultado del draft).
2. Entrena un modelo utilizando `scikit-learn` u otra biblioteca similar.
3. Guarda el modelo entrenado en `app/model/nba_draft_model.pkl`.

## Extender el Proyecto
- Agrega más características como estadísticas de los jugadores, rendimiento universitario o resultados de combinaciones físicas.
- Mejora el modelo experimentando con diferentes algoritmos o hiperparámetros.

## Licencia
Este proyecto es de código abierto y está disponible bajo la Licencia MIT.
