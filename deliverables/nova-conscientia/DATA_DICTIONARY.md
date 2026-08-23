# Dictionnaire de données proposé

Ce document décrit la couche d’enrichissement sans exiger que les noms techniques soient visibles dans l’interface publique.

---

## Identité du concept

### `id`

Identifiant stable et machine-readable.

Exemple :

```text
nova.etat_vibratoire
```

Il ne doit pas changer si le libellé visible est légèrement révisé.

### `term`

Libellé humain.

### `source_original`

Bloc immuable contenant les données Nova de la version source :

- famille ;
- catégorie ;
- définition ;
- signes ;
- confusions ;
- équivalents ;
- résonances d’origine.

---

# Axes analytiques

## `types[]`

Nature logique du concept.

Valeurs actuelles :

```text
state
phenomenon
transition
action
obstacle
safety
concept
situation
condition
```

Un terme peut avoir plusieurs types lorsque la source elle-même mélange des fonctions.

---

## `modalities[]`

Canaux phénoménologiques principalement impliqués :

```text
visual
auditory
somatosensory
proprioceptive
vestibular
interoceptive
affective
cognitive
temporal
social_presence
```

`multimodal` est volontairement évité : il vaut mieux stocker les modalités réellement présentes.

---

## `phases[]`

Position temporelle possible :

```text
wake
sleep_onset
awakening
threshold
separation
experience
return
post_experience
```

Une phase décrit **quand**, pas **ce que le phénomène est**.

---

## `selfhood_dimensions[]`

Dimensions du soi corporel :

```text
self_location
body_ownership
first_person_perspective
agency
body_boundaries
```

Exemple : une Rotation peut modifier la perspective et la self-location sans qu’il soit nécessaire d’interpréter ontologiquement cette modification.

---

## `cognitive_dimensions[]`

```text
meta_awareness
reasoning_clarity
memory_continuity
goal_maintenance
executive_control
attention_stability
temporal_continuity
reality_monitoring
```

Permet de distinguer des notions que le tag générique « cognitif » écraserait.

---

## `motor_states[]`

```text
normal
reduced
immobility
atonia
perceived_paralysis
involuntary_movement
motor_effort
```

La motricité reste séparée des sensations somatiques.

---

## `action_functions[]`

Fonction opérationnelle d’une action.

Exemples conceptuels :

- régulation émotionnelle ;
- stabilisation ;
- orientation ;
- transition ;
- retour ;
- mémoire ;
- interrogation / communication.

Le vocabulaire exact peut être adapté avec Nova avant stabilisation.

---

# Assertions

## `assertions[]`

Une assertion représente une proposition individuelle au sujet du concept.

Exemple :

```json
{
  "predicate": "precedes",
  "target": "nova.decrochage",
  "epistemic_status": "source_supported",
  "basis": "La fiche indique que le phénomène peut précéder le décrochage."
}
```

### Pourquoi au niveau assertion ?

Parce qu’une seule fiche peut contenir :

- un signe observable ;
- une règle pratique ;
- une interprétation ;
- une hypothèse causale.

Attribuer un statut unique au terme entier ferait perdre cette distinction.

---

# Relations conceptuelles

## Relations actuelles

```text
is_a
part_of
precedes
follows
co_occurs_with
facilitates
inhibits
distinguish_from
may_trigger
may_contain
associated_with
```

### Relations symétriques

En principe :

```text
associated_with
co_occurs_with
distinguish_from
```

### Relations dirigées

Exemples :

```text
A precedes B
A facilitates B
A inhibits B
A may_trigger B
A part_of B
```

---

# Statuts épistémiques

Vocabulaire actuel :

```text
source_explicit
source_supported
phenomenological_observation
operational_definition
interpretation
hypothesis
proposed
```

Ils ne constituent pas une échelle simple de « vrai → faux ».

Ils disent **de quel genre de proposition il s’agit et d’où vient sa légitimité**.

---

# Sources externes

Un concept externe possède son propre identifiant :

```text
monroe.focus10
vieira.estado_vibracional
```

Il reste externe au namespace Nova.

Les crosswalks acceptent notamment :

```text
operationally_similar_to
partial_overlap
may_manifest_as
technique_targets
distinguish_from
no_direct_equivalent
```

`same_as` n’est pas utilisé dans les premières versions.

---

# Couche scientifique

Chaque étude contient :

```text
citation
year
evidence_class
source_locator
design_summary
findings[]
nc_links[]
limitations[]
does_not_establish[]
```

Les rôles possibles d’un lien scientifique vers NC sont :

```text
experimental_analogue
mechanistic_context
clinical_context
phenomenology_context
measurement_precedent
operationalization_support
alternative_explanation
```

Une étude scientifique n’est donc jamais automatiquement un « équivalent » du concept auquel elle est reliée.

---

# Rapports d’expérience

Un rapport structuré sépare :

```text
raw_description
term_refs[]
mapping_status
confidence
interpretation
```

Le récit brut doit pouvoir être conservé même si le mapping est ensuite corrigé.

Les rapports peuvent également stocker :

- ordre des événements ;
- temps relatif ;
- contexte d’induction ;
- confiance mnésique ;
- exposition préalable aux traditions ;
- type de questionnement ;
- consentement d’utilisation.

---

# Pathways

Un Pathway est un objet distinct :

```text
stages[]
transitions[]
constraints[]
provenance[]
```

Une transition de Pathway peut être :

```text
proposed_precedes
observed_precedes
optional_branch
may_facilitate
may_cooccur
```

Elle ne devient jamais automatiquement une relation ontologique entre les concepts Nova.
