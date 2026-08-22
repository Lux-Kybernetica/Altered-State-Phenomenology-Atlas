# NC × Lux — Pipeline technique

1. `NOVA_NOMENCLATURE_V1.json` : extraction fidèle de Nova.
2. `NOVA_V1_ENRICHED_PILOT_10_v0.2.json` : 10 termes pilotes annotés manuellement.
3. `NOVA_V1_FULL_PREANNOTATED_v0.3.json` : propagation heuristique aux 92 termes.
4. `NC_LUX_REVIEW_QUEUE_v0.3.md` : file de révision humaine priorisée.
5. Après révision : création d'une v0.4 consolidée et seulement ensuite génération du graphe relationnel.

Principe : l'original Nova ne bouge jamais ; toute annotation Lux reste séparée et traçable.
