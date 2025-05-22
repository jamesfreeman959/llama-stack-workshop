# From PIDs to Pods: the life cycle of an eBPF-autoinstrumented Kubernetes application

**Speakers:** Marc Tuduri
                    
**Track:** DevOps and Automation
                    
**Room:** 31
                    
**Date & Time:** 2025-06-14 10:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
eBPF allows to safely attach small programs in the Linux Kernel and inspect the runtime memory of the Kernel and userspace programs at runtime. This opens a wide range of possibilities for observability applications. However, the low-level approach of eBPF often makes it difficult to match the inspected data with high-level concepts, such as the entities in your Kubernetes cluster.
This talk describes our journey to make Kubernetes a first-class citizen in Grafana Beyla, our eBPF-based instrumentation tool. From a hacker perspective, we will describe how we did to match the low-level abstractions from eBPF with the high-level Kubernetes information, in order to provide a unified experience by fuzzing the barriers between application, platform and infrastructure. We designed Beyla to be ubiquitous, so it can run as a simple operating-system-level process that internally understands about processes. But we wanted our Kubernetes users to keep talking about Pods, Deployments, and Services, so they don’t have to change their mindset nor have to dig into the lower-level constructions of the operating system to keep using Beyla.
