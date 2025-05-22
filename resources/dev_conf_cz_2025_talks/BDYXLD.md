# Writing controllers in rust

**Speakers:** Danil Grigorev
                    
**Track:** Application and Services Development
                    
**Room:** 29
                    
**Date & Time:** 2025-06-14 11:00:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Kubernetes API server provides a standardized extension layer, called CustomResourceDefinitions (CRDs). This is a go-to contract, used to implement a controller with added functionality. There are some standard libraries, like controller-runtime and kubebuilder, written in Go, built to integrate with it natively. But what about other languages, like Rust?

How would a controller look like written in Rust? Why would you want to consider writing one? What benefits or downsides this approach might have? And how can a Rust controller still benefit from an established Go ecosystem?

We will explore these topics, compare implementations and share experience over other projects using Rust within kubernetes.
