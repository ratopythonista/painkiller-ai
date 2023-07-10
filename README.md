# Painkiler AI

This application is a set of microservices to handle with medical patients health.

## usage

You can use this by having docker and docker compose installed and run those commands:

`docker-compose build; docker-compose up`

When the applications is up, you can access:

[Patient API](./patient/README.md) - http://localhost:8000/docs

Mesaure API - 

Jonas API -

You can also know more about wich one by clickling on the name.


## tests

In order to test the modules, you need to install the following:

`pip install pytest pytest-cov pytest-mock`

Then you can run:
    Patient API: `(cd patient; make install; pytest --cov-report term-missing  --cov-config=.coveragerc --cov=patient tests/)`
    Measurement API: `(cd measurement; make install; pytest --cov-report term-missing  --cov-config=.coveragerc --cov=measurement tests/)`
    Painkiller Package: `(cd painkiller; pip install .; pytest --cov-report term-missing  --cov-config=.coveragerc --cov=painkiller tests/)`

``