# Painkiler AI

This application is a set of microservices to handle with medical patients health.

## usage

You can use this by having docker and docker compose installed and run those commands:

`docker-compose build; docker-compose up`

When the applications is up, you can access:

[Patient API](./patient/README.md) - http://localhost:8080/docs

[Mesaure API](./measurement/README.md) - http://localhost:8081/docs

Jonas API
    - FileSystem Console: http://localhost:9001

You can also know more about wich one by clickling on the name.

In order to have database pre poluated to use Jonas API, you can run with the compose up:

`docker cp ./scripts/populate.sql painkiller-database:populate.sql; docker exec -it painkiller-database psql -U painkiller -d postgres -f populate.sql`


## tests

In order to test the modules, you need to install the following:

`pip install pytest pytest-cov pytest-mock`

Then you can run:
    Patient API: `(cd patient; make install; pytest --cov-report term-missing  --cov-config=.coveragerc --cov=patient tests/)`
    Measurement API: `(cd measurement; make install; pytest --cov-report term-missing  --cov-config=.coveragerc --cov=measurement tests/)`
    Painkiller Package: `(cd painkiller; pip install .; pytest --cov-report term-missing  --cov-config=.coveragerc --cov=painkiller tests/)`
    Jonas API: `(cd jonas; make install; pytest --cov-report term-missing  --cov-config=.coveragerc --cov=jonas tests/)` 

``