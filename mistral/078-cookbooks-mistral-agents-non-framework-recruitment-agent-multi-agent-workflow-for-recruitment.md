---
title: Multi Agent Workflow For Recruitment - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-agents-non_framework-recruitment_agent-multi_agent_workflow_for_recruitment
source: crawler
fetched_at: 2026-01-29T07:33:45.24356941-03:00
rendered_js: false
word_count: 1145
summary: This document outlines an automated multi-agent recruitment system that leverages Mistral's LLM and OCR capabilities to streamline candidate screening, matching, and communication.
tags:
    - multi-agent-systems
    - mistral-ai
    - recruitment-automation
    - llm-agents
    - ocr-processing
    - workflow-orchestration
category: guide
---

## Introduction

The Multi Agent Workflow For Recruitment is an automated system designed to help streamline the hiring process through specialized AI agents working in harmony to improve candidate evaluation, save time and resources, and improve overall hiring outcomes.

## The Problem

Today's recruitment landscape faces three critical challenges:

1. **Overwhelming Volume**: Recruiters struggle to efficiently process large numbers of applications, often missing qualified candidates.
2. **Manual Inefficiency**: Traditional resume screening is time-consuming, inconsistent, and vulnerable to bias.
3. **Poor Candidate Experience**: Slow response times and fragmented communication damage employer brand and lose top talent.

## Why This Matters

Ineffective recruitment directly impacts business outcomes through:

- **Reduced Performance**: Missing qualified candidates leads to suboptimal hires and team performance
- **Business Delays**: Extended hiring cycles postpone critical projects and initiatives
- **Higher Costs**: Inefficient processes and prolonged vacancies increase recruitment costs

## Our Solution

The Multi Agent Workflow For Recruitment addresses these challenges through a coordinated system of specialized AI agents:

1. **DocumentAgent**: Intelligently extracts and processes text from resumes and job descriptions using advanced Mistral's OCR
2. **JobAnalysisAgent**: Analyzes job descriptions to identify required skills, experience, and qualifications
3. **ResumeAnalysisAgent**: Parses resumes to create structured candidate profiles with key capabilities
4. **MatchingAgent**: Evaluates candidates against job requirements with nuanced understanding beyond keyword matching
5. **EmailCommunicationAgent**: Generates personalized email communications and schedules interviews with qualified candidates
6. **CoordinatorAgent**: Orchestrates the entire workflow between agents for seamless operation.

The solution uses Mistral LLM for language understanding, structured output mechanisms for consistent data extraction, and Mistral OCR for document parsing.

### Example: Data Scientist Hiring

To illustrate how the Multi Agent Workflow For Recruitment operates in practice, consider a realistic example:

HireFive needs to hire a Senior Data Scientist with machine learning expertise. The job description specifies requirements including 3+ years of experience, proficiency in Python and deep learning frameworks, and a Master's degree in a quantitative field. From a pool of candidate resumes, the workflow automatically:

- Extracts structured requirements from the job description, identifying critical skills
- Parses all the resumes, creating standardized profiles with skills, experience, and education
- Evaluates each candidate, assigning scores like "Technical Skills: 32/40" and "Experience: 25/30"
- Identifies candidates scoring above the 70-point threshold
- Automatically sends personalized interview invitations with scheduling links to these candidates

The entire process completes in minutes, providing HireFive's hiring manager with a ranked list of qualified candidates while eliminating hours of manual resume screening.

### Solution Architecture

![Solution Architecture](https://docs.mistral.ai/cookbooks/mistral/agents/non_framework/recruitment_agent/solution_architecture.png)

### Installation

### Imports

### Setup API Keys

### Initialize Mistral API Client

### Download Data

Here, we download the necessary data for the demonstration.

1. Job Descrition.
2. Candidate Resumes.

##### Helper functions to download Job description and candidate resumes

#### Download Job Description

#### Download Candidate Resumes

### Define Pydantic Models

Pydantic models provide structured data validation between agents, ensuring consistent formats for candidate profiles, job requirements, and evaluation scores while enabling seamless integration with Mistral LLM's parsing capabilities. Following are the different pydantic models we use for

- **Skill**: Represents a candidate's technical or soft skill with its proficiency level and years of experience.
- **Education**: Captures educational qualifications including degree, field of study, institution, and performance metrics.
- **Experience**: Tracks professional experience with role details, duration, utilized skills, and key accomplishments.
- **ContactDetails**: Stores candidate contact information including name, email, and optional communication channels.
- **JobRequirements**: Defines position requirements including mandatory and preferred skills, experience level, and educational qualifications.
- **CandidateProfile**: Consolidates a candidate's complete professional profile including contact details, skills, education, and work history.
- **SkillMatch**: Evaluates individual skill alignment between job requirements and candidate capabilities with confidence scores.
- **CandidateScore**: Provides comprehensive scoring across key evaluation areas with total score calculation and identified strengths/gaps.
- **CandidateResult**: Connects file information with extracted candidate data and evaluation scores for final ranking and selection.

### Base Agent Class

The `Agent` class serves as the foundation for all specialized agents, providing a standardized interface for processing and communicating between agents in the recruitment workflow.

Each agent implements the common `process()` method while inheriting identity management and communication capabilities.

### DocumentAgent: Handles document extraction and OCR

The `DocumentAgent` handles document processing by extracting structured text from various files using Mistral's OCR capabilities. It transforms complex resume PDFs and job descriptions into text, serving as the initial data gateway for the entire recruitment workflow.

### JobAnalysisAgent: Handles job requirement extraction and analysis

The JobAnalysisAgent extracts structured job requirements from plain text job descriptions using Mistral LLM. It transforms unstructured job postings into organized data models capturing required skills, experience levels, and educational qualifications needed for candidate matching.

### ResumeAnalysisAgent: Handles resume parsing and profile extraction

The ResumeAnalysisAgent transforms raw resume text into structured candidate profiles using Mistral LLM's parsing capabilities. It extracts and organizes key information including contact details, skills, education history, and professional experience into standardized data structures for consistent evaluation.

### MatchingAgent: Evaluates candidate fit against job requirements

The `MatchingAgent` evaluates candidate profiles against job requirements to generate comprehensive scoring across technical skills, experience, education and additional qualifications. It employs Mistral LLM to assess the quality and relevance of candidate attributes beyond simple keyword matching, producing a detailed evaluation with confidence metrics and identified strengths and gaps.

## EmailCommunicationAgent: Handles email generation and sending

The `EmailCommunicationAgent` generates personalized email communications to candidates and sends them through SMTP integration. It crafts contextually relevant messages based on candidate qualifications and scheduling information, managing the critical final step of candidate engagement in the recruitment workflow.

## CoordinatorAgent: Manages the workflow and coordinates between agents

The `CoordinatorAgent` orchestrates the entire recruitment workflow by managing communication and data flow between all specialized agents. It initializes the process with job descriptions, distributes resumes, collects evaluation results, applies threshold-based filtering, and triggers candidate communications, serving as the central intelligence that ensures the seamless execution of the multi-agent recruitment system.

### Run the workflow

To run the Multi Agent Workflow For Recruitment, you simply need to:

- Configure file paths for the job description, resume directory, and output results
- Set up email credentials and Calendly scheduling link
- Initialize the CoordinatorAgent with your Mistral client
- Configure the EmailCommunicationAgent with sender credentials
- Execute the workflow with your desired threshold score

#### Define paths

#### Gmail App Password Setup

To use the email functionality in the Multi Agent Workflow For Recruitment with Gmail, you'll need to create an app password:

1. Enable 2-Step Verification on your Google Account:
   
   - Go to your Google Account → Security
   - Under "Signing in to Google," select 2-Step Verification → Get started
2. Generate an App Password:
   
   - Go to your Google Account → Security
   - Under "Signing in to Google," select App passwords
   - Select "Mail" as the app and "Other" as the device (name it "Recruitment Workflow")
   - Click "Generate"
   - Google will display a 16-character password (four groups of four characters)
3. Use this app password in your workflow configuration:

This app password bypasses 2FA and allows the workflow to send emails through your Gmail account securely without storing your actual Google password in the code.

#### Initialize coordinator agent

#### Set up communication agent with email credentials

#### Execute hiring workflow

Note: We have considered 5 candidate resumes for simplicity's sake.

You can check each of the candidates extracted results.