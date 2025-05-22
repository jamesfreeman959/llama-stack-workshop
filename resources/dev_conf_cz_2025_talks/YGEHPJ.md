# Declarative Networking in Declarative World, ver. 2025

**Speakers:** Mateusz Kowalski
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 27
                    
**Date & Time:** 2025-06-13 10:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Since the beginning of time, declarative APIs have been driving everything that can happen inside a Kubernetes cluster. Predefined CRDs, operators defining custom CRDs, everything is about declarative APIs. Write your YAML once, deploy it, forget it. That’s how you create a cluster, that’s how you deploy your workload.

But is it, for real, as simple as it sounds? How do you bring declarativeness to the imperative world? In the current state of things, host networking is one huge imperative nightmare. So how to happily marry an old-school Network Manager and brand new Kubernetes API?

Over the years we were working on the NMstate project to provide you with a Declarative Network API, allowing you to manage host networking in a declarative manner.

In 2025 we are coming back with brand new features. Based on the feedback, we focused on air-gapped and big clusters – think hundreds of nodes with hundreds of VLANs each. We also happily married K8s and KubeVirt – no matter what your workload is, containers or VMs, NMstate is there for you.

Not only a project update – we will also show you how the Kubernetes cluster with NMState Operator manages networking on the nodes it deploys. It may sound like a chicken and egg situation, but trust us, it is not. Last but not least, we show how it protects itself from applying destructive network changes potentially taking your cluster down.

Join us and discover what’s new in the world of complex network topologies.
