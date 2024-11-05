# Kasten Kapitän 🍺

**Kasten Kapitän** ist eine Python-Flask-Webanwendung, die dabei hilft, das perfekte Bier zu Ihrem Lieblingsessen zu finden. Entdecken Sie, welche Biersorte zu verschiedenen Gerichten am besten passt, und lassen Sie sich von Kasten Kapitän inspirieren, um das perfekte Geschmackserlebnis zu kreieren!

## Funktionen

- **Gericht-Bier-Paarungen**: Erhalten Sie Empfehlungen für Biersorten, die zu verschiedenen Gerichten passen – von Pizza über Steak bis hin zu Desserts.
- **Match-Bewertung**: Jedes Gericht-Bier-Paar kommt mit einer prozentualen Bewertung, wie gut die beiden zusammenpassen.
- **Einfache Navigation**: Übersichtliche Anzeige und Auswahl für eine benutzerfreundliche Suche nach passenden Bier- und Essenskombinationen.

## Beispiel-JSON für Gericht-Bier-Paarungen

Die Anwendung verwendet JSON-Daten, um Biersorten und passende Gerichte zu speichern. Ein Beispiel:

```json
{
  "pairings": [
    {
      "beer": "Pils",
      "matches": [
        { "dish": "Pizza", "match_percentage": 95 },
        { "dish": "Sushi", "match_percentage": 85 }
      ]
    }
  ]
}
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
