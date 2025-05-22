# How to Prevent AI Agents from Accessing Unauthorized Data

**Speakers:** Sohan Maheshwar
                    
**Track:** Artificial Intelligence and Data Science
                    
**Room:** 30
                    
**Date & Time:** 2025-06-12 15:30:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
It’s time for Day 2 Ops in the world of AI.

Building enterprise-ready AI poses challenges around data security,scalability, and integration, especially in compliance-regulated industries. Firms are increasing efforts to mitigate risks associated with LLMs regarding sensitive data exfiltration of personally identifiable information and sensitive company data. The primary mitigation strategy is to build guardrails around Retrieval-Augmented Generation (RAG) to safeguard data while also optimizing query response quality and efficiency. 

To enable precise guardrails, one must implement permissions systems with advanced fine grained authorization capabilities such as returning lists of authorized subjects and accessible resources. Such systems ensure that LLMs can access only authorized data while preventing exfiltration of sensitive information, making RAGs more efficient and improving performance at scale. 

This session will cover how modern permissions systems can safeguard sensitive data in RAG pipelines. We'll start with why Authorization is critical for RAG pipelines to protect sensitive data from potential vulnerabilities and also the various techniques for permissions-aware data retrieval. The talk will also include a practical demo implementing fine-grained authorization for RAG using Pinecone, Langchain, OpenAI, and SpiceDB - an Open Source authorization database.
