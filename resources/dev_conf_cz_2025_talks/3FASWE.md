# container-snap: Atomic Updates from OCI Images using Podman’s Btrfs Driver

**Speakers:** Dan Čermák
                    
**Track:** Linux Distributions, Operating Systems, and Edge
                    
**Room:** 33
                    
**Date & Time:** 2025-06-12 16:35:00
                    
**Duration:** 15 minutes
                    
## Abstract
                    
Traditional package updates using tools like RPM or Zypper can introduce risks, such as incomplete updates or accidentally breaking the running system. To overcome these challenges, we developed **container-snap**, a prototype plugin designed to deliver **atomic OS updates**—updates that are fully applied or rolled back without compromising the system's state.

**container-snap** leverages OCI images as the source for updates and integrates seamlessly with openSUSE’s [tukit](https://github.com/openSUSE/transactional-update) to enable transactional OS updates. By utilizing **Podman’s btrfs storage driver**, it creates btrfs subvolumes directly from OCI images, allowing systems to boot from the OCI image. This approach empowers users to construct their own OS images using familiar container image-building tools, like Docker or [Buildah](https://buildah.io/).

In this session, we’ll dive into:
- The architecture and technical implementation of container-snap
- Challenges encountered during development and how we resolved them
- Key lessons learned along the way
- A live demo showcasing container-snap in action

Come and join this session to learn more about how to boot from an OCI image without bricking your system!
