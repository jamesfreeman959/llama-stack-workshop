# System provisioning and bootc, now and the future

**Speakers:** Colin Walters
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 27
                    
**Date & Time:** 2025-06-13 13:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
At the last Devconf.cz, I demoed how one can "replace/reinstall" a cloud instance with a bootc (bootable) container image. However, this is just one option in the wider environment.

In this talk we'll first take a deeper technical dive for background into that perennial question "How do I boot a container?". But more specifically we'll look at the broader options for deploying a bootc container to a physical/virtual system (Anaconda, bootc-image-builder, bootc install to-existing-root, or a factory reset).

We'll cover interesting details like static IP addressing on bare metal, best practices for secrets (outside of the container), and also touch on the interesting topic of the larger question of system configuration frontends (kickstart vs cloud-init vs blueprints vs Ignition) that all intersect with bootc still.
