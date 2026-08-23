# Plan d’intégration à faible disruption

Le principe directeur est de **ne pas casser la Skill Tree actuelle**.

L’interface publique peut continuer à présenter les six familles Nova exactement comme aujourd’hui. Les étapes ci-dessous enrichissent progressivement la donnée sous-jacente.

---

## Étape 0 — Geler la v1 comme source

**Risque : quasi nul**

- attribuer un identifiant stable à chaque terme ;
- conserver la définition, les signes, confusions et équivalents tels qu’ils sont dans la v1 ;
- enregistrer la version de source ;
- ne jamais écraser le texte original lors d’une annotation ultérieure.

Résultat : on peut expérimenter sans perdre l’historique.

---

## Étape 1 — Ajouter les relations typées

**Risque : faible / bénéfice immédiat**

Conserver les résonances actuelles pour la navigation si elles sont utiles, mais ajouter en parallèle :

```text
DISTINGUISH_FROM
PRECEDES
CO_OCCURS_WITH
FACILITATES
INHIBITS
IS_A
PART_OF
MAY_TRIGGER
MAY_CONTAIN
ASSOCIATED_WITH
```

Chaque relation devrait porter :

```text
source
predicate
target
basis
status
provenance
```

### Pourquoi commencer ici ?

Parce que les relations typées améliorent immédiatement :

- l’affichage des termes proches ;
- les confusions ;
- la navigation ;
- la génération d’un graphe ;
- les futures recherches.

Sans modifier une seule définition visible.

---

## Étape 2 — Ajouter les axes invisibles

**Risque : faible**

Sous chaque fiche, stocker les métadonnées multi-axiales :

```text
types[]
modalities[]
phases[]
selfhood_dimensions[]
cognitive_dimensions[]
motor_states[]
action_functions[]
```

Elles peuvent rester totalement invisibles au départ.

Puis introduire progressivement des filtres UX :

- phénomènes vestibulaires ;
- phénomènes auditifs ;
- entrée du sommeil ;
- réveil ;
- retour ;
- mémoire ;
- self-location ;
- motricité ;
- etc.

### Gain

Le même terme peut enfin appartenir à plusieurs dimensions sans être dupliqué dans plusieurs branches.

---

## Étape 3 — Afficher le statut des affirmations

**Risque : faible / bénéfice épistémique élevé**

Ajouter de petits badges facultatifs :

```text
OBSERVATION
DÉFINITION OPÉRATOIRE
INTERPRÉTATION
HYPOTHÈSE
```

Une fiche peut contenir plusieurs assertions de statuts différents.

### Exemple

```text
Sensation de vibration interne
[OBSERVATION]

Souvent rapportée près d’une transition
[ASSOCIATION / CORPUS]

Désaccouplement somato-conscience
[INTERPRÉTATION]
```

L’utilisateur n’est pas obligé d’adhérer à une ontologie pour utiliser la nomenclature.

---

## Étape 4 — Ajouter la provenance

Chaque information ajoutée peut recevoir une provenance :

```text
Nova Conscientia
Monroe / Gateway
Vieira / Projeciologia
étude scientifique
corpus de témoignages
annotation proposée
```

### UX possible

Une fiche affiche par défaut Nova uniquement.

Un bouton **Comparer** ouvre ensuite :

| Nova | Monroe | Vieira | Science |
|---|---|---|---|
| terme / définition | terme proche | terme proche | études pertinentes |

Aucune colonne n’est déclarée supérieure ou équivalente aux autres.

---

## Étape 5 — Formulaire de témoignage

**Risque : moyen / valeur stratégique très élevée**

Le formulaire doit demander le récit libre **avant** de montrer la nomenclature.

Ordre recommandé :

1. récit libre ;
2. chronologie libre ;
3. questions ouvertes de clarification ;
4. verrouillage du texte brut ;
5. seulement ensuite mapping vers les termes Nova ;
6. évaluation de confiance du mapping.

Variables utiles :

- moment de l’expérience ;
- induction ;
- intentionnalité ;
- ordre des événements ;
- rappel ;
- exposition préalable aux traditions ;
- délai avant rapport ;
- contexte de sommeil ;
- résultat / retour.

### Gain

La nomenclature devient un protocole de collecte plutôt qu’un simple glossaire.

---

## Étape 6 — Construire les Pathways à partir des rapports

Un Pathway ne devrait pas être une vérité déclarée dans le graphe.

Il devient une structure statistique :

```text
A apparaît dans 62 % des rapports
A précède B dans 71 % des rapports contenant A+B
B apparaît sans A dans 29 % des rapports
```

La séquence peut ainsi :

- se confirmer ;
- se ramifier ;
- dépendre d’une technique ;
- varier selon les pratiquants ;
- disparaître.

---

## Étape 7 — Application / graphe avancé

Seulement lorsque les données sont propres.

Possibilités :

- graphe interactif ;
- visualisation des trajectoires ;
- comparaison de traditions ;
- statistiques de corpus ;
- exploration des modalités ;
- API / export JSON ;
- outil de recherche collaboratif.

---

# Ordre recommandé

```text
SOURCE STABLE
   ↓
RELATIONS TYPÉES
   ↓
MÉTADONNÉES MULTI-AXIALES
   ↓
PROVENANCE / STATUT
   ↓
COMPARAISON DE SOURCES
   ↓
RAPPORTS STRUCTURÉS
   ↓
PATHWAYS EMPIRIQUES
   ↓
GRAPHE / APPLICATION AVANCÉE
```

Cet ordre maximise les gains immédiats tout en évitant de reconstruire l’interface plusieurs fois.
