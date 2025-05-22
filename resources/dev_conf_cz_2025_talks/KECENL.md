# Batch Job / Queue Processing Without a Message Broker

**Speakers:** Jan CIzmar
                    
**Track:** Application and Services Development
                    
**Room:** 29
                    
**Date & Time:** 2025-06-12 10:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Building background job processing often involves introducing a message broker (RabbitMQ, Kafka, etc.) into your architecture.

But what if your application could handle batch jobs on its own, without any external messaging system? Tolgee – an open-source localization platform – faced this challenge and implemented a solution that keeps the infrastructure lean.

This talk will dive into how Tolgee orchestrates batch operations (like bulk translations) using only its application server and database. We'll explore how Tolgee leverages PostgreSQL row-level locks (`SKIP LOCKED`) to manage job queues and concurrency, storing tasks in the database instead of relying on external brokers. 

In a multi-instance setup, Tolgee uses a lightweight caching and pub-sub mechanism (via Redis) to synchronize work across nodes and avoid duplicate processing.

The result is a robust job-processing system with significantly reduced infrastructure complexity. The concepts are framework-agnostic: you can apply the same principles in any language or tech stack using a database and basic scheduling tools. By cutting out external dependencies, this approach simplifies deployment and maintenance while still handling large-scale batch tasks efficiently.

In this session, you'll learn:
- How to implement a database-backed job queue using simple transactions or locks instead of a dedicated message broker
- Techniques for scheduling and executing background tasks inside your application process
- Strategies to coordinate task processing across multiple instances using minimal tools (e.g. in-memory caches or lightweight pub-sub)
- Lessons from Tolgee’s real-world experience building a broker-free batch job system, with a live demo to round it off
