resource "aws_ecr_repository" "backend" {
  name                 = format("%s-backend-%s", var.project_name, terraform.workspace)
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    project = var.project_name
    env     = terraform.workspace
  }
}
