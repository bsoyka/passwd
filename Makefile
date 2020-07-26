github:
	@sphinx-build -M html source build
	@python githubcopy.py
