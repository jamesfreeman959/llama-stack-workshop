# Build It Your Way: Modular Pipelines for Bootable Containers

**Speakers:** Rishabh Saini
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 33
                    
**Date & Time:** 2025-06-14 13:35:00
                    
**Duration:** 15 minutes
                    
## Abstract
                    
The success of bootable containers hinges on streamlining three key steps:
1) Writing an OS from scratch using Containerfiles
2) Building images efficiently
3) Deploying them securely

With bootc, we have simplified OS creation to just writing a Containerfile, but to make this process truly production-ready, we need a customizable, secure, and automated build and deployment workflow.
On-Cluster Layering (OCL) automates in-cluster builds, but what if users could define their own workflows? 

Enter the Unified Build API, which enables tasks like Containerfile linting, custom testing, security scanning, image signing, and caching—all tailored to their needs.
Consider it like assembling LEGO blocks for OS builds—users provide the blueprint, and we handle execution. Join me in exploring how this approach modularizes, secures, and simplifies OS container builds in production.
