# python-env

Containerized Python environments.

Both the [Dockerfile.dev](./Dockerfile.dev) and [Dockerfile.prod](./Dockerfile.prod) versions will produce the same environment. The [Dockerfile.prod](./Dockerfile.prod) version uses a multi-staged build in an effort to keep the final image small, and adheres to a higher security standard.

## Development

During development, mount your current working directory to the container:

```sh
docker run -it --rm -v $(pwd):/usr/local/app $(docker build -q -t python-env -f Dockerfile.dev .)
```

## Production

Copy your files into the image. Make sure to use [.dockerignore](./.dockerignore) to keep unwanted files out of the image (like a local Python venv).

- [Line 44] [Dockerfile.prod](./Dockerfile.prod):

    ```Dockerfile
    COPY . $HOME
    ```

Build the image:

```sh
docker build --no-cache -t python-app -f Dockerfile.prod .
```

Run the image:

```sh
docker run -it --rm python-app
```

Restart the container:

```sh
docker start -i <container_id>
```
