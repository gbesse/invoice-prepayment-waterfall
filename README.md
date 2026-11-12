# invoice-prepayment-waterfall

## Français

Réconcilier acomptes soldes et arrondis en décimal exact.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m invoice_prepayment_waterfall examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Réconcilier acomptes soldes et arrondis en décimal exact : calcul déterministe sur entrées structurées, témoins et cas limites explicites.

### Limites

Modèle borné, données fictives, aucun service ou matériel de production validé. Méthodes classiques ; aucune supériorité SOTA générale ni adoption humaine démontrée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Reconcile prepayments balances and exact decimal rounding.

Synthetic data; no network access or secret required.

```sh
python -m invoice_prepayment_waterfall examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Reconcile prepayments balances and exact decimal rounding: deterministic computation over structured inputs, explicit witnesses and boundary cases.

### Limits

Bounded model and synthetic data; no production service or hardware validated. Classical methods; no general SOTA superiority or human adoption demonstrated.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Conciliar anticipos saldos y redondeos decimales exactos.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m invoice_prepayment_waterfall examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Conciliar anticipos saldos y redondeos decimales exactos: cálculo determinista con entradas estructuradas, testigos y casos límite explícitos.

### Límites

Modelo acotado y datos ficticios; ningún servicio ni hardware de producción validado. Métodos clásicos; sin superioridad SOTA general ni adopción humana demostrada.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.peppol.eu/poacc/billing/3.0/
- https://docs.python.org/3/library/decimal.html

## Projets voisins / Neighboring projects / Proyectos vecinos

FR : [invoice-credit-allocation](https://github.com/gbesse/invoice-credit-allocation) est un autre diagnostic du portefeuille. Ici : Réconcilier acomptes soldes et arrondis en décimal exact. Comparaison de périmètres seulement, sans affiliation ni benchmark de supériorité.

EN: [invoice-credit-allocation](https://github.com/gbesse/invoice-credit-allocation) is a different portfolio diagnostic. Here: Reconcile prepayments balances and exact decimal rounding. Scope comparison only, no affiliation or superiority benchmark.

ES: [invoice-credit-allocation](https://github.com/gbesse/invoice-credit-allocation) es otro diagnóstico del portafolio. Aquí: Conciliar anticipos saldos y redondeos decimales exactos. Comparación de alcance, sin afiliación ni benchmark de superioridad.
