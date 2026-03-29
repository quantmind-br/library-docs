---
title: 'IndustrialKnowledgeAgent: The Smart Industrial Equipment Knowledge Agent - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/mistral-agents-non_framework-industrial_knowledge_agent-industrialknowledgeagent
source: crawler
fetched_at: 2026-01-29T07:33:43.818110552-03:00
rendered_js: false
word_count: 1111
summary: A guide on building an intelligent agent for managing and querying industrial equipment knowledge using Mistral AI.
tags:
    - Mistral AI
    - Industrial AI
    - Knowledge Agent
    - RAG
    - AI Cookbook
category: guide
---

## Problem Statement

In industrial settings, engineers and technicians often struggle to manage and retrieve comprehensive information about various equipment. This information is scattered across technical manuals, maintenance logs, safety protocols, troubleshooting guides, and parts inventories. The fragmented nature of this data makes it difficult to access and utilize effectively, leading to inefficiencies and potential safety risks. This problem requires an intelligent, adaptive solution to provide real-time, context-aware responses to queries.

## Proposed Solution

To address these challenges, we propose an agentic workflow that integrates a Retrieval-Augmented Generation (RAG) system with a database querying system (FunctionCalling). This solution leverages LLMs (including structured output mechanism), embedding models and structured data retrieval to provide contextually relevant and precise information. The workflow is orchestrated by multiple agents, each with a specific role:

1. **RAGAgent**: Utilizes LLMs and Embedding models to retrieve and generate contextually relevant information from technical documents.
2. **DatabaseQueryAgent**: Handles precise and structured data retrieval from databases containing maintenance logs, technical specifications, parts inventories, and compliance records.
3. **WorkflowOrchestrator**: Orchestrates interactions between the RAGSearchAgent and DatabaseAgent, ensuring seamless and efficient query resolution.

## Dataset Details

### PDF Documents

The PDF documents contain detailed information about various industrial equipment, categorized into:

1. **Technical Manuals**: Operation and maintenance guides.
2. **Maintenance Guides**: Routine and preventive maintenance tasks.
3. **Troubleshooting Guides**: Solutions to common issues.
4. **Safety Protocols**: Safety procedures and guidelines.

### Databases

The databases contain structured information that complements the PDF documents:

1. **Compliance Database (`compliance_db`)**: Safety certifications and compliance statuses.
2. **Maintenance Database (`maintenance_db`)**: Logs of maintenance activities.
3. **Technical Specifications Database (`technical_specifications_db`)**: Detailed technical specifications.
4. **Parts Inventory and Compatibility Database (`parts_inventory_compatibility_db`)**: Information on parts, compatibility, and inventory status.

By integrating these datasets, the proposed agentic workflow aims to provide a comprehensive and efficient system for managing and retrieving industrial equipment information, ensuring that engineers and technicians have access to the most relevant and up-to-date information.

*NOTE*: Please note that all data used in this demonstration has been synthetically generated.

### Technical Architecture:

### Installation

Installs the necessary Python packages for the IndusAgent system.

### Imports

Imports required libraries for LLM operations, data processing, vector database management, and utility functions.

### Download Data

Downloads the dataset from Google Drive, extracts it to a data directory, and sets up the working environment. The dataset contains CSV files for database operations and PDFs for document processing.

By the end of the process, you should be able to see the downloaded data, as shown in the image below.

#### Download data from Google Drive

#### Extract and setup data directory

### Set up environment variables

Sets up the Mistral API key as an environment variable for authentication.

### Initialize Mistral LLM and Qdrant Vector Database

Initializes the Mistral LLM client for text generation and Qdrant vector database client for similarity search operations.

*Note*:

1. We will use our latest model, `Mistral Small 3` for demonstration.
2. You need to set up Qdrant Cloud or a Docker setup before proceeding. You can refer to the [documentation](https://qdrant.tech/cloud/) for the setup instructions.

### System Prompts

The system uses three different types of prompts to guide the LLMs for response generation:

1. *PDF Summarization Prompt*: `summarization_prompt` is used to create concise summaries of PDF documents.
2. *Response Generation Prompt*: `response_generation_prompt` is used to generate responses based on retrieved context.
3. *Final Response Integration Prompt*: `final_response_generation_prompt` is used to summarize responses from multiple sources - PDFs and different databases.

## DataProcessor

The `DataProcessor` class is a comprehensive component that handles all data processing operations in the system. It manages both unstructured (PDFs) and structured (CSV) data, along with embedding generation and storage.

- PDF document processing and text extraction using Mistral OCR.
- CSV to database ingestion
- Embedding generation and vector storage
- Batch processing of documents and data

### Main Components

#### 1. Document Processing

- `get_categorized_filepaths`: Walks through the directory structure to get categorized PDF file paths
- `parse_pdf`: Extracts text from all pages of a PDF file using Mistral OCR.
- `process_single_pdf`: Processes individual PDFs through the complete pipeline
- `process_documents`: Handles sequential processing of multiple documents

#### 2. Summarization and Embeddings

- `summarize`: Generates concise summaries of text using the Mistral model
- `get_text_embedding`: Creates text embeddings using Mistral's embedding model
- `qdrant_insert_embeddings`: Stores embeddings with metadata in Qdrant vector database
- `process_and_store_embeddings`: Handles batch processing of embeddings

#### 3. Database Operations

- `insert_csv_to_table`: Loads a single CSV file into a specified database table
- `insert_data_database`: Handles multiple CSV files insertion into their respective tables

## RAGAgent

The `RAGAgent` class implements Retrieval-Augmented Generation (RAG) to provide intelligent search and response generation. It combines vector search capabilities with the LLM to give contextually relevant answers.

- Query categorization and classification
- Vector similarity search in Qdrant
- Context-aware response generation
- Document citation handling

### Main Components

#### 1. Query Processing

- `query_categorization`: Classifies queries into predefined categories (technical manual, safety protocol, etc.)
- `query`: Orchestrates the complete RAG pipeline from query to final response

#### 2. Search and Retrieval

- `qdrant_search`: Performs semantic search using query embeddings, filters results by document category and returns top-k most relevant documents.

#### 3. Response Generation

- `generate_response`: Creates natural language responses using retrieved context, uses LLM with specialized prompts, Provides citations to source documents.

#### Query Category Model

A Pydantic model that defines the structure for query categorization, used by RAGAgent to classify queries into relevant categories (technical\_manual, safety\_protocol, etc.).

### Database Query Tools

Defines database query function tools. These tools define the function calling interface for the DatabaseQueryAgent, enabling structured querying of different database tables.

## DatabaseQueryAgent

The `DatabaseQueryAgent` class manages interactions with the SQLite database, handling structured data queries through function calling on various databases containing maintenance logs, technical specifications, parts inventories, and compliance records. It provides specialized querying capabilities for different database tables.

- Natural language query processing
- Structured database querying
- Function calling for query execution
- JSON response formatting

### Main Components

#### 1. Table-Specific Queries

- `query_compliance`: Retrieves filtered compliance records
- `query_maintenance`: Accesses maintenance-related information
- `query_technical_specs`: Fetches technical specifications
- `query_parts_inventory_compatibility`: Retrieves parts and compatibility data

#### 2. Query Processing

- `query`: Processes natural language queries using function calling, Handles tool calls for appropriate database operations, Tracks database tool citations, Formats responses with query results.

## WorkflowOrchestrator

The `WorkflowOrchestrator` class orchestrates the interaction between RAGAgent and DatabaseQueryAgent to provide comprehensive responses by combining information from both structured and unstructured data sources.

- Workflow orchestration and coordination
- Response combination and integration
- Final response summarization
- Source citation management

### Main Components

#### 1. Workflow Execution

- `workflow`: Manages the complete query processing pipeline, Coordinates responses from both agents, Generates final unified response, Maintains traceability through citations.

#### 2. Response summarization

- `combine_and_summarize_responses`: Merges and summarizes responses from both agents, Applies structured formatting to combined responses, Uses summarization prompts for coherent output.

### Initialize and Process Documents

Initializes the DataProcessor and processes PDF documents through the complete pipeline - from file ingestion to embedding storage.

### Insert Data into Database tables.

Loads multiple CSV files into their corresponding database tables in SQLite.

### Initialise the Agents

Initializes the three core agents:

- RAGAgent for document search and response
- DatabaseQueryAgent for structured data querying.
- WorkflowAgent for orchestrating responses.

### Example Queries