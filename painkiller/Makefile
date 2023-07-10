deploy:
	rm -rf dist/; pip install build; python -m build; pip install twine; python -m twine upload --repository testpypi dist/*