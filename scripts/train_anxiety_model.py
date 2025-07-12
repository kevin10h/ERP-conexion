"""
Entrena varios algoritmos, elige el mejor (F1)
y guarda un Pipeline (scaler+modelo) en app/models/ml.joblib
uso:  python scripts/train_anxiety_model.py datos.csv
"""
import sys, warnings, joblib, pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

warnings.filterwarnings("ignore")

CSV      = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("enhanced_anxiety_dataset.csv")
OUT      = Path("app/models/ml.joblib")          # <- FastAPI ya apunta aquí

# --- 1. Cargar y limpiar ---
df = pd.read_csv(CSV)
df = df.loc[:, ~df.columns.str.lower().str.startswith(("row_number", "marca"))]

rename = {                                 # nombres cortos
 '1. ¿Cuántos años tienes?':'Age', '2. ¿Cuál es tu género?':'Gender',
 '3. ¿Cuál es tu ocupación actual?':'Occupation', '4. ¿Cuántas horas duermes en promedio cada noche?':'Sleep',
 '5. ¿Cuántas horas a la semana realizas actividad física?':'Physical',
 '6. ¿Cuántos miligramos de cafeína consumes al día (café, té, bebidas energéticas, etc.)?':'Caffeine',
 '7. ¿Cuántos tragos de alcohol consumes por semana?':'Alcohol',
 '8. ¿Fumas actualmente?':'Smoking', '9. ¿Tienes antecedentes familiares de ansiedad?':'Family',
 '10. En una escala del 1 al 10, ¿cuál es tu nivel de estrés actual? ':'Stress',
 '11.¿Cuál es tu frecuencia cardíaca en reposo (en bpm)? ':'Heart',
 '12.¿Cuál es tu ritmo respiratorio (respiraciones por minuto)? ':'Breathing',
 '13.En una escala del 1 al 5, ¿cuánto sudor presentas en situaciones normales? ':'Sweating',
 '14.¿Has experimentado mareos recientemente? ':'Dizziness',
 '15.¿Estás tomando medicamentos actualmente? ':'Medication',
 '16. ¿Estás asistiendo a sesiones de terapia psicológica? Si es así, ¿cuántas veces al mes? ':'Therapy',
 '17. ¿Has pasado recientemente por un evento importante o estresante? (Ej. mudanza, pérdida, ruptura, cambio laboral, etc.) ':'Major',
 '18.¿Cómo calificarías la calidad de tu dieta en general? ':'Diet',
 '19.¿Qué nivel de ansiedad consideras que tienes actualmente? ':'Anxiety'
}
df = df.rename(columns=rename)

binary = {'Sí':1,'No':0,'sí':1,'no':0,'SÍ':1,'NO':0}
for col in ['Smoking','Family','Dizziness','Medication','Major']:
    df[col] = df[col].map(binary).fillna(0)

for col in ['Gender','Occupation']:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

df = df.apply(pd.to_numeric, errors='coerce').dropna()
df['y'] = (df['Anxiety'] >= 6).astype(int)
X, y = df.drop(columns=['Anxiety','y']), df['y']

X_tr, X_te, y_tr, y_te = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# --- 2. Modelos candidatos ---
cands = {
  "logreg": LogisticRegression(max_iter=2000, class_weight='balanced'),
  "mlp"   : MLPClassifier(hidden_layer_sizes=(64,32), max_iter=400, early_stopping=True, random_state=42),
  "forest": RandomForestClassifier(n_estimators=200, max_depth=8, class_weight='balanced', random_state=42)
}

best, best_f1 = None, 0.0
for name, clf in cands.items():
    pipe = Pipeline([("scaler", StandardScaler()), ("clf", clf)])
    pipe.fit(X_tr, y_tr)
    f1 = f1_score(y_te, pipe.predict(X_te))
    print(f"{name:>6}: F1={f1:.3f}")
    if f1>best_f1: best, best_f1 = pipe, f1

print(f"🏆 Mejor modelo F1={best_f1:.3f} → guardando {OUT}")
OUT.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(best, OUT)
