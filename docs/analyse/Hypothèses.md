
# Hypothèses


### Question 1. Quelles sont les zones de Haute-Garonne les plus exposées aux départs de feux ?

**Hypothèse :**

Les zones les plus exposées aux départs de feux en Haute-Garonne seraient principalement les secteurs présentant une forte couverture végétale et forestière, associés à des conditions météorologiques favorables aux incendies (températures élevées, sécheresse et vent). Les zones situées à proximité des espaces agricoles et des zones habitées pourraient également être davantage exposées.

**Sources à mobiliser :**
- BDIFF : localisation historique des incendies et nombre de départs de feu.
- BD Forêt V2 : localisation et répartition des espaces forestiers.
- Corine Land Cover : occupation et utilisation des sols.
- Admin Express : délimitation des communes.
- AROME / ARPEGE : conditions météorologiques.
- PDPFCI : identification des zones à risque.

**Vérification :**
- Cartographier les départs de feu par commune.
- Calculer le nombre de départs de feu par commune et par année.
- Croiser les résultats avec la couverture forestière et les conditions météorologiques.

### Question 2. Quel est le lien entre le niveau de la Météo des forêts et les départs de feu réels ?

**Hypothèse :**

Plus le niveau de danger de la Météo des forêts est élevé, plus le nombre de départs de feu pourrait augmenter. Cependant, un niveau de danger élevé ne signifie pas systématiquement qu'un incendie va se déclarer, car les départs de feu dépendent également des activités humaines et d'autres facteurs environnementaux.

**Sources à mobiliser :**
- Météo des forêts : niveaux de danger et historique des prévisions.
- BDIFF : dates et localisations des départs de feu.
- AROME / ARPEGE : température, vent, humidité et précipitations.
- EFFIS : indices de risque et données sur les incendies.
- Copernicus Climate Data Store : données météorologiques et climatiques.

**Vérification :**
- Comparer le nombre de départs de feu pour chaque niveau de danger.
- Étudier les départs de feu par jour et par niveau de danger.
- Calculer le taux de départs de feu pour chaque niveau.
- Vérifier si les niveaux élevés correspondent à une augmentation des départs de feu.

### Question 3. Comment se comporte la Météo des forêts en Haute-Garonne par rapport à l'Occitanie et au reste de la France ?

**Hypothèse :**

La Haute-Garonne pourrait présenter une évolution du niveau de danger différente de celle observée dans les autres départements d'Occitanie et dans le reste de la France, en raison de ses caractéristiques géographiques, climatiques et de sa couverture végétale.

**Sources à mobiliser :**
- Météo des forêts : historique des niveaux de danger par département.
- AROME / ARPEGE : comparaison des conditions météorologiques.
- Copernicus Climate Data Store : historique climatique.
- Admin Express : délimitation des départements et régions.
- BDIFF : comparaison des départs de feu entre territoires.

**Vérification :**
- Calculer la fréquence de chaque niveau de danger en Haute-Garonne.
- Comparer les résultats avec les autres départements d'Occitanie.
- Comparer les résultats avec les moyennes nationales.
- Étudier les différences selon les saisons et les années.

---


### Question 4. Comment sont calculés les seuils actuels de déclenchement des dispositifs renforcés ?

**Hypothèse :**

Les seuils de déclenchement des dispositifs renforcés pourraient être définis à partir de plusieurs indicateurs combinant les conditions météorologiques, le niveau de danger incendie, l'état de la végétation et l'historique des incendies. Les décisions pourraient également tenir compte des caractéristiques locales du territoire et des moyens disponibles.

**Sources à mobiliser :**
- Météo des forêts : niveaux de danger.
- PDPFCI / PPFCI : stratégies départementales et plans de protection contre les incendies.
- Stratégie nationale de défense des forêts : cadre national de prévention et de lutte.
- Statistiques nationales des SDIS : organisation et moyens des services de secours.
- AROME / ARPEGE : paramètres météorologiques.

**Vérification :**
- Identifier les critères de déclenchement mentionnés dans les documents réglementaires et opérationnels.
- Comparer ces critères avec les niveaux de danger de la Météo des forêts.
- Vérifier si les seuils sont identiques ou adaptés selon les territoires.

### Question 5. Quelle superficie ou étendue de forêt est-elle perdue à chaque apparition des feux de forêt ?

**Hypothèse :**

La superficie brûlée varie fortement selon les incendies. La majorité des départs de feu pourraient entraîner des surfaces brûlées relativement limitées, tandis qu'un nombre plus faible de grands incendies pourrait représenter une part importante de la superficie totale détruite.

**Sources à mobiliser :**
- BDIFF : superficies brûlées et caractéristiques des incendies.
- EFFIS : cartographie et surfaces touchées par les grands incendies.
- NASA FIRMS : détection des anomalies thermiques et des points chauds.
- BD Forêt V2 : identification des surfaces forestières.
- Corine Land Cover : occupation des sols.

**Vérification :**
- Calculer la superficie moyenne brûlée par incendie.
- Comparer les superficies selon les années et les départements.
- Identifier les incendies les plus importants.
- Calculer la part de la superficie totale brûlée représentée par les grands incendies.

### Question 6. Combien de temps mettent les équipes en place pour détecter les départs des feux de forêt dans la région ?

**Hypothèse :**

Le temps de détection pourrait varier selon la localisation du départ de feu, l'accessibilité du terrain, la couverture du réseau de surveillance et les moyens technologiques disponibles. Les zones équipées de caméras de surveillance et de systèmes de détection automatique pourraient permettre une détection plus rapide que les zones isolées.

**Sources à mobiliser :**
- Pyronear : images de départs de feu et données liées aux caméras partenaires.
- Interventions SDIS : informations relatives aux interventions.
- Statistiques nationales des SDIS : organisation et moyens des services de secours.
- Carroyage DFCI 2 km : organisation géographique de la défense des forêts contre les incendies.
- Points de rencontre des secours et couverture téléphonique : accessibilité et couverture des territoires.
- BD TOPO : infrastructures et réseau routier.

**Vérification :**
- Étudier les horaires de détection, de signalement et d'intervention lorsqu'ils sont disponibles.
- Comparer les temps selon les zones géographiques.
- Identifier les territoires où les moyens de surveillance sont moins présents.

**Limite :** Les données d'images Pyronear et les statistiques d'intervention ne donnent pas nécessairement l'heure réelle de départ du feu ni l'heure de sa première détection. Pour calculer précisément un délai, il faudra disposer d'horodatages fiables.

---


### Question 7. À partir de quel niveau de danger de la Météo des forêts peut-on observer une hausse nette des départs de feu en Occitanie ?

**Hypothèse :**

Une augmentation significative du nombre de départs de feu pourrait être observée à partir du niveau de danger élevé, avec une augmentation potentiellement plus importante aux niveaux très élevé et extrême. Cette relation pourrait être plus marquée pendant les périodes estivales, lorsque les températures sont élevées et que la végétation est sèche.

**Sources à mobiliser :**
- Météo des forêts : niveaux de danger.
- BDIFF : historique des départs de feu en Occitanie.
- Interventions SDIS : interventions liées aux incendies.
- AROME / ARPEGE : conditions météorologiques.
- EFFIS : indices de risque incendie.

**Vérification :**
- Regrouper les départs de feu selon le niveau de danger.
- Calculer le nombre moyen de départs de feu par niveau.
- Comparer les fréquences entre les différents niveaux.
- Identifier le niveau à partir duquel la hausse devient statistiquement significative.

### Question 8. Comment peut-on renforcer la surveillance à partir du niveau de danger ?

**Hypothèse :**

L'intensité de la surveillance pourrait être progressivement renforcée en fonction du niveau de danger de la Météo des forêts. Lorsque le danger augmente, il serait pertinent d'augmenter la fréquence de surveillance des zones forestières sensibles, de mobiliser davantage de moyens humains et techniques et de renforcer la détection automatique des départs de feu.

**Sources à mobiliser :**
- Météo des forêts : niveaux de danger quotidiens.
- Pyronear : surveillance par caméras et détection automatique.
- PDPFCI / PPFCI : organisation de la prévention.
- Statistiques nationales des SDIS : moyens humains et matériels.
- Carroyage DFCI 2 km : organisation de la surveillance.
- Points de rencontre des secours et couverture téléphonique : capacités de communication et d'intervention.
- BD TOPO : infrastructures et accessibilité.

**Vérification :**
- Identifier les zones présentant les risques les plus importants.
- Comparer leur niveau de surveillance actuel avec leur niveau de danger.
- Identifier les secteurs insuffisamment couverts.
- Proposer des niveaux de surveillance adaptés à chaque niveau de danger.

### Question 9. Comment la fréquence mensuelle des départs de feu évolue-t-elle au cours de l'année ?

**Hypothèse :**

Les départs de feu ne sont probablement pas répartis de manière uniforme au cours de l'année. Leur fréquence pourrait augmenter pendant les mois les plus chauds et les plus secs, notamment entre juin et septembre, avec un pic potentiel pendant l'été. Cette évolution pourrait varier selon les départements et les conditions météorologiques de chaque année.

**Sources à mobiliser :**
- BDIFF : dates des départs de feu.
- Interventions SDIS : historique mensuel des interventions.
- Météo des forêts : évolution mensuelle du niveau de danger.
- AROME / ARPEGE : températures, précipitations et humidité.
- Copernicus Climate Data Store : données climatiques historiques.
- EFFIS : évolution temporelle des incendies.

**Vérification :**
- Regrouper les départs de feu par mois.
- Calculer le nombre moyen de départs de feu par mois sur plusieurs années.
- Identifier les mois présentant les fréquences les plus élevées.
- Comparer les résultats avec l'évolution mensuelle des niveaux de danger.

---

## 4. Tableau récapitulatif des hypothèses

| Personne | Question | Hypothèse principale |
|---|---|---|
| Dorra | Zones les plus exposées en Haute-Garonne | Les zones combinant une forte couverture forestière, des conditions météorologiques défavorables et une proximité avec les activités humaines seraient les plus exposées. |
| Dorra | Lien entre Météo des forêts et départs réels | Une augmentation du niveau de danger serait associée à une augmentation du nombre de départs de feu. |
| Dorra | Comparaison Haute-Garonne, Occitanie et France | La fréquence des niveaux de danger élevés varierait selon les caractéristiques géographiques et climatiques des territoires. |
| Ange | Calcul des seuils de déclenchement | Les seuils seraient déterminés à partir de plusieurs indicateurs météorologiques, environnementaux et opérationnels. |
| Ange | Superficie forestière perdue | La majorité des incendies pourraient brûler des surfaces limitées, tandis qu'un petit nombre de grands incendies représenterait une part importante des surfaces brûlées. |
| Ange | Temps de détection des équipes | Les délais de détection varieraient selon les équipements de surveillance, l'accessibilité et la localisation des départs de feu. |
| Mouad | Niveau de danger associé à une hausse des départs | Une hausse significative pourrait apparaître à partir du niveau de danger élevé. |
| Mouad | Renforcement de la surveillance | La surveillance pourrait être progressivement renforcée en fonction du niveau de danger et de la vulnérabilité des territoires. |
| Mouad | Fréquence mensuelle des départs | Les départs de feu seraient plus fréquents pendant les mois chauds et secs, notamment durant l'été. |

---

## 5. Points de vigilance

1. **Distinguer le nombre de départs de feu et le risque réel :** une commune possédant beaucoup de forêts peut avoir davantage de départs de feu sans nécessairement présenter le risque le plus élevé par hectare de forêt.

2. **Distinguer corrélation et causalité :** une augmentation des départs de feu lorsque le niveau de danger augmente ne signifie pas automatiquement que le niveau de danger provoque les incendies.

3. **Vérifier la disponibilité réelle des données :** les 39 sources du défi ne répondent pas toutes directement aux neuf questions. Certaines hypothèses nécessiteront des informations complémentaires, notamment pour les seuils opérationnels et les délais de détection.

4. **Ne pas considérer les hypothèses comme des conclusions :** chaque hypothèse devra être confirmée, nuancée ou infirmée à partir des résultats de l'analyse.
