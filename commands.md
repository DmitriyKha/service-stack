### docker compose
```sh
docker compose -f docker-compose.dev2.yml up --build
docker compose -f docker-compose.dev2.yml stop
docker compose -f docker-compose.dev2.yml rm -v
docker compose -f docker-compose.dev2.yml down -v
```


### containter access & logs
```sh
docker exec -it some-mongo {bash, sh}
docker logs some-mongo 
```


### git commands
```sh
git checkout -b brance-name
git remote -v
git commit -S -m ""
git log --graph
```

### mongosh
```sh
docker exec -it container-name mongosh -u root -p example
# Current Mongosh Log ID:	69abf0071a624bc1778563b0
# Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.7.0
# Using MongoDB:		undefined
# Using Mongosh:		2.7.0
# test>
help
show databases
```
