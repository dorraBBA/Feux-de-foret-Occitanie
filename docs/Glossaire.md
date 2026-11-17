# Glossaire — [Occitanie]

Dernière mise à jour : 2026-11-17



## Grain

**Définition :** Ce que représente une ligne dans un jeu de données.

**Sources et colonnes :** Variables selon la source.

**Divergences :** Le grain peut différer entre les sources. La ligne peut réprésenter un incendie dans une source et une commune dans l'autre

**Règle retenue :** Identifier systématiquement ce que représente une ligne.

**Unité ou granularité :** Événement, commune, jour, année, etc.

**Exemple :** Une ligne BDIFF = un incendie.

**Statut :** proposé

**Origine de la définition :** https://www.getdbt.com/blog/guide-to-data-grain

**Ajouté par :** Ange-Samuel Brou, 2026-11-17





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