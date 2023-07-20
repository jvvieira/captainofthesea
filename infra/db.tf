resource "aws_db_instance" "captainoftheseas" {
  allocated_storage   = 20
  engine              = "postgres"
  engine_version      = "15.3"
  identifier          = format("%s-%s", var.project_name, terraform.workspace)
  instance_class      = "db.t3.micro"
  skip_final_snapshot = true
  storage_encrypted   = false
  publicly_accessible = false
  apply_immediately   = true
  multi_az            = false

  password = jsondecode(data.aws_secretsmanager_secret_version.current.secret_string)["password"]
  username = jsondecode(data.aws_secretsmanager_secret_version.current.secret_string)["username"]
  tags = {
    project = var.project_name
    env = terraform.workspace
  }
}
