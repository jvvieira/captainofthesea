resource "aws_ssm_parameter" "db_address" {
  name        = format("/%s/database/endpoint", terraform.workspace)
  description = "Database Endpoint"
  type        = "SecureString"
  value       = aws_db_instance.captainoftheseas.endpoint

  tags = {
    environment = terraform.workspace
    project     = var.project_name
  }
}

resource "aws_ssm_parameter" "db_name" {
  name        = format("/%s/database/db", terraform.workspace)
  description = "Database Name"
  type        = "SecureString"
  value       = aws_db_instance.captainoftheseas.db_name

  tags = {
    environment = terraform.workspace
    project     = var.project_name
  }
}

data "aws_ssm_parameter" "user" {
  name = format("/%s/database/user", terraform.workspace)
}

data "aws_ssm_parameter" "password" {
  name = format("/%s/database/password", terraform.workspace)
}
