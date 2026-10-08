from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics

texts = [
    "Eu amo programar em Python", "A máquina de lavar está quebrada", "Eu gosto de pizza", 
    "Python é uma linguagem de programação", "Eu preciso consertar minha máquina de lavar",
    "Pizza é minha comida favorita", "Estou aprendendo a programar", "O forno está quebrado",
    "Eu amo pizza de pepperoni", "A geladeira parou de funcionar", "O curso de Python é ótimo",
    "Preciso de um técnico para consertar minha geladeira", "A pizza de marguerita é deliciosa",
    "Eu gosto de aprender novas linguagens de programação", "O conserto do micro-ondas foi caro"
]

labels = [
    "tecnologia", "doméstico", "comida", "tecnologia", "doméstico", "comida", 
    "tecnologia", "doméstico", "comida", "doméstico", "tecnologia", "doméstico",
    "comida", "tecnologia", "doméstico"
]

X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)
labels_predicted = model.predict(X_test)

print(metrics.classification_report(y_test, labels_predicted, zero_division=0))

new_texts = ["Eu preciso aprender Python", "A pizza está delecionsa"]
new_labels_predicted = model.predict(new_texts)
print("Previsões para novos textos:", new_labels_predicted)