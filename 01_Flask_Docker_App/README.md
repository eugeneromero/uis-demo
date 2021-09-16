# UiS DevOps Lecture Flask demo application

## Building

Build this image with
```
docker build -t uis-demo:1.0.0 .
```
If local network is running IPv6, it might be necessary to build using the `host` network, instead of the default `docker` one:
```
docker build --network host -t uis-demo:1.0.0 .
```

## Running
This application can be run with

```
docker run --rm -it uis-demo:1.0.0
```
