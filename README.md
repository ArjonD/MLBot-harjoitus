# Seminaarityön raportti – Naive Bayes -pohjainen Chatbot

## Johdanto
Seminaarityössä tavoitteena on toteuttaa yksinkertaisen chatbot, joka käyttää koneoppia luokittelemaan
käyttäjän syötteitä eri intentteihin (tervehdys, hyvästely, nimen kysely) ja palauttamaan näihin lopuksi
sopivan vastauksen. 

## Tavoitteet
Tämän projektin tavoitteet olivat:
- Ymmärtää tekstin vektorisointia (Bag-of-Words)
- Kouluttaa yksinkertaisen intenttiluokitin Naive Bayes menetelmällä
- Toteuttaa toimivan komentorivipohjaisen chatbotin
- Rakentaa järjeselmän, joka valitsee vastauksen luokitellun intentin perusteella
- Harjoitella koneoppimiskirjastojen eli sklearnin käyttöä

## Toteutus
**Arkkitehtuuri**
A[Syöte käyttäjältä] --> B[CountVectorizer: muutetaan teksti numeroiksi]
B --> C[Multinomial Naive Bayes -luokitin]
C --> D[Intenttiarvaus]
D --> E[Vastaus sanakirjasta]
E --> F[Vastauksen tulostus]

**Koodi**
1. Data
   - Pieni kokoelma, joka koostuu esimerkkilauseista, josta se oppii (training_sentences)
   - Esimerkkilauseille omat luokat, jotta voi päättellä mikä intentti se on (training_labels)
   - Sanakirja, josta chatbot poimii vastauksen intenttin mukaisesti. (responses)
2. Tekstin vektorisointi
   - Countvectorizer muuttaa sanat numeroiksi
3. Mallin koulutus
   - MultinomialNB avulla tehdään Bag-of-Words, joka tekee tilasto taulukon intenttien mahdollisuuksien mukaisesti
4. Käyttäjän syöte
   - Syöte muunnetaan vektoriin
   - Luokitin ennistaa intentin
   - vastaus haetaan sanakirjast
## Käytetty teknologiat
- Python 3
- scikit-learn
- CountVectorizer
- MultinomialNB
- Komentorivi
## Oppiminen
Opin projektista
- Tekstin muunnos numeriseen muotoon
- Naive Bayes mallin periaatteet
- opetusdatan haasteet, kun on pieni kokoelma
- Cmd kautta tehdä koodia (python -c "import sklearn; print(sklearn.__version__))
## Jatkokehitys
Chatbot toimii, mutta jos pitäisi parantaa:
- Testidatan lisäys
- Sanakirjaston laajennus
- Tehdä chatbotista web versio eikä komentorivi
## Lähteet
- [Scikit-learn documentation – CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
- [Scikit-learn documentation – MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)
- Géron, A. Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow, O’Reilly, 2019.
