| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Météo-France. Données produites à partir des prévisions météorologiques et de l'état de sécheresse de la végétation. |
| Mode d'accès et format | API REST avec authentification via un compte sur le portail API Météo-France. Données disponibles au format CSV et images PNG pour les cartes. |
| Grain (une ligne = ?) | Une ligne du fichier CSV correspond à un département et à son niveau de danger prévu pour une journée (J+1 ou J+2). |
| Emprise géographique | France, à l'échelle départementale. |
| Période réellement couverte | Archives disponibles depuis 2024. Les prévisions en temps réel concernent J+1 et J+2 pendant la saison estivale (juin à septembre). |
| Date de mise à jour affichée sur la fiche | 24 septembre 2026 (dernière mise à jour affichée dans le catalogue data.gouv.fr de l'API). |
| Fréquence de mise à jour | Quotidienne à 17 h pendant la saison estivale (juin à septembre). Des mises à jour exceptionnelles peuvent avoir lieu entre deux diffusions. |
| Volumétrie | Moins de 2 Mo pour le flux temps réel dans le cas général. |
| Clés disponibles | `Reference_time` (date et heure de production), `dep_code` (code département), `nom_dep` (nom département), `niveau_j1` (danger à J+1), `niveau_j2` (danger à J+2). |
| Données personnelles | Aucune donnée personnelle identifiée. |
| Licence | Licence Ouverte Etalab, sans redevance selon la documentation de Météo-France. Attention : la fiche API data.gouv.fr affiche actuellement « Licence non renseignée ». |