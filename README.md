# eaas-deployment-f
An api template, add new nodes to kubernetes cluster automation with ansible.

I have many of these variations, f is the next one I'm doing on github.
EaaS deployment f does not have TLS and features a single Apache webserver
with mpm-prefork web cgi program exectuion. There are a few demo
programs included, you would replace those with your actual API.

This repo is a template of sorts for deployment of a micro-service
that would likely only be used to communicate with the loopback
and there would be another service that provides TLS on top of this,
such as HAProxy or Traefik etc.

More of what this repo is about is the installation of a 3 node kubernetes cluster
with a calico network, and a template for deploying microservices
within it.

See more examples of these templates, both of these others include TLS:
https://github.com/jpegleg/eaas-deployment-e
https://github.com/jpegleg/eaas-deployment-d
