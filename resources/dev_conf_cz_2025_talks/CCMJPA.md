# Extending clusters to the edge and far edge with bootable containers

**Speakers:** Clodagh Walsh
                    
**Track:** Linux Distributions, Operating Systems, and Edge
                    
**Room:** 32
                    
**Date & Time:** 2025-06-14 10:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Due to resource constraints it may not be feasible to run a kubelet and its dependencies on an edge device to act as a fully fledged kubernetes node. This session explores how the bootc and virtual kubelet projects can be combined to create a lightweight solution extending clusters to the edge and far edge.

Bootable containers, enabled by the bootc project, follow OCI principles to create bootable images suitable for a range of systems and architectures. Bootable containers simplify device management through rollbacks and automatic updates.

By implementing a virtual kubelet provider for bootc managed devices, workloads can run natively on edge devices leveraging any specialised hardware without the overhead of a kubelet and container engine.

This session is of interest to cluster administrators particularly those who are seeking innovative solutions to manage edge devices. This session also presents an application of bootable containers and the bootc project showcasing it alongside familiar cloud native tools. This work is part of the P2CODE project funded by the Horizon Europe Research programme.
