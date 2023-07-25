[
    {
      "name" : "backend",
      "image" : "${ecr_url}",
      "memory" : 1024,
      "cpu" : 512,
      "essential" : true,
      "entryPoint" : ["/"],
      "portMappings" : [
        {
          "containerPort" : 8000,
          "hostPort" : 8000
        }
      ]
    }
  ]
