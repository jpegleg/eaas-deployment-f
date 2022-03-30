![eaas-template-f](https://carefuldata.com/images/cdlogo.png)

https://github.com/jpegleg/eaas-deployment-f 🟨 status: usable [ work in progress, reference template ]

# eaas-deployment-f
An api template, add new nodes to kubernetes cluster automation with ansible for Debian-based systems (Ubuntu, Debian, Mint, Kali, etc)

I have many of these variations, f is the next one I'm doing on github.
EaaS deployment f features a single Apache webserver
with mpm-prefork web cgi program exectuion. There is a demo
encryption-as-a-service included, you would replace those with your actual API etc.


More of what this repo is about is the installation of a 3 node kubernetes cluster
with a calico network, and a template for deploying microservices
within it.

See more examples of these templates:

https://github.com/jpegleg/eaas-deployment-e  # status: 🟩 usable [ docker only template, reference template ]

https://github.com/jpegleg/eaas-deployment-d   # status: 🟩 usable [ microk8s single node, reference template ]

https://github.com/jpegleg/eaas-deployment-k  # status: 🟩 usable [ generic k8s config templates ]

And related resource templates:

https://github.com/jpegleg/eaas-deployment-h  # status: 🟩 usable [ security reference templates ]

# included shell scripts

There are some shell scripts included in this repo that do some example configurations.
I would recommend using them as references rather than actual deployment method,
but they represet "a way" of doing things, not the best possible for your situation way.

The scripts represent phases of the configuration. The first phase is to set up kubelet
and docker and make a 3 node k8s cluster with a calico network.

The second phase represents building a local registry in docker on each node containing
the "zcrab" template. This would be replaced with the docker build process, code, and
materials that make up the microservice or application that is deployed.

These phase shell scripts are a work in progress and may or may not work at any given time.

## shell script phase status

phase 1: minimum viable product

phase 2: WIP

phase 3: TBD

phase +: TBD
