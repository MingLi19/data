
```mermaid
erDiagram
    Company ||--o{ User : has
    Company ||--o{ Vessel : has
    Vessel ||..|{ Equipment : has
    Vessel ||--|| VesselType : is
    Vessel ||--|| TimeZone : is
    Equipment ||--|{ FuelType : is
    Vessel ||--|{ PowerSpeedCurve : has
```
