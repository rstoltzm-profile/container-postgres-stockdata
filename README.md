# postgres container project

## Overview
1. Collect data
2. Create Postgres db container
3. Load data
4. Query data with external container

## Steps
1. docker-compose up --build
    * this will run data-collector, startup database, load data
3. go to 3-query-postgres
    * build and run container following notes.txt

## Improvements
* combine data-collect and data-loader into single container
* separate out postgres db from container stack
* create a container for building and managing the postgres database

## Screenshots
### docker-compose view 
* data-collector and data-loader will run once and stop
* postgres db will keep running
![image](https://github.com/user-attachments/assets/e7fe4fac-897d-4cf1-b654-2a6b85395880)
### query-postgres will look like this, run as separate container
![image](https://github.com/user-attachments/assets/c9472c35-d7bf-4593-b123-1efddac4e0fa)
