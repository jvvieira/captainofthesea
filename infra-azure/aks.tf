# resource "azurerm_kubernetes_cluster" "default" {
#   name                = "${random_pet.prefix.id}-aks"
#   location            = azurerm_resource_group.default.location
#   resource_group_name = azurerm_resource_group.default.name
#   dns_prefix          = "${random_pet.prefix.id}-k8s"
#   kubernetes_version  = "1.26.3"

#   default_node_pool {
#     name            = "default"
#     node_count      = 1
#     vm_size         = "Standard_D2_v2"
#     os_disk_size_gb = 30
#   }

#   service_principal {
#     client_id     = var.appId
#     client_secret = var.password
#   }

#   role_based_access_control_enabled = true

#   tags = {
#     environment = "Demo"
#   }
# }