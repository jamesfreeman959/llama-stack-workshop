# Bringing Incremental Backups to Kubernetes with CSI Snapshot Metadata Service

**Speakers:** Praveen M, Rakshith R
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 27
                    
**Date & Time:** 2025-06-14 14:45:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
As Kubernetes adoption grows, efficient backup and recovery mechanisms become critical. Traditional backup methods often backup the entire volume regardless of the actual allocated or changed blocks leading to time-consuming processes that fail to scale.

Changed Block Tracking (CBT) technique helps in identifying allocated blocks of a single snapshot or block-level changes between pairs of snapshots of the same block volume and enabling differential backups that capture only the modified data. This approach is significantly efficient compared to full volume backups, reducing both time and resource demands.

To bring this capability to Kubernetes, the Container Storage Interface (CSI) introduces a new CBT API that allows CSI drivers to expose changed block tracking as a native service. With this API, backup applications can efficiently retrieve metadata on allocated blocks of a single snapshot or changed blocks between snapshots, enabling fast and reliable differential backups of CSI volumes.

By leveraging CSI CBT APIs, vendors can perform incremental backups natively within K8s, eliminating the need for storage-specific implementations.

In this session, we will dive into the architecture of the new CSI CBT API, discuss its efficiency, reliability and scalability and explore how it benefits the Kubernetes ecosystem by making the backup process more streamlined and performant.

Links:
1) https://github.com/kubernetes/enhancements/tree/master/keps/sig-storage/3314-csi-changed-block-tracking
2) https://github.com/kubernetes-csi/external-snapshot-metadata
