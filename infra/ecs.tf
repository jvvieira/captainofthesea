resource "aws_kms_key" "ecs_key" {
  description             = var.project_name
  deletion_window_in_days = 7
}

resource "aws_cloudwatch_log_group" "ecs_log_group" {
  name = var.project_name
}


resource "aws_ecs_cluster" "cluster" {
  name = var.project_name

  configuration {
    execute_command_configuration {
      kms_key_id = aws_kms_key.ecs_key.arn
      logging    = "OVERRIDE"

      log_configuration {
        cloud_watch_encryption_enabled = true
        cloud_watch_log_group_name     = aws_cloudwatch_log_group.ecs_log_group.name
      }
    }
  }

  tags = {
    project = var.project_name
    env     = terraform.workspace
  }
}


resource "aws_ecs_cluster_capacity_providers" "spot" {
  cluster_name = aws_ecs_cluster.cluster.name

  capacity_providers = ["FARGATE_SPOT", "FARGATE"]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = "FARGATE_SPOT"
  }
}


resource "aws_ecs_service" "ecs_service" {
  name            = format("%s-backend", var.project_name)
  cluster         = aws_ecs_cluster.cluster.id
  task_definition = aws_ecs_task_definition.backend.arn

  capacity_provider_strategy {
    capacity_provider = "FARGATE_SPOT"
    weight = 1
  }

  network_configuration {
    subnets          = [for s in data.aws_subnet.subnet : s.id]
    assign_public_ip = true
  }

  desired_count = 1

  tags = {
    project = var.project_name
    env     = terraform.workspace
  }
}


data "template_file" "container_definitions" {
  template = file("./task-definitions/backend.tpl")
  vars = {
    "ecr_url": aws_ecr_repository.backend.repository_url
  }
}

resource "aws_ecs_task_definition" "backend" {
  family                   = format("%s-backend", var.project_name)
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  memory                   = "1024"
  cpu                      = "512"
  execution_role_arn       = "arn:aws:iam::798616997032:role/ECSExecutionRole"
  container_definitions    = data.template_file.container_definitions.rendered

  tags = {
    project = var.project_name
    env     = terraform.workspace
  }
}
