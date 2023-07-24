# resource "aws_lb" "alb" {
#   name               = var.project_name
#   internal           = false
#   load_balancer_type = "application"
#   security_groups    = ["sg-02194f9a9c7a93183"]
#   subnets            = [for s in data.aws_subnet.subnet : s.id]

#   enable_deletion_protection = true

#   tags = {
#     project = var.project_name
#     env     = terraform.waorkspace
#   }
# }


# resource "aws_lb_target_group" "alb-example" {
#   name        = var.project_name
#   target_type = "alb"
#   port        = 80
#   protocol    = "TCP"
#   vpc_id      = var.vpc_id
# }
