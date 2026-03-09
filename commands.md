100** app
10011 - backend
10012 - jupyter

100** DB access
10021 - adminer
10022 - mongo-exspress


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


git fetch -p # удаляет ссылки на несуществующие ветки в удаленном
git branch -r # ветки в удаленных
git push repo --delete branch # удаление ветки в удаленном


git rm -r --cached src/app/.ipynb_checkpoints/
git restore --staged .

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
### alembic
```sh
alembic init alembic


alembic revision --autogenerate -m "initial"
alembic upgrade head
```
