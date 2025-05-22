# Zap the Flakes! Leveraging AI to Combat Flaky Tests with CANNIER

**Speakers:** Daniel Hiller
                    
**Track:** Artificial Intelligence and Data Science
                    
**Room:** 30
                    
**Date & Time:** 2025-06-14 12:30:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Flakes aka tests that don’t behave deterministically, i.e. they fail sometimes and pass sometimes, are an ever recurring problem in software development. This is especially the sad reality when running end-to-end tests where a lot of components are involved. There are various reasons why a test can be flaky, however the impact can be as fatal as CI being loaded beyond capacity causing overly long feedback cycles or even users losing trust in CI itself.

Ideally CI maintainers want potential flakes to be flagged at the earliest stage of the development lifecycle, so that they do not even enter the end-to-end test suite. They want a gate that acts as a safeguard for developers, pointing out to them what kind of stability issues a test has. This reduces CI user frustration and improves trust in CI. At the same time it cuts down on unnecessary waste of CI system resources.

This talk will explore the [CANNIER](https://www.gregorykapfhammer.com/research/papers/parry2023/) approach, which aims to reduce the time cost of rerunning tests. The speaker and the audience will take a closer look at the feature set used to create training data from existing test code of the [KubeVirt](https://kubevirt.io/) project, enabling CI systems to predict probable flakiness of a certain test with an AI model.  

The speaker will cover how a subset of the CANNIER feature set is implemented, how it is used to generate training data for an AI model, and how the model is used to analyze flakiness probability, generating actionable feedback for test authors.

Attendees will gain insight on how the CANNIER approach can help them improve test reliability, ultimately enhancing overall software quality and team productivity.
