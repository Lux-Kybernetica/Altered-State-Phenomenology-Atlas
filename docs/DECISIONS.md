# Decision log

## D001 — Preserve Nova source text
**Decision:** Never overwrite the source wording inside the working model.

**Reason:** We need traceability and must be able to distinguish Nova content from Lux analysis.

---

## D002 — Multi-type concepts are allowed
**Decision:** `types` is an array rather than a single exclusive value.

**Reason:** Entries such as Hypnagogie, État vibratoire and Sortie complète legitimately cross logical categories.

---

## D003 — Remove generic `multimodal`
**Decision:** Prefer explicit accumulated modalities.

**Reason:** `multimodal` hides information. `visual + auditory + proprioceptive` is more useful.

---

## D004 — Add embodiment / selfhood
**Decision:** Track self-location, body ownership, perspective, agency and body boundaries independently.

**Reason:** SHC and autoscopic phenomena frequently concern the organization of the self, not only sensory events.

---

## D005 — Add motor state
**Decision:** Motor condition is a separate axis from perceptual modality.

**Reason:** Paralysis, atonia, involuntary movement and motor effort cannot be represented cleanly as sensory modalities.

---

## D006 — Epistemic status belongs to assertions
**Decision:** Classify individual propositions as source-explicit, source-supported, observation, operational definition, interpretation, hypothesis or proposal.

**Reason:** One entry can mix several epistemic levels.

---

## D007 — Keep the repository private for now
**Decision:** Treat the repository as private research material.

**Reason:** It contains or derives from third-party Nova Conscientia material. Public redistribution should wait for a clearer collaboration/reuse framework.

---

## D008 — Add cognitive dimensions
**Decision:** Add an optional `cognitive_dimensions[]` axis with controlled values: `meta_awareness`, `reasoning_clarity`, `memory_continuity`, `goal_maintenance`, `executive_control`, `attention_stability`, `temporal_continuity`, `reality_monitoring`.

**Reason:** The Nova family `États & lucidité` already distinguishes several cognitive functions that cannot be represented adequately by the single modality label `cognitive`. Lucidity, mental clarity, memory continuity and executive control are related but not interchangeable.

**Constraint:** The axis identifies which cognitive dimension is involved; it does not yet impose a universal numeric scale or severity level. Qualitative state remains expressed through assertions until the corpus justifies a stronger dimensional model.

---

## D009 — A phenomenon need not have a sensory modality
**Decision:** `modalities[]` may legitimately be empty when an entry is primarily a reorganization of selfhood rather than a sensory event.

**Reason:** `Dissolution des frontières` is better represented by `self_location` and `body_boundaries` than by inventing a sensory modality merely to fill the field.

---

## D010 — Preserve source-category mismatches explicitly
**Decision:** When Nova's source category conflicts with the semantic content of its own definition, preserve the category in the source layer but classify the Lux annotation from the definition rather than the label.

**Reason:** `Pression émotionnelle` and `Distorsion du temps` are both filed under `présence perçue` in Nova v1, although their definitions describe affective/interoceptive and temporal phenomena respectively. The discrepancy is useful audit information and must not be silently normalized away.

---

## D011 — Absence of perceptual content can still be a modality state
**Decision:** A term such as `Écran noir` may use the `visual` modality even though the reported visual content is absence rather than presence.

**Reason:** Future data modeling must distinguish whether a modality is relevant from what content that modality contains. Otherwise 'no image' becomes indistinguishable from 'visual modality not assessed'.

---

## D012 — Add action functions
**Decision:** Add optional `action_functions[]` with controlled values: `stabilization`, `affect_regulation`, `attention_regulation`, `intention_control`, `separation`, `navigation`, `interaction`, `epistemic_monitoring`, `return`, `memory_consolidation`, `integration`.

**Reason:** `action` tells us what kind of object an entry is, but not what the action is intended to do. `Se calmer`, `Point focal`, `Retour volontaire` and `Ancrage de mémoire` are all actions with different functions.

**Constraint:** Action function does not imply demonstrated efficacy. It records the operational role attributed to the action in the source/model.

---

## D013 — Obstacle is a functional type, not a phenomenological dimension
**Decision:** Do not create a separate obstacle-domain axis unless later data require it.

**Reason:** Nova obstacles decompose adequately across cognition, affect, motor state, perception and memory. An item is an `obstacle` relative to the practice goal, while its underlying phenomenology is represented by the other axes.

---

## D014 — Safety guidance is not a clinical standard
**Decision:** Preserve Nova safety thresholds and recommendations as operational guidance or interpretation unless independently sourced later.

**Reason:** Statements such as the one-week pause rule for sleep disruption are useful as source content but must not be silently promoted into universal clinical thresholds. Warning entries are modeled without assigning diagnosis or etiology.
