 # Omnichain Analytics Backend

This project is all about tracking blockchain transactions across Ethereum, Solana, and XRP in real-time. Using Kafka, FastAPI, and PostgreSQL, we’re streaming data, analyzing trends, and setting up APIs for cool insights.

## Features
- Blockchain data integration (Ethereum, Solana, XRP)
- Real-time data streaming with Kafka
- FastAPI backend
- PostgreSQL & Snowflake storage
- Redis caching
- Analytics modules
- Airflow for scheduled ETL
- Dockerized deployment

## What I've been working so far? 
1. Connected to Ethereum, Solana, XRP for live transaction data
2. Kafka pipelines are up, streaming blockchain events
3. FastAPI backend with some functional endpoints
![image](https://github.com/user-attachments/assets/cbe0003f-daab-46d9-9f87-da33023c15e7)
4. PostgreSQL & Redis handling data storage + caching
5. Airflow DAGs ready for automation (logic still in progress)
6. Analytics modules in place—gas fees, token movement, arbitrage detection


## What's next?
1. Fine-tune fata ingestion & streaming
2. Improve API endpoints & analytics calculations
3. Add error handling & better logging
4. Maybe a simple UI (Streamlit or React(to learn how to use it))

## How to run this:
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Setup `.env` variables
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
