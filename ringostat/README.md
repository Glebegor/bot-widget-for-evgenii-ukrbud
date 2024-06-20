# Ringostat app

## Config

### .env
```env
DB_PASSWORD = "123321"
DB_ADMIN_PASSWORD = "123321"

SECRET_KEY = "secret_key"
```

### config.yml
```yml
db:
  User: "postgres"
  Name: "main"
  Admin: "admin"

server:
  Port: "8080"
  Host: "localhost"
  Debug: "true"
```

### main.db
You just need to create main db in root directory of the project with name that you wrote in config.