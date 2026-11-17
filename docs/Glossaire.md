# Glossaire — [Occitanie]

Dernière mise à jour : 2026-11-17



## Grain

**Définition :** Ce que représente une ligne dans un jeu de données

**Sources et colonnes :** Variables selon la source

<<<<<<< HEAD
**Divergences :** Le grain peut différer entre les sources. La ligne peut réprésenter un incendie dans une source et une commune dans l'autre
=======
**Divergences :** Le grain peut différer entre les sources
>>>>>>> f05bb1f2eafe9ad0e751f7e3e0973c18d831bea0

**Règle retenue :** Identifier systématiquement ce que représente une ligne

**Unité ou granularité :** Événement, commune, jour, année, etc

**Exemple :** Une ligne BDIFF = un incendie

**Statut :** proposé

**Origine de la définition :** https://www.getdbt.com/blog/guide-to-data-grain

**Ajouté par :** Ange-Samuel Brou, 2026-11-17


<<<<<<< HEAD



## Météo des forêts

**Définition :** Service de Météo-France informant le public du niveau de danger de feux de forêt et de végétation.

**Sources et colonnes :** [Météo des forêts - Météo-France](https://previ.meteofrance.com/meteo-des-forets) — niveau de danger par département.

**Divergences :** Aucune identifiée.

**Règle retenue :** Utiliser les 4 niveaux : faible, modéré, élevé, très élevé.

**Unité ou granularité :** Département / jour.

**Exemple :** Danger élevé dans l'Hérault.

**Statut :** proposé

**Origine de la définition :** Météo-France — Météo des forêts

**Ajouté par :** Ange-Samuel Brou, 2026-11-17




## Emprise

**Définition :** Étendue géographique couverte par un jeu de données.

**Sources et colonnes :** [CNIG - La donnée géolocalisée](https://cnig.gouv.fr/la-donnee-geolocalisee-r21398.html)

**Divergences :** L'emprise varie selon la source et son territoire couvert.

**Règle retenue :** Indiquer le territoire réellement couvert par les données.

**Unité ou granularité :** Commune, département, région, France, etc.

**Exemple :** Emprise : région Occitanie.

**Statut :** proposé

**Origine de la définition :** CNIG — standards et métadonnées des données géographiques.

**Ajouté par :** Ange-Samuel Brou, 2026-11-17


## Guet

**Définition :** Surveillance d'un territoire permettant de détecter rapidement les départs de feu.

**Sources et colonnes :** [Ministère de l'Intérieur - Lutte contre les feux de forêt](https://www.interieur.gouv.fr/fr/Espace-presse/Dossiers-de-presse/Proteger-les-populations-les-biens-et-l-environnement-contre-les-feux-de-foret)

**Divergences :** Le guet peut être fixe, mobile ou assuré par différents moyens de surveillance.

**Règle retenue :** Surveillance destinée à détecter et signaler rapidement un départ de feu.

**Unité ou granularité :** Zone / dispositif de surveillance.

**Exemple :** Surveillance d'un massif forestier pendant la saison estivale.

**Statut :** proposé

**Origine de la définition :** Ministère de l'Intérieur — stratégie nationale de lutte contre les feux de forêt.

**Ajouté par :** Ange-Samuel Brou, 2026-11-17
=======
## Météo des forêts

**Définition :** Indicateur du niveau de danger de départ de feu

**Sources et colonnes :** Données Météo-France

**Divergences :** Les niveaux de danger et les critères de calcul peuvent varier

**Règle retenue :** Identifier les niveaux et les critères de calcul

**Unité ou granularité :** Niveau de danger par jour et par zone

**Exemple :** Une zone est classée en danger élevé

**Statut :** à vérifier

**Origine de la définition :** Données Météo-France

**Ajouté par :** Dorra Boucharbia, 2026-11-17


## Fausse alerte

**Définition :** Alerte de danger élevé sans départ de feu constaté

**Sources et colonnes :** Données Météo-France et BDIFF

**Divergences :** La définition et les critères de mesure peuvent varier

**Règle retenue :** Définir les critères permettant d'identifier une fausse alerte

**Unité ou granularité :** Alerte par jour et par zone

**Exemple :** Danger élevé annoncé sans incendie enregistré

**Statut :** à vérifier

**Origine de la définition :** Analyse du besoin métier

**Ajouté par :** Dorra Boucharbia, 2026-11-17


## Départ de feu

**Définition :** Début d'un incendie dans un espace naturel ou forestier

**Sources et colonnes :** Base de données BDIFF

**Divergences :** Les types de feux pris en compte peuvent varier

**Règle retenue :** Identifier les types de feux concernés par l'étude

**Unité ou granularité :** Événement

**Exemple :** Une ligne BDIFF = un incendie

**Statut :** à vérifier

**Origine de la définition :** Données BDIFF

**Ajouté par :** Dorra Boucharbia, 2026-11-17


## Dispositif renforcé

**Définition :** Moyens supplémentaires de patrouille et de surveillance contre les incendies

**Sources et colonnes :** Données opérationnelles des services de secours, si disponibles

**Divergences :** Les moyens et les coûts peuvent varier selon les territoires

**Règle retenue :** Identifier les moyens mobilisés et leurs coûts

**Unité ou granularité :** Dispositif par zone et par période

**Exemple :** Déploiement de patrouilles supplémentaires en période de risque élevé

**Statut :** à vérifier

**Origine de la définition :** Analyse du besoin métier

**Ajouté par :** Dorra Boucharbia, 2026-11-17


## Seuil de déclenchement

**Définition :** Niveau de danger à partir duquel le dispositif de surveillance est renforcé

**Sources et colonnes :** Données Météo-France et données opérationnelles

**Divergences :** Le seuil peut varier selon les territoires

**Règle retenue :** Identifier le seuil actuellement utilisé

**Unité ou granularité :** Niveau de danger

**Exemple :** Le niveau de danger élevé déclenche des patrouilles supplémentaires

**Statut :** à vérifier

**Origine de la définition :** Analyse du besoin métier

**Ajouté par :** Dorra Boucharbia, 2026-11-17


## Emprise géographique

**Définition :** Territoire couvert par une étude ou un jeu de données

**Sources et colonnes :** Données géographiques, BDIFF et Météo-France

**Divergences :** Les échelles géographiques peuvent varier selon les sources

**Règle retenue :** Identifier les limites géographiques et harmoniser les échelles

**Unité ou granularité :** Commune, département, région

**Exemple :** Région Occitanie

**Statut :** à vérifier

**Origine de la définition :** Analyse du besoin métier

**Ajouté par :** Dorra Boucharbia, 2026-11-17

>>>>>>> f05bb1f2eafe9ad0e751f7e3e0973c18d831bea0
