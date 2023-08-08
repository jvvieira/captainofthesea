module "alb" {
  source  = "terraform-aws-modules/alb/aws"
  version = "~> 8.0"

  name = format("prod-lb-%s", var.project_name)

  load_balancer_type = "application"

  vpc_id          = aws_vpc.main.id
  subnets         = [for subnet in aws_subnet.public_subnets : subnet.id]
  security_groups = [aws_security_group.load_balancer.id]

  http_tcp_listeners = [
    {
      port               = 80
      protocol           = "HTTP"
      target_group_index = 0
    },
  ]

  target_groups = [
    {
      name             = "${terraform.workspace}-${var.api_container_name}"
      backend_protocol = "HTTP"
      backend_port     = 8000
      target_type      = "ip"
    },
  ]

  tags = {
    project = var.project_name
    env     = terraform.workspace
  }
}



# resource "aws_lb" "lb" {
#   name               = format("prod-lb-%s", var.project_name)
#   internal           = false
#   load_balancer_type = "application"
#   security_groups    = [aws_security_group.load_balancer.id]
#   subnets            = [for subnet in aws_subnet.public_subnets : subnet.id]

#   enable_deletion_protection = false

#   tags = {
#     project = var.project_name
#     env     = terraform.workspace
#   }
# }

# resource "aws_lb_target_group" "test" {
#   name     = "tf-example-lb-tg"
#   port     = 80
#   protocol = "HTTP"
#   vpc_id   = aws_vpc.main.id
# }


# resource "aws_lb_listener" "lb_http" {
#   load_balancer_arn = aws_lb.lb.arn
#   port              = "80"
#   protocol          = "HTTP"

#   default_action {
#     type = "redirect"

#     redirect {
#       port        = "443"
#       protocol    = "HTTPS"
#       status_code = "HTTP_301"
#     }
#   }
# }
