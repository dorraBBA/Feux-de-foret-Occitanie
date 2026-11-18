| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Ministère de l'Intérieur, Direction générale de la sécurité civile et de la gestion des crises (DGSCGC). Données collectées chaque année auprès des services d'incendie et de secours (SDIS, BSPP, BMPM). Publiées sur data.gouv.fr (« Interventions réalisées par les services d'incendie et de secours »). |
| Mode d'accès et format | Téléchargement direct d'un fichier CSV par année (ex. `interventions2024.csv`), séparateur `;`. Pas d'API. |
| Grain (une ligne = ?) | Un service d'incendie et de secours (un département, plus BSPP et BMPM) pour une année. Les colonnes sont des compteurs d'interventions par type. |
| Emprise géographique | France entière : 99 lignes dans le fichier 2024 (96 départements, BSPP, BMPM, etc.). Les 13 départements d'Occitanie sont présents en 2024 (vérifié). |
| Période réellement couverte | Fichiers annuels de 2008 à 2024 (2024 et 2014 ouverts et vérifiés). Les années 2010, 2011 et 2012 : non vérifiées, fichiers non ouverts. |
| Date de dernière mise à jour affichée sur la fiche | 2 juillet 2026 (jeu de données) ; fichier 2024 mis à jour le 2 juillet 2026. |
| Fréquence de mise à jour | Annuelle (indiquée sur la fiche data.gouv.fr). |
| Volumétrie | Environ 30 Ko par fichier, 99 lignes et 71 colonnes par année (vérifié sur 2024 et 2014). |
| Clés disponibles | `Numéro` (code département, ex. 31 ; texte « BSPP » / « BMPM » pour Paris et Marseille), `Département`, `Région`, `Année`. Les noms de région changent avant 2016 (« Midi-Pyrénées », « Languedoc-Roussillon » en 2014, « Occitanie » en 2024) : joindre sur `Numéro`, pas sur `Région`. |
| Données personnelles | Aucune : ce sont des compteurs agrégés par département. |
| Licence | Licence Ouverte (code `fr-lo` sur data.gouv.fr). |
| Questions de votre analyse auxquelles elle pourrait répondre | Q2 (fréquence des feux) partiellement : colonne `Feux de végétations` par département et par an, dont la Haute-Garonne (403 en 2024, 604 en 2014). Elle ne distingue pas les feux de forêt des autres feux de végétation (herbe, broussailles). Colonne `Fausses alertes` utile pour la notion de fausse alerte. Rien sur les surfaces (Q3) ni sur les délais (Q4). |

**Remarques de vérification**
- Les fichiers ne sont pas tous au même format : 2014 et 2024 sont tous deux en encodage Windows (Latin-1) ; les milliers sont séparés par une espace (parfois un caractère spécial en 2024). Nettoyage nécessaire avant chargement.
- Le fichier ne contient ni date, ni mois, ni heure : impossible de croiser avec la Météo des forêts, qui est journalière.
