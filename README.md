# fastapi-async-tdd
Developing and Testing an Asynchronous API with FastAPI and Pytest

## Resources

- testdriven.io [article](https://testdriven.io/blog/fastapi-crud/)

## Basics

1. Build the docker image

        docker-compose up -d --build

2.  Visit http://127.0.0.1:8002/ping and http://127.0.0.1:8002/docs for autogenerated docs from swagger

3. Run the test stub from docker


        docker-compose exec web pytest .

4. Ensure the `notes` table was added

    - Get a psql prompt from the postgres container

          docker-compose exec db psql --username=hello_fastapi --dbname=hello_fastapi_dev

    - List databases

          hello_fastapi_dev=# \l

5. Try out the `POST` route with [HTTPie](https://httpie.org/doc#installation)


        http --json POST http://localhost:8002/notes/ title=Foo description=bar
