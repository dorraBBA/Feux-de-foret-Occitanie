
# Objectif 1 — Cartographier les zones les plus exposées aux incendies

## KPI 1.1 (principal) — Nombre moyen annuel de départs de feu par commune

| Champ | Valeur |
|---|---|
| 1. Question et objectif | Quelles sont les 10 communes de Haute-Garonne qui enregistrent le plus de départs de feu ? Objectif 1 de `docs/analyse/objectifs.md`. |
| 2. Formule | Numérateur : nombre total de départs de feu dans la commune. Dénominateur : nombre d'années étudiées. Formule : KPI = nombre de départs de feu / nombre d'années. Unité : feux par commune et par an. |
| 3. Paramètres | Période : 5 ou 10 ans ; territoire : Haute-Garonne (31) ; nombre de communes : Top 10. |
| 4. Périmètre, période, granularité, fréquence | Haute-Garonne ; période proposée : 2016–2025 ; granularité : commune ; recalcul annuel. |
| 5. Source et champs | BDIFF : date, commune, département. IGN Admin Express : limites communales. IGN BD Forêt V2 : couverture forestière. Fiches : `docs/sources/fiche-BDIFF.md` et `docs/sources/fiche-BD-Foret-V2.md`. |
| 6. Lignes utilisables | Non vérifiées : export BDIFF non ouvert. À mesurer : part des lignes avec date, commune et département renseignés. |
| 7. Proxy et biais | Si les coordonnées exactes manquent, utiliser la commune déclarée. Biais : représenter toute la commune comme exposée peut surestimer la surface réellement concernée. |
| 8. Décision éclairée | Classer les communes et proposer une surveillance prioritaire dans les 10 premières, en tenant compte de leur couverture forestière. |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** passer de 10 à 15 communes.

- Ce qui change : la carte affiche 15 communes au lieu de 10 et la surveillance pourrait être répartie sur davantage de territoires.
- Ce qui ne change pas : la formule, les sources, la période et la méthode de calcul.
- Décision : élargir la liste des communes prioritaires si les ressources disponibles le permettent.

**RACER :**

- Relevant : permet d'identifier les communes prioritaires.
- Accepted : à confirmer avec le SDIS 31.
- Credible : oui si les données historiques sont complètes.
- Easy : simple comptage des départs de feu par commune.
- Robust : dépend de la période et de la qualité des localisations.

**Garde-fous :**

- Afficher le nombre total de feux avec la moyenne annuelle.
- Fixer la période avant de calculer le classement.
- Ne pas considérer toute la commune comme présentant le même risque.
- Vérifier les communes ayant peu de données.
- Risque résiduel : les feux non déclarés ne sont pas comptabilisés et le passé ne garantit pas le risque futur.

---

## KPI 1.2 (secondaire) — Part de la surface forestière par commune

| Champ | Valeur |
|---|---|
| 1. Question et objectif | Quelle proportion de chaque commune est couverte par la forêt ? Complément de l'objectif 1. |
| 2. Formule | Numérateur : surface forestière de la commune. Dénominateur : surface totale de la commune. Formule : KPI = (surface forestière / surface totale) × 100. Unité : %. |
| 3. Paramètres | Territoire : Haute-Garonne ; type de végétation ; millésime BD Forêt V2. |
| 4. Périmètre, période, granularité, fréquence | Haute-Garonne ; granularité : commune ; mise à jour selon les données IGN. |
| 5. Source et champs | IGN BD Forêt V2 : polygones forestiers et géométrie. IGN Admin Express : limites communales. Fiche : `docs/sources/fiche-BD-Foret-V2.md`. |
| 6. Lignes utilisables | Non vérifiées : fichiers géographiques à ouvrir. |
| 7. Proxy et biais | Utiliser les polygones forestiers IGN comme estimation de la couverture forestière. Biais : un millésime ancien peut surestimer ou sous-estimer la surface forestière actuelle. |
| 8. Décision éclairée | Compléter le classement des communes avec leur couverture forestière. |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** modifier les types de végétation inclus.

- Ce qui change : la surface forestière calculée et la comparaison entre communes.
- Ce qui ne change pas : les départs de feu historiques et les limites administratives.
- Décision : réexaminer les priorités si l'exposition forestière estimée change.

**RACER :**

- Relevant : complète l'analyse territoriale.
- Accepted : à confirmer avec le SDIS 31.
- Credible : dépend du millésime IGN.
- Easy : nécessite une jointure spatiale.
- Robust : sensible à la définition de la forêt.

**Garde-fous :**

- Afficher le millésime des données.
- Ne pas confondre couverture forestière et probabilité d'incendie.
- Vérifier les différences entre les dates des données géographiques.

---

# Objectif 2 — Mesurer la relation entre la Météo des forêts et les départs de feu

## KPI 2.1 (principal) — Taux de départs de feu par niveau de danger

| Champ | Valeur |
|---|---|
| 1. Question et objectif | À partir de quel niveau de danger de la Météo des forêts observe-t-on une hausse nette des départs de feu en Occitanie ? Objectif 2 de `docs/analyse/objectifs.md`. |
| 2. Formule | Numérateur : nombre de départs de feu enregistrés au niveau de danger étudié. Dénominateur : nombre de journées-départements correspondant à ce niveau. Formule : KPI = nombre de départs de feu / nombre de journées-départements du niveau. Unité : feux par journée-département. |
| 3. Paramètres | Niveaux : faible, modéré, élevé, très élevé ; période : au moins 3 années communes ; territoire : Occitanie. |
| 4. Périmètre, période, granularité, fréquence | Occitanie ; période proposée : 2024–2026 sous réserve de disponibilité ; granularité : département et jour ; recalcul après chaque saison. |
| 5. Source et champs | BDIFF : date, commune, département. Archives de la Météo des forêts : date, département, niveau de danger. Fiche : `docs/sources/fiche-BDIFF.md`. |
| 6. Lignes utilisables | Non vérifiées : exports à ouvrir. À mesurer : part des enregistrements avec date, département et niveau de danger permettant le croisement. |
| 7. Proxy et biais | Utiliser le danger départemental si le danger local exact manque. Biais : le danger réel au lieu de l'incendie peut être surestimé ou sous-estimé selon les conditions locales. |
| 8. Décision éclairée | Identifier le premier niveau de danger associé à une hausse nette des départs de feu et proposer un seuil de surveillance renforcée. |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** passer le seuil de déclenchement de « élevé » à « modéré ».

- Ce qui change : davantage de journées peuvent nécessiter une surveillance renforcée, ce qui augmente potentiellement les coûts.
- Ce qui ne change pas : la formule, les données historiques et les taux calculés pour chaque niveau.
- Décision : comparer les deux seuils avant de choisir celui qui correspond aux risques et aux moyens disponibles.

**RACER :**

- Relevant : directement lié au déclenchement de la surveillance.
- Accepted : à confirmer avec le SDIS 31.
- Credible : oui si les données météorologiques et les incendies sont correctement croisés.
- Easy : nécessite un regroupement par date, département et niveau.
- Robust : sensible à la qualité des données et aux années étudiées.

**Garde-fous :**

- Afficher le nombre de feux et le nombre de journées-départements par niveau.
- Ne pas comparer uniquement les nombres bruts de feux.
- Fixer la période avant l'analyse.
- Vérifier les niveaux représentés par peu de journées.
- Risque résiduel : la météo n'explique pas toutes les causes des départs de feu.

---

## KPI 2.2 (secondaire) — Part des journées nécessitant une surveillance renforcée

| Champ | Valeur |
|---|---|
| 1. Question et objectif | Combien de journées nécessiteraient une surveillance renforcée selon le seuil choisi ? Complément de l'objectif 2. |
| 2. Formule | Numérateur : nombre de journées-départements dont le danger est supérieur ou égal au seuil. Dénominateur : nombre total de journées-départements observées. Formule : KPI = (journées-départements au-dessus du seuil / journées-départements observées) × 100. Unité : %. |
| 3. Paramètres | Seuil : modéré, élevé ou très élevé ; période ; départements d'Occitanie. |
| 4. Périmètre, période, granularité, fréquence | Occitanie ; saison de la Météo des forêts ; granularité : département et jour ; calcul mensuel et annuel. |
| 5. Source et champs | Archives de la Météo des forêts : date, département, niveau de danger. |
| 6. Lignes utilisables | Non vérifiées : vérifier les dates et départements présents dans les archives. |
| 7. Proxy et biais | Utiliser les journées au-dessus du seuil comme estimation de la charge de surveillance. Biais : peut surestimer la mobilisation réelle si plusieurs zones sont couvertes par les mêmes équipes. |
| 8. Décision éclairée | Estimer la charge de surveillance et vérifier sa compatibilité avec les moyens du SDIS 31. |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** passer le seuil de « élevé » à « modéré ».

- Ce qui change : la part de journées nécessitant une surveillance augmente ou reste identique.
- Ce qui ne change pas : les archives, les dates et les départements étudiés.
- Décision : réévaluer les effectifs et les coûts avant de retenir le seuil.

**RACER :**

- Relevant : mesure la charge potentielle de surveillance.
- Accepted : à confirmer avec le SDIS 31.
- Credible : dépend de la complétude des archives.
- Easy : simple comptage par niveau de danger.
- Robust : dépend du seuil choisi.

**Garde-fous :**

- Afficher le nombre absolu de journées-départements avec le pourcentage.
- Distinguer les journées-départements des journées calendaires.
- Ne pas confondre journée au-dessus du seuil et intervention réelle.
- Vérifier les moyens humains et financiers disponibles.
