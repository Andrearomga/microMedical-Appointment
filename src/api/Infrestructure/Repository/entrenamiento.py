import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Función para limpiar el texto
def limpiar_texto(texto):
    texto_limpio = re.sub(r'[^\w\s]', '', texto)  # Elimina puntuación y caracteres especiales
    return texto_limpio.lower()  # Convierte a minúsculas

# Lectura del archivo CSV con codificación 'latin1'
try:
    df = pd.read_csv('src/api/Infrestructure/Repository/dataset_groserias.csv', encoding='latin1')
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    exit()

# Limpiar el texto
df['texto'] = df['texto'].apply(lambda x: limpiar_texto(str(x)))

# Vectorización de texto usando TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['texto'])

# Separación de datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, df['groseria'], test_size=0.2, random_state=42)

# Entrenamiento del modelo Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluación del modelo
predicciones = model.predict(X_test)
print("Reporte de clasificación:")
print(classification_report(y_test, predicciones))
print("Exactitud:", accuracy_score(y_test, predicciones))

# Guardar el modelo y el vectorizador en archivos
joblib.dump(model, 'modelo_entrenado.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Modelo y vectorizador guardados exitosamente.")
