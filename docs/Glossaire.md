# Glossaire — [Occitanie]

Dernière mise à jour : 2026-11-17

## SDIS

**Définition** : Service Départemental d'Incendie et de Secours, chargé des opérations de secours et de la lutte contre les incendies.

**Sources et colonnes** : Données et statistiques des SDIS.

**Divergences** : Les moyens et les méthodes d'intervention peuvent varier selon les départements.

**Règle retenue** : Identifier le SDIS concerné et son département.

**Unité ou granularité** : Département.

**Exemple** : Le SDIS 31 intervient en Haute-Garonne.

**Statut** : validé

**Origine de la définition** : Services départementaux d'incendie et de secours.

**Ajouté par** : Mouad Arahal, 2026-11-17


## Météo des forêts

**Définition** : Indicateur de Météo-France qui informe sur le niveau de danger de feu de forêt.

**Sources et colonnes** : Météo-France, niveaux de danger par département et par jour.

**Divergences** : Le niveau de danger varie selon les conditions météorologiques et les territoires.

**Règle retenue** : Utiliser les niveaux officiels de Météo-France.

**Unité ou granularité** : Département et jour.

**Exemple** : Un département est classé en danger élevé.

**Statut** : validé

**Origine de la définition** : Météo-France.

**Ajouté par** : Mouad Arahal, 2026-11-17


## Seuil de déclenchement

**Définition** : Niveau de danger à partir duquel des mesures supplémentaires de surveillance sont mises en place.

**Sources et colonnes** : Données de danger de feu et règles opérationnelles du SDIS.

**Divergences** : Le seuil peut varier selon les territoires et les moyens disponibles.

**Règle retenue** : Déterminer un seuil adapté à partir des données analysées.

**Unité ou granularité** : Niveau de danger.

**Exemple** : Renforcer la surveillance lorsque le danger atteint un niveau défini.

**Statut** : à définir

**Origine de la définition** : Analyse du besoin du SDIS.

**Ajouté par** : Mouad Arahal, 2026-11-17


## Patrouilles

**Définition** : Équipes qui se déplacent pour surveiller les zones à risque et détecter les départs de feu.

**Sources et colonnes** : Informations opérationnelles du SDIS sur les moyens de surveillance.

**Divergences** : La fréquence et les zones de patrouille peuvent varier selon le risque.

**Règle retenue** : Adapter les patrouilles aux zones et aux périodes les plus exposées.

**Unité ou granularité** : Patrouille, zone et période.

**Exemple** : Une équipe surveille une zone forestière pendant une journée à risque.

**Statut** : validé

**Origine de la définition** : Organisation de la surveillance des incendies.

**Ajouté par** : Mouad Arahal, 2026-11-17


## Guet

**Définition** : Surveillance depuis un point d'observation pour repérer rapidement les départs de feu.

**Sources et colonnes** : Informations sur les dispositifs de surveillance des incendies.

**Divergences** : Les dispositifs de guet peuvent être différents selon les départements.

**Règle retenue** : Identifier les points d'observation et les périodes de surveillance.

**Unité ou granularité**: Point d'observation et période.

**Exemple** : Un agent surveille une forêt depuis un poste de guet.

**Statut** : validé

**Origine de la définition** : Dispositifs de prévention des incendies.

**Ajouté par** : Mouad Arahal, 2026-11-17


## Grain

**Définition :** Ce que représente une ligne dans un jeu de données

**Sources et colonnes :** Variables selon la source

**Divergences :** Le grain peut différer entre les sources

**Règle retenue :** Identifier systématiquement ce que représente une ligne

**Unité ou granularité :** Événement, commune, jour, année, etc

**Exemple :** Une ligne BDIFF = un incendie

**Statut :** validé

**Origine de la définition :** Glossaire Data

**Ajouté par :** Ange-Samuel Brou, 2026-11-17


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

