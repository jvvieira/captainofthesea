resource "aws_db_instance" "captainoftheseas" {
  allocated_storage   = 20
  engine              = "postgres"
  engine_version      = "15.3"
  identifier          = format("%s-%s", var.project_name, terraform.workspace)
  db_name             = format("%s-%s", var.project_name, terraform.workspace)
  instance_class      = "db.t3.micro"
  skip_final_snapshot = true
  storage_encrypted   = false
  publicly_accessible = true
  apply_immediately   = true
  multi_az            = false

  password = data.aws_ssm_parameter.password.value
  username = data.aws_ssm_parameter.user.value

  tags = {
    project = var.project_name
    env     = terraform.workspace
  }
}
