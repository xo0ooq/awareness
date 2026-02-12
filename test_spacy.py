import spacy

# Załaduj model polski
nlp = spacy.load("pl_core_news_sm")

# Tekst do analizy
tekst = "Ala ma kota i lubi go bardzo. Codziennie go karmi."

# Przetwarzanie tekstu
doc = nlp(tekst)

# Tokenizacja
print("=== Tokeny ===")
print([token.text for token in doc])

# Lematyzacja
print("\n=== Lematy ===")
print([token.lemma_ for token in doc])

# Części mowy
print("\n=== Części mowy ===")
for token in doc:
    print(f"{token.text} → {token.pos_}, {token.tag_}")

# Opcjonalnie: wyświetlenie zależności składniowych
print("\n=== Zależności składniowe ===")
for token in doc:
    print(f"{token.text} → head: {token.head.text}, dep: {token.dep_}")
