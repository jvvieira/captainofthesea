# Captain of the sea

### Tech-stack
- Backend:
    - Python + FastAPI

- Backend:
    - IaC: Terraform
    - Cloud: AWS
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

### Project Deploy

#### Infrascructure
Run the following steps

- Login into AWS
```
aws configure
```

- Create the workspace
    ```
    cd infra
    terraform workspace new prod
    ```
- Update resources
    ```
    terraform apply
    ```

#### Backend
Run the following steps

- Create the env files
    ```
    cd backend
    poetry shell
    python ../scripts/setup_env.py prod
    ```
- Update the database
    ```
    alembic upgrade head
    ```
- Deploy a new Docker version
    ```
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 798616997032.dkr.ecr.us-east-1.amazonaws.com
    docker build -t captain-of-the-sea-backend-prod .
    docker tag captain-of-the-sea-backend-prod:latest 798616997032.dkr.ecr.us-east-1.amazonaws.com/captain-of-the-sea-backend-prod:latest
    docker push 798616997032.dkr.ecr.us-east-1.amazonaws.com/captain-of-the-sea-backend-prod:latest
    ```


#### Errors
-- Missing docker permission

```
sudo groupadd docker

sudo usermod -aG docker $USER

newgrp docker

```