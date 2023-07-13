resource "aws_ssm_parameter" "db_address" {
  name        = "/database/endpoint"
  description = "Database Endpoint"
  type        = "SecureString"
  value       = aws_db_instance.captainoftheseas.endpoint

  tags = {
    environment = "production"
    project = "captainofthesea"
  }
}
