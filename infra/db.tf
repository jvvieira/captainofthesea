data "aws_secretsmanager_secret" "secrets" {
  arn = "arn:aws:secretsmanager:us-east-1:798616997032:secret:db_credentials-itNIU7"
}

data "aws_secretsmanager_secret_version" "current" {
  secret_id = data.aws_secretsmanager_secret.secrets.id
}

resource "aws_db_instance" "captainoftheseas" {
  allocated_storage   = 20
  engine              = "postgres"
  engine_version      = "15.3"
  identifier          = "captainoftheseas"
  instance_class      = "db.t3.micro"
  skip_final_snapshot = true
  storage_encrypted   = false
  publicly_accessible = false
  apply_immediately   = true
  multi_az            = false

  password = jsondecode(data.aws_secretsmanager_secret_version.current.secret_string)["password"]
  username = jsondecode(data.aws_secretsmanager_secret_version.current.secret_string)["username"]
  tags = {
    project = "captainofthesea"
  }
}
