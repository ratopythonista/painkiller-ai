## About

This project is an microservice that handles with patient measurement data.

### Usage

To use this service you need to install using:
`pip install -e . --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/`

Then run with:
`uvicorn main:app --host 0.0.0.0 --port 8000`

### [Mesasurements](https://askthescientists.com/measuring-health/)

- Blood Pressure
- Heart Rate
- Breathing Rate
- Body Temperature
- Oxygen Saturation
- Blood Glucose
- Sleep
- Activity
