# Test for Django

### Build Docker image and up docker-compose settings
docker build .  
docker-compose build


### Migrate Database if needed
docker-compose run app sh -c "app/manage.py migrate"

### Create superuser
docker-compose run app sh -c "app/manage.py createsuperuser"

### Run Project
docker-compose up

http://127.0.0.1:8000/admin/  
username : admin  
password : tez


### Undone / TODO
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя