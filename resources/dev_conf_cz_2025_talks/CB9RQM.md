# Concurrency vs. Parallelism in Node.js: Understanding the Event Loop and Worker Threads

**Speakers:** Hrithik Gavankar, Rohit Bharmal
                    
**Track:** Open Track
                    
**Room:** 33
                    
**Date & Time:** 2025-06-14 13:55:00
                    
**Duration:** 15 minutes
                    
## Abstract
                    
Did you know that Node.js can handle thousands of concurrent connections on a single thread, yet struggles with CPU-intensive tasks? Understanding the difference between concurrency and parallelism is key to optimizing performance in high-scale applications.

This talk takes a deep dive into Node.js’ asynchronous model, explaining how the Event Loop, non-blocking I/O, and Worker Threads enable efficient multitasking. Using real-world examples from API handling and real-time sports data processing, we’ll explore when to rely on Node’s async model and when to offload work to Worker Threads for better performance.

Key Takeaways:
Concurrency vs. Parallelism in Node.js – How they work and when to use each approach.
Deep Dive into the Event Loop – Understanding microtasks, macrotasks, and asynchronous execution.
When to Use Worker Threads – Offloading CPU-heavy tasks to prevent blocking the main thread.
Real-World Performance Optimizations – Lessons from handling large-scale API requests and real-time data updates.
By the end of this session, attendees will have a clear understanding of Node.js’ execution model and the best practices for achieving optimal performance in high-load applications.
