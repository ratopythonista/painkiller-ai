## About

This project is an package to handle with all database stuff needed on painkiller.

## DER

Following you can see the Diagram that represents the database.

![image](painkiller-ai-database.png)


### Conditionts

- Healthy
- High blood pressure
- Diabetes
- Heart disease
- Asthma
- Obesity
- Arthritis
- Alzheimer's
- Depression

### [Mesasurements](https://askthescientists.com/measuring-health/)

- Blood Pressure
- Heart Rate
- Breathing Rate
- Body Temperature
- Oxygen Saturation
- Blood Glucose
- Sleep
- Activity


### To use this package, you need to run the following command on any change.
`rm -rf dist/; pip install build; python -m build; pip install twine; python -m twine upload --repository testpypi dist/*`