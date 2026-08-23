# Monroe / Gateway × Nova — crosswalk v0.1 audit

## Scope

This audit reviews the first external terminology crosswalk from The Monroe Institute / Gateway Experience into canonical Nova Conscientia concepts.

The crosswalk is **not** an import of Monroe ontology into Nova. It is a translation/alignment layer for phenomenological and procedural comparison.

## Coverage

- External Monroe/Gateway concepts: **12**
- Crosswalk mappings: **14**
- Direct identity mappings (`same_as` / equivalence): **0**
- Canonical NC references unresolved: **0**
- Mapping statuses used: `crosswalk_inference`

## Canonical NC references checked

The mappings resolve to reviewed NC IDs including:

- `nova.endormissement_conscient`
- `nova.amnesie_de_retour`
- `nova.balancement`
- `nova.flottement`
- `nova.chute_interne`
- `nova.etat_vibratoire`
- `nova.bourdonnement`
- `nova.bourdonnement_intracranien`
- `nova.images_hypnagogiques`
- `nova.hypnagogie`
- `nova.lacher_prise`
- `nova.hypercontrole`
- `nova.rotation_volontaire`
- `nova.decrochage`
- `nova.sortie_partielle`
- `nova.sortie_complete`
- `nova.retour_volontaire`
- `nova.ancrage_post_experience`
- `nova.orientation`
- `nova.debrief_structure`
- `nova.ancrage_de_memoire`

## High-confidence correspondences

The strongest v0.1 operational alignments are:

- perceived vibrations → `nova.etat_vibratoire`
- buzzing / rushing auditory cues → `nova.bourdonnement` / `nova.bourdonnement_intracranien`
- dream-like imagery near sleep → `nova.images_hypnagogiques` / `nova.hypnagogie`
- release of expectations / non-forcing → `nova.lacher_prise`
- Point of Departure 180° rotation technique → `nova.rotation_volontaire`
- intentional return to C-1 → `nova.retour_volontaire`
- post-exercise grounding → `nova.ancrage_post_experience` / `nova.orientation`

## Deliberately weak or partial correspondences

- Focus 10 ↔ Endormissement conscient is **operationally similar**, not equivalent. Focus 10 is a Monroe program-defined Focus state; NC models a phenomenological transition/process concept.
- Click-out ↔ Amnésie de retour is only a **partial mnemonic overlap**. Their temporal placement differs.
- Monroe separation/projection language spans several NC concepts rather than mapping cleanly to one node.
- Generic Monroe language about “vibrational energy” is **not** mapped to `nova.etat_vibratoire`; only subjectively perceived vibration phenomena are.

## Source boundary

The Gateway manuals use metaphysical/program-specific language including energy body, nonphysical systems, projection and Focus levels. Those formulations remain attributed to Monroe/Gateway source framing. The crosswalk does not promote them to Nova source facts or scientific assertions.

## Result

**PASS at the data-model level — 12 external concepts and 14 non-identity mappings are internally coherent and all referenced NC IDs resolve to canonical reviewed concepts.**

Automated execution of `scripts/validate_crosswalks.py` remains part of the unresolved GitHub Actions execution issue, but the committed crosswalk has been manually reference-audited.
