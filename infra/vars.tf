variable "AWS_REGION" {
  default = "us-east-1"
}

variable "project_name" {
  type    = string
  default = "captain-of-the-sea"
}

variable "db_name" {
  type    = string
  default = "captainofthesea"
}

variable "api_container_name" {
  type    = string
  default = "captainofthesea"
}
