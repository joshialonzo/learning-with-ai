## Main prompt

Create a “Tutorial 0” to configure the local Python virtual environment using uv and Python 3.12. Then, use that tutorial to build a FastAPI project with Docker, Docker Compose, PostgreSQL for the database, Redis for the cache, and Infisical for secrets management. I need to configure the project to retrieve the secrets from the Infisical project and write them to a local config.yaml file. I want to translate all these into environment variables in the Docker and Docker-Compose projects. Write several tutorials, starting with tutorial 0, each one with integration tests to verify that the integration of a new technology is working correctly. Each tutorial should build on the previous one by adding a new technology and end-to-end tests.

## Secondary prompt

Rewrite the tutorials following this order:

1. uv and project configuration
2. FastAPI application
3. Dockerization
4. Docker Compose
5. PostgreSQL
6. Redis
7. Infisical
8. e2e testing