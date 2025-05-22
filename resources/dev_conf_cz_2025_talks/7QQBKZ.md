# Reproducible Builds in Fedora

**Speakers:** Jelle van der Waa, Davide Cavalca, Zbigniew Jędrzejewski-Szmek
                    
**Track:** Linux Distributions, Operating Systems, and Edge
                    
**Room:** 32
                    
**Date & Time:** 2025-06-13 10:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Over the last year, Fedora has made done a lot of work to make package builds reproducible. We introduced a build post-processing tool to resolve common sources of build irreproducibilities. We also reported bugs or fixed individual issues in hundreds of packages. Together, those steps have increased the fraction of reproducible builds to about 90%.

We're ready to move to a next phase, where public rebuilders continuously rebuilds Fedora packages and report irreproducibilities, and any irreproducibilities are reported as bugs to be fixed.

This talk will give an overview of changes to build tools, build configuration, and packages required to make builds deterministic, as well as the setting up of the public rebuilders. We'll show how Fedora compares to other distributions working on reproducible builds.
