# MAL Anime & Manga List Scraper Pipeline

Uses Airflow 2.5.0

## Setup

For comprehensive setup, see [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#)

1. `mkdir -p ./dags ./logs ./plugins ./data`
2. `echo -e "AIRFLOW_UID=$(id -u)" > .env`
3. `docker compose up airflow-init`
4. `docker-compose up`

See `http://localhost:8080` afterwards and use `airflow` as the username and password

Use `docker-compose down --volumes` for cleaninh-up

## Oldies README

usage:

1. user-link-scraper: get 20 online users links from ```/users```
2. user-link-deduplication: online users last longer than scraping session, so there's possible chance of duplication in scraping. deduplication erases duplicated record.
3. extract-profile: extract anime and manga stats from user profile
4. check-list-access: checks whether anime and manga list could be accessed. case when it can't include badresult (private list) or incompatible data table

data flow (in csv):

```link (dedup) -> all profile -> filtered profile (anime & manga days > 1) -> username -> access (inaccessible marked) -> offset -> lists```
)
etc

- extract-online-users: manual javascript extractor
