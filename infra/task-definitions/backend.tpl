[
    {
      "name" : "${container_name}",
      "image" : "${ecr_url}",
      "memory" : 1024,
      "cpu" : 512,
      "essential" : true,
      "portMappings" : [
        {
          "containerPort" : 8000,
          "hostPort" : 8000
        }
      ]
    }
  ]
