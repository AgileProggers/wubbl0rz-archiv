<div align="center" width="100%">
    <img src="https://raw.githubusercontent.com/AgileProggers/archiv-frontend/master/static/favicon.ico" width="128"/>
</div>

<div align="center" width="100%">
    <h2>wubbl0rz VOD Archiv</h2>
    <p>Stack: Go, Gin, Gorm, FFmpeg</p>
</div>

## 🐳 Deploy

Copy `.env.sample` to `.env` and replace the required variables.

### Example `docker-compose.yml`

```
version: '3'
services:
  api:
    container_name: archiv-api
    build: .
    restart: unless-stopped
    env_file: .env
    ports:
      - 127.0.0.1:5000:5000
    volumes:
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
      - /path/to/media/:/var/www/media/
    depends_on:
      - db
  db:
    container_name: archiv-db
    image: postgres:15-alpine
    restart: unless-stopped
    env_file: .env
    volumes:
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
      - /path/to/postgres/:/var/lib/postgresql/data
```

## 🚪 Reverse Proxy

The easiest way is to use caddy. Paste the following into a file called `Caddyfile`.

```
api.wubbl0rz.tv {
    reverse_proxy localhost:5000
    encode gzip
    header Access-Control-Allow-Origin "*"
}
```

## Backup and restore database

Required to upgrade major postgres versions.

**Backup**
`docker exec -t archiv-db pg_dumpall -c -U YOUR_DB_USER > /path/to/backup/dump_$(date +%Y-%m-%d"_"%H_%M_%S).sql`

**Restore**
`docker exec -i archiv-db psql -d YOUR_DB_NAME -U YOUR_DB_USER < /path/to/backup/dump_<some-date>.sql`

## Documentation

Check out [the swagger page](https://api.wubbl0rz.tv/swagger/index.html) for more documentation.
