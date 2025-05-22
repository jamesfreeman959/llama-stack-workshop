# Running Multi-Arch Builds & Tests in OpenShift CI/CD

**Speakers:** Nick Moraitis
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 33
                    
**Date & Time:** 2025-06-12 13:55:00
                    
**Duration:** 15 minutes
                    
## Abstract
                    
Our team is responsible for the entire CI/CD infrastructure powering OpenShift development, a large-scale system running across multiple OpenShift clusters. 
Thousands of jobs and builds are executed daily, supporting both internal OpenShift teams and external organizations relying on our infrastructure.

One of the biggest challenges we tackled was enabling multi-architecture builds and test execution at this scale, something not natively supported by OpenShift builds.

In this talk, I'll dive into the solutions we implemented to make it work.
From handling multi-arch base images to ensuring consistent test execution across architectures, I’ll share the technical solutions we developed and the lessons we learned.
