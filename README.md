# Labb - NoSQL
## Innehåll
Laborationen innehåller 3 delar (4 om man vill):


### 1. Redis (Real-Time State)
Vi använder Redis som en key-value store för att lagra det absolut senaste värdet från en sensor. Vi utforskar även TTL (Time To Live).

### 2. MongoDB (Flexibel Data)
Vi använder MongoDB för att lagra historik över sensor-events i ett dokumentformat. Detta visar flexibiliteten med schemalösa databaser.

### 3. Mini-Arkitektur (Simulering)
Vi kör ett Python-script (`sensor_sim.py`) som simulerar en sensor. Scriptet skickar data till både Redis (för realtidsstatus) och MongoDB (för historik).

### 4. SQLite Baseline
Vi börjar med att titta på hur sensordata hanteras i en traditionell SQL-databas. Vi definierar ett schema och gör enkla sökningar.


## Komma igång

### Starta databaserna
Använd Docker Compose för att starta Redis och MongoDB:
```bash
docker compose up -d
```

### Kör sensor-simuleringen
För att starta den simulerade sensorn i en container:
```bash
docker compose run --rm sensor-sim
```

### Utforska data
- **Redis:** `docker compose exec redis redis-cli`
- **MongoDB:** `docker compose exec mongo mongosh` (kör sedan `use iot` för att använda rätt databas)

## Filer i projektet
- `nosql_iot_lab.marp.md`: Presentationsbilder med detaljerade instruktioner för varje steg.
- `setup_sqlite.sql`: SQL-skript för att skapa tabell och sätta in testdata i SQLite.
- `sensor_sim.py`: Python-script som simulerar sensordata.
- `docker-compose.yml`: Konfiguration för att köra alla tjänster.
- `Dockerfile.sensor`: Instruktioner för att bygga containern till sensor-simuleringen.
- `requirements.txt`: Python-beroenden.
