# Integration testing for container images via Kind in GitLab CI

**Speakers:** Michael Hofmann
                    
**Track:** DevOps and Automation
                    
**Room:** 27
                    
**Date & Time:** 2025-06-12 12:30:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Red Hat's Continuous Kernel Integration (CKI) project is responsible for the infrastructure and workflow automation for all internal kernel development.

The workflow automation part is implemented by a diverse zoo of about 30 Python-based micro services, with updates delivered and deployed multiple times a day.

In this talk, we will describe our approach to integration testing the interactions of these services via Kind, i.e. a Kubernetes cluster running in Docker, deployed on-demand in GitLab CI.

We will also discuss the general challenges around running and testing interconnected services:
- unit tests and their limits
- testing across multiple interdependent repositories
- DevOps strategies and API design considerations

Attendees will gain an understanding of the failure modes of micro services, and how testing in GitLab CI can be structured to prevent them. The CKI project's approach to integration testing can serve as a blueprint for a testing setup that does not rely on heavy-weight staging environments and can be completely implemented in the CI services provided by the major Git forge providers.
