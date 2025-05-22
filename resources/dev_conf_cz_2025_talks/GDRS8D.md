# Boxcutter - or what we learnt about managing objects with Server-Side-Apply in Kubernetes

**Speakers:** Josh, Nico Schieder
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 27
                    
**Date & Time:** 2025-06-14 10:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Writing controllers that manage other objects is hard. Especially if you want to do:
- server-side-apply (all the cool kids are talking about it)
- proper status reporting through generic object probes
- phased ordering of managed objects (Namespaces need to exist before resources can be put into them; CustomResourceDefinitions (CRDs) must be registered before being used; ...)
- Drift detection (did someone else change an object under my control?)
- permission management with separate caches (You don't want a probe reading the data of something you're not allowed to read...)

We'd like to present to you, what we learnt about managing objects using server-side-apply while extracting some functionality of our service-delivery operator "package-operator" into the separate library "boxcutter".
