# Effortless, standardised homelab observability with eBPF

**Speakers:** Goutham Veeramachaneni
                    
**Track:** DevOps and Automation
                    
**Room:** 31
                    
**Date & Time:** 2025-06-12 14:45:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Running a homelab means running a diverse set of applications like NextCloud, readeck.org, usememos.com.

They are written in many languages and frameworks and in general lack a good way to monitor them. The old way to monitor them involved having a basic blackbox_exporter enabled synthetic monitoring. Even instrumented, each application has a different set of metrics, leading to complex alerting and dashboards.

Grafana Beyla, powered by eBPF and OpenTelemetry, combined with Prometheus promises to generate first class observability signals for services regardless of the language and frameworks used. This talk will walk through deploying Beyla for a homelab, and the challenges in having good observability even with Beyla.

We will walk through:

1. Deploying Beyla in your environment with Prometheus
2. Setting up dashboards for the data
3. Robust alerting over the signals, especially in low, sporadic traffic (homelab) scenarios.
4. The missing signals from eBPF and how you can fill those gaps
