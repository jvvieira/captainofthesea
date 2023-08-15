resource "azurerm_resource_group" "default" {
  name     = var.project_name
  location = var.location
}