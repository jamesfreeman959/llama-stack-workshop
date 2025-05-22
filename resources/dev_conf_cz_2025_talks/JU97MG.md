# Kubernetes Multitenancy in Image Pulling

**Speakers:** Standa Láznička
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 27
                    
**Date & Time:** 2025-06-12 14:45:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Imagine this: you train your AI model, spend a lot of time and resources, feed it internal data. When you are finally done with it, you containerize it and deploy it to a Kubernetes cluster. Everything's fine. Until it isn't! Another tenant you are sharing the cluster with somehow managed to get a hold of your image. How could it be? They cannot access any of your namespaces, you made sure of that.

This session will introduce you to the trouble of multi-tenancy of images you pull with Kubernetes, and you will learn about a new (alpha) feature that aims to finally solve multi-tenant access to Kubernetes node's images.
