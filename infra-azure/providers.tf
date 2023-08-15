terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.69.0"
    }
  }

#   cloud {
#     organization = "jvieira"


#     workspaces {
#       name = "captainofthesea"
#     }
#   }
}


provider "azurerm" {
  features {}
}