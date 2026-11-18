| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Météo-France. Jeu de données « Archives de la Météo des forêts » sur data.gouv.fr, distinct de l'API temps réel décrite dans `fiche-météo_des_forêts.md`. |
| Mode d'accès et format | Téléchargement direct, sans compte : un fichier `csv.gz` par année (`mdf_2024.csv.gz`, `mdf_2025.csv.gz`, `mdf_2026.csv.gz`), plus un GeoJSON des départements, un zip d'échantillons et un PDF de présentation. |
| Grain (une ligne = ?) | Un département pour un jour : niveau de danger prévu à J+1 et à J+2. |
| Emprise géographique | France métropolitaine, échelle départementale (96 départements dans les fichiers 2024 et 2026, dont les 13 d'Occitanie). |
| Période réellement couverte | Fichier 2024 : du 3 juin au 30 septembre 2024 (120 jours). Fichier 2026 : du 28 mai au 5 octobre 2026. Fichier 2025 : non vérifié (non ouvert). Les années avant 2024 n'existent pas dans ce jeu. |
| Date de dernière mise à jour affichée sur la fiche | 5 octobre 2026 (fichier 2026) ; fichiers 2024 et 2025 mis à jour en juin 2026. |
| Fréquence de mise à jour | Quotidienne selon la fiche data.gouv.fr ; les données ne sont produites que pendant la saison estivale. |
| Volumétrie | `mdf_2024.csv.gz` : 40 Ko, 11 520 lignes ; `mdf_2026.csv.gz` : 50 Ko, 12 576 lignes (vérifié). |
| Clés disponibles | `num_dep` (code département), `nom_dep`, `date`. Format du code différent selon l'année : « 1 » en 2024, « 01 » en 2026. Séparateur `,` en 2024 et `;` en 2026. |
| Données personnelles | Aucune. |
| Licence | Licence Ouverte v2.0 (code `lov2` sur data.gouv.fr). |
| Questions de votre analyse auxquelles elle pourrait répondre | Q1 (seuil de déclenchement) : donne le niveau de danger quotidien par département, mais pas la méthode de calcul ni le seuil actuel du SDIS 31. Q2 à Q4 de l'analyse de groupe : base indispensable pour comparer la Haute-Garonne, l'Occitanie et la France, à croiser avec les départs de feu. |

**Remarques de vérification**
- Niveaux observés : de 1 à 4. Haute-Garonne en 2024 : 104 jours au niveau 1, 15 au niveau 2, 1 au niveau 3 (J+1). En 2026 : 26 jours au niveau 1, 70 au niveau 2, 31 au niveau 3, 4 au niveau 4. Les niveaux ne sont donc pas distribués de la même façon d'une année sur l'autre.
- Colonne `date` : horodatage UTC avec heure (ex. `2024-06-04T16:00:00Z`) : la date réelle de validité doit être précisée avant la jointure avec les feux.
- Seulement 2 à 3 saisons : trop court pour juger un seuil sur de longues séries.
