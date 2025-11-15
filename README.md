# BiasSphere

## Overview
This project was created as part of Holistic AI's Great Agent Hack November 2025. BiasSphere is a lightweight application for visualising and analysing bias in news articles.

## Installation
```bash
git clone https://github.com/yourusername/BiasSphere.git
cd BiasSphere
```

## Pre-requisites
- **uv**: This repository uses `uv` for package management
    - Run `uv sync --group=all` to install all dependencies
- **poetry**: Poetry is used for dependency management and packaging
    - Install Poetry by following the instructions at https://python-poetry.org/docs/#installation
    - Use `poetry sync` to install project dependencies
- **pre-commit**: Pre-commit runs code linting, type checking, and dependency management, to ensure code quality and clean code
    - Install pre-commit hooks using `uv add tool pre-commit` and `pre-commit install`

## Usage
```bash
poetry run sync 
```
### Start backend API server
```bash
poetry run uvicorn api.app:app --reload
```
### Start frontend
```bashbash
uv run python3 src/frontend/main.py
```

## Features
- Visualisation of bi

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

- Create a new branch `feat/_short_description_of_feature_
- Create a PR with a description of changes made

## Contact
For questions or feedback, please open an issue.