# Captain of the sea

### Tech-stack
- Backend:
    - Python + FastAPI

- Backend:
    IaC: Terraform
    Cloud: AWS
        - Services
            Postgres RDS
            AWS ECR
            AWS ECS + Fargate


### Running the project
- Install Poetry[https://python-poetry.org/docs/]
- Install all the Python libs
    ```
    cd backend
    poetry install
    ```
- Create env files
    ```
    cd scripts
    python3 setup_env.py dev
    ```
- Run Docker
    ```
    docker compose up
    ```
