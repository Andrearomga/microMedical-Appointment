import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

def limpiar_texto(texto):
    texto_limpio = re.sub(r'[^\w\s]', '', texto)
    return texto_limpio.lower()

# Verifica la existencia del archivo CSV
csv_path = 'src/api/Infrestructure/Repository/dataset_groserias.csv'
if not os.path.exists(csv_path):
    print(f"No se encontró el archivo CSV en {csv_path}")
    exit()

df = pd.read_csv(csv_path, encoding='latin1')
df['texto'] = df['texto'].apply(lambda x: limpiar_texto(str(x)))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['texto'])
X_train, X_test, y_train, y_test = train_test_split(X, df['groseria'], test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

predicciones = model.predict(X_test)
print("Reporte de clasificación:")
print(classification_report(y_test, predicciones))
print("Exactitud:", accuracy_score(y_test, predicciones))

# Directorio base donde se encuentra el CSV
base_dir = os.path.dirname(csv_path)

# Rutas completas para guardar los modelos
model_path = os.path.join(base_dir, 'modelo_entrenado.pkl')
vectorizer_path = os.path.join(base_dir, 'vectorizer.pkl')

joblib.dump(model, model_path)
joblib.dump(vectorizer, vectorizer_path)
print(f"Modelo y vectorizador guardados exitosamente en {model_path} y {vectorizer_path}.")
