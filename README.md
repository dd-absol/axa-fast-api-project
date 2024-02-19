python project for axa technical assessment

install dependencies with

`pip install "fastapi[all]"`

start the server for local development or testing with

`uvicorn app.main:app --reload`

run the unit tests file with

`python app/business_logic_tests.py`

if you have docker installed, you can run the app in a container using

`docker build -t myimage .`

then

`docker run -d --name mycontainer -p 80:80 myimage`
