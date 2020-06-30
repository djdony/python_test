# Test for Django

### Build Docker image and up docker-compose settings
docker build .
docker-compose build


### Migrate Database
docker-compose run app sh -c "app/manage.py migrate"

### Create superuser
docker-compose run app sh -c "app/manage.py createsuperuser"

### Run Project
docker-compose up
