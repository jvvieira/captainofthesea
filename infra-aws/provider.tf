terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  backend "s3" {
    bucket = "captainofthesea-tfstate"
    key    = "captain/terraform.tfstate"
    region = "us-east-1"
  }

  required_version = ">= 1.2.0"
}


provider "aws" {
  region = var.AWS_REGION
}
