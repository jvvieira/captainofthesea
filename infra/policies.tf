resource "aws_iam_policy" "assume_role_policy" {
  name = "assume-role"
  path = "/"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement : [
      {
        "Sid" : "VisualEditor0",
        "Effect" : "Allow",
        "Action" : [
          "sts:AssumeRole",
          "iam:PassRole"
        ],
        "Resource" : "*"
      }
    ]
  })

  tags = {
    project = var.project_name
    env     = terraform.workspace
  }
}



data "aws_iam_policy" "AmazonECSTaskExecutionRolePolicy" {
  arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}
