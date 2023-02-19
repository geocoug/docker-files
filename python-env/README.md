# python-env

Containerized Python environments. The [Dockerfile](./Dockerfile) uses a multi-staged build in an effort to keep the final image small, and attempts to implement some security features.

```sh
docker run -it --rm -v $(pwd):/usr/local/app $(docker build -q --no-cache -t python-env .)
```
