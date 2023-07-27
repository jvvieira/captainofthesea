resource "aws_iam_role" "ecs_execution_role" {
  name = "ECSExecution"

  assume_role_policy = <<EOF
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                  "Service": "ecs-tasks.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
          }
      ]
  }
  EOF

  managed_policy_arns = [aws_iam_policy.assume_role_policy.arn, data.aws_iam_policy.AmazonECSTaskExecutionRolePolicy.arn]
  tags = {
    project = var.project_name
    env     = terraform.workspace
  }
}
