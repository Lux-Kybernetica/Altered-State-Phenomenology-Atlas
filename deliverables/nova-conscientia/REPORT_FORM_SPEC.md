# Formulaire de témoignage — spécification v0.1

Objectif : recueillir des expériences comparables **sans injecter le vocabulaire de la nomenclature dans le récit avant qu’il soit produit**.

La partie A–D est destinée au participant. La partie E est réservée au codage ultérieur.

---

# A. Contexte minimal

### 1. Quand l’expérience s’est-elle produite ?

- date approximative ;
- heure approximative si connue ;
- endormissement / réveil / réveil nocturne / sieste / autre / inconnu.

### 2. Était-elle recherchée ?

- oui ;
- non ;
- partiellement / je ne sais pas.

### 3. Faisiez-vous quelque chose de particulier avant ?

Champ libre.

Ne pas proposer immédiatement une liste de techniques.

### 4. Combien de temps s’est écoulé entre l’expérience et ce récit ?

- quelques minutes ;
- moins d’une heure ;
- le même jour ;
- plusieurs jours ;
- plusieurs semaines ou davantage.

---

# B. Récit libre — À POSER AVANT TOUT LEXIQUE

## Question principale

> Racontez l’expérience depuis le dernier moment dont vous vous souvenez avant son début jusqu’au moment où vous considérez qu’elle était terminée. Décrivez ce que vous avez remarqué dans l’ordre, même si certains éléments vous semblent insignifiants.

Champ long, sans suggestions.

## Relance autorisée

> Y a-t-il quelque chose entre deux moments de votre récit dont vous vous souvenez mais que vous n’avez pas encore décrit ?

## Relance interdite à ce stade

Éviter :

- « Avez-vous eu des vibrations ? »
- « Avez-vous senti votre corps astral ? »
- « Étiez-vous en paralysie du sommeil ? »
- « Avez-vous traversé une zone de bascule ? »
- « Avez-vous fait une sortie partielle ? »

Ces formulations injectent précisément les catégories que nous voulons ensuite mesurer.

---

# C. Clarification phénoménologique ouverte

Ces questions ne doivent être posées qu’après le récit libre.

## Corps et mouvement

> Votre sensation de la position, de la forme ou du mouvement de votre corps a-t-elle changé ? Si oui, décrivez comment avec vos propres mots.

> Avez-vous essayé de bouger physiquement ? Qu’est-ce qui s’est passé ?

## Localisation

> Où aviez-vous l’impression de vous trouver par rapport à votre corps et à l’environnement ? Cette impression a-t-elle changé au cours de l’expérience ?

## Perspective

> Depuis quel point de vue perceviez-vous la scène ou l’espace ? Ce point de vue a-t-il changé ?

## Vision

> Qu’avez-vous vu, s’il y avait quelque chose à voir ? Comment cela a-t-il commencé et évolué ?

## Audition

> Qu’avez-vous entendu, s’il y avait quelque chose à entendre ?

## Sensations corporelles

> Quelles sensations corporelles étaient présentes ? Où étaient-elles situées et comment ont-elles évolué ?

## Émotions

> Quelles émotions étaient présentes ? Ont-elles changé quelque chose au déroulement de l’expérience ?

## Pensée et lucidité

> À quels moments saviez-vous ce qui vous arrivait ? Pouviez-vous réfléchir, vous souvenir de votre intention ou décider quoi faire ?

## Mémoire

> Y a-t-il des passages qui semblent manquer ou être difficiles à remettre dans l’ordre ?

---

# D. Variables de contamination / apprentissage

Ces questions sont posées **après** la description phénoménologique.

### Avant cette expérience, connaissiez-vous ou pratiquiez-vous :

- Nova Conscientia ;
- Gateway / Monroe Institute / Hemi-Sync ;
- Projeciologia / Conscienciologia / Vieira ;
- rêve lucide ;
- paralysie du sommeil ;
- pratiques de SHC / projection astrale ;
- autres systèmes similaires.

Pour chaque réponse positive :

> Depuis combien de temps environ et à quel niveau de familiarité ?

### Aviez-vous lu ou entendu, avant l’expérience, qu’un phénomène particulier devait se produire ?

Champ libre.

### Aviez-vous utilisé une technique donnant des instructions sur la manière dont le corps devait sembler bouger ou se séparer ?

Champ libre.

---

# E. Codage analyste — NON MONTRÉ AVANT LE RÉCIT

Chaque événement identifié reçoit :

```text
sequence
raw_description
nova_term_refs[]
mapping_status
mapping_confidence
interpretation (facultative, séparée)
```

## Mapping status

```text
reported_explicitly
analyst_mapped
uncertain
```

### Exemple

Récit :

> « J’avais l’impression de tourner lentement alors que je savais que mon corps était immobile. »

Codage possible :

```text
nova.rotation
confidence = 0.93
mapping_status = analyst_mapped
```

Le texte brut reste inchangé.

---

# F. Qualité du rapport

L’analyste renseigne :

## Confiance mnésique

0 → souvenir très incertain

1 → souvenir jugé très précis

## Confiance dans l’ordre temporel

0 → ordre largement reconstruit

1 → ordre jugé très sûr

## Complétude

```text
fragmentary
partial
substantial
near_complete
```

---

# G. Consentement

Le participant choisit explicitement un périmètre :

```text
usage privé de recherche
analyse anonymisée
publication anonymisée autorisée
```

Les informations identifiantes ne sont pas nécessaires à l’analyse phénoménologique.

---

# H. Règle de comparaison

Pour les études inter-traditions, l’analyse principale devrait idéalement être effectuée sur :

1. les descriptions brutes ;
2. par des codeurs qui ignorent, si possible, la tradition du participant ;
3. avant toute comparaison avec Monroe, Vieira ou un Pathway attendu.

Ensuite seulement on regarde si des séquences communes apparaissent.

---

# I. Ce que le formulaire permet de tester

Avec suffisamment de rapports, on peut calculer :

- fréquence des phénomènes ;
- ordre A → B ;
- A sans B ;
- B sans A ;
- différences selon technique ;
- différences selon exposition doctrinale ;
- différences entre sujets naïfs et entraînés ;
- fiabilité du mapping entre codeurs ;
- influence du délai de rappel ;
- branches de Pathway réellement observées.

Le formulaire devient ainsi le pont entre la nomenclature et une recherche cumulative.
