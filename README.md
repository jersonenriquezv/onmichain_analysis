# Omnichain Analytics Backend

A scalable backend system for aggregating and analyzing real-time blockchain transaction data from Ethereum, Solana, and XRP. Features real-time streaming, analytics, and robust API endpoints.

## Features
- Blockchain data integration (Ethereum, Solana, XRP)
- Real-time data streaming with Kafka
- FastAPI backend
- PostgreSQL & Snowflake storage
- Redis caching
- Analytics modules
- Airflow for scheduled ETL
- Dockerized deployment

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables in `.env`
4. Run services with Docker Compose: `docker-compose up --build`

## Directory Structure
- `connectors/` - Blockchain connectors
- `streaming/` - Kafka producers/consumers
- `analytics/` - Analytics modules
- `api/` - FastAPI app
- `db/` - Database integrations
- `airflow/` - Airflow DAGs
- `docker/` - Dockerfiles and compose
- `tests/` - Tests

## Deployment
- Dockerized for local and cloud deployment
- AWS Lambda ready 