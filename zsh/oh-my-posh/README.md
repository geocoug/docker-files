# zsh

Custom Zsh environment with Oh My ZSH and Oh My Posh.

The base image [zshusers/zsh](https://hub.docker.com/r/zshusers/zsh/) is build on top of [minideb](https://hub.docker.com/r/bitnami/minideb).

## Usage

```bash
docker build -t zsh . \
&& docker run -it --rm zsh
```
