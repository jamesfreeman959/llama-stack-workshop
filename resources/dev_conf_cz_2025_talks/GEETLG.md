# Auto-instrumentation for GPU performance using eBPF

**Speakers:** Marc Tuduri, Dominik Süß
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 29
                    
**Date & Time:** 2025-06-14 14:45:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Modern AI workloads rely on large GPU fleets whose efficient utilisation is crucial due to high costs. However, gathering telemetry from these workloads to optimise performance is challenging because it requires manual instrumentation and adds performance overheads. Further, it does not produce telemetry in a standardised format for commonly used visualisation tools like Prometheus.

This talk explores the potential of leveraging eBPF to capture CUDA calls made to GPUs, including kernel launches and memory allocations. Data from these probes can be used to export Prometheus metrics, facilitating detailed analysis of kernel launch patterns and associated memory usage. This approach offers significant benefits as eBPF imposes minimal overhead and requires no intrusive instrumentation. Our implementation is also open-source and available on GitHub.
