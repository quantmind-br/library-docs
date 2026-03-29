---
title: Planning Complex Tasks | goose
url: https://block.github.io/goose/docs/tutorials/plan-feature-devcontainer-setup
source: github_pages
fetched_at: 2026-01-22T22:16:19.916153597-03:00
rendered_js: true
word_count: 1300
summary: This tutorial demonstrates how to use the goose Plan feature to decompose complex technical tasks into systematic, step-by-step execution roadmaps. It guides users through brainstorming, planning, and implementing a GitHub Codespaces development environment with Docker and automated API testing.
tags:
    - goose-ai
    - project-planning
    - github-codespaces
    - docker-setup
    - devcontainers
    - task-management
category: tutorial
---

*Transform overwhelming tasks into systematic, step-by-step execution plans*

Using goose for large, complex tasks can feel overwhelming, especially when you're unsure of exactly how you want to approach it in advance. I experienced this when I needed to set up a complex development environment for an [API course](https://github.com/LinkedInLearning/java-automated-api-testing-with-rest-assured-5989068) I published. Between Docker configurations, database initialization, devcontainer setup, and GitHub Codespaces integration, there are dozens of moving pieces that need to work together perfectly. One missing configuration or incorrect dependency can derail the entire process.

This tutorial shows you how to use goose's [Plan feature](https://block.github.io/goose/docs/guides/creating-plans) to transform a complex devcontainer setup into a systematic, executable roadmap. You'll learn how to brainstorm with goose, refine your requirements, and let goose create both a detailed plan and implementation checklist.

## What You'll Learn[​](#what-youll-learn "Direct link to What You'll Learn")

By the end of this tutorial, you'll understand how to:

- Use goose's Plan feature to break down complex technical projects
- Brainstorm and refine requirements through AI-assisted conversation
- Transform high-level goals into detailed, executable steps
- Create comprehensive checklists for validation and quality assurance
- Execute plans systematically with clear deliverables

## The Challenge: Complete Codespaces Environment[​](#the-challenge-complete-codespaces-environment "Direct link to The Challenge: Complete Codespaces Environment")

Our goal is to create a GitHub repository that provides a complete development environment for API testing with Rest Assured. When students open the repository in GitHub Codespaces, they should have:

- **Automated Setup**: Zero manual configuration required
- **API Server**: REST API running automatically
- **Database**: MySQL with pre-loaded schema and test data
- **Development Tools**: Java 17, Docker, and necessary VS Code extensions
- **One-Click Experience**: Everything starts with `docker-compose up -d`

This involves coordinating multiple technologies: Docker, MySQL, PHP, Java, devcontainers, and GitHub Codespaces.

## Step 1: Initial Brainstorming Session[​](#step-1-initial-brainstorming-session "Direct link to Step 1: Initial Brainstorming Session")

Let's start by having a brainstorming conversation with goose to clarify our requirements.

Planning in Desktop vs CLI

The goose Desktop doesn't have a `/plan` keyword like the CLI. In Desktop, you need to explicitly ask goose to create a plan:

```
"Hey goose, can you create a plan to set up my GitHub repo for Codespaces with automatic Docker startup? Please don't start the actual work yet."
```

In the CLI, you can enter plan mode with `/plan` and goose will ask clarifying questions before generating the plan. Unless you specifically ask goose Desktop to "create a plan", it might jump straight into implementation.

### Starting the Conversation[​](#starting-the-conversation "Direct link to Starting the Conversation")

**You:** *"I need help setting up a GitHub repository for automated API testing. Students should be able to open it in GitHub Codespaces and immediately start writing tests without any manual setup. Can you help me think through what's needed?"*

**goose:** *"I'd be happy to help you design this automated setup! Let me ask some clarifying questions to understand your requirements better:*

1. What type of API are you working with? (REST, GraphQL, etc.)
2. What testing framework do you want students to use?
3. Do you need a real database with test data, or can you use mocked responses?
4. What programming language should students use for their tests?
5. Are there specific API endpoints or functionality they'll be testing?"

### Refining Requirements[​](#refining-requirements "Direct link to Refining Requirements")

**You:** *"It's a REST API built in PHP that students will test using Rest Assured in Java. They need a real MySQL database with actual test data so they can practice realistic scenarios. The API has endpoints for managing products and categories in an e-commerce system."*

**goose:** *"Perfect! That gives me a clear picture. A few more questions to ensure we design this correctly:*

1. Do you already have the PHP API code, or do we need to create it?
2. What version of Java should the environment support?
3. Should the MySQL database be populated with sample products and categories?
4. Do you want any specific VS Code extensions pre-installed?
5. What's your timeline for getting this working?"

**You:** *"I have the existing PHP API code that currently runs in MAMP. I need Java 17 for Rest Assured compatibility. Yes, the database should have sample data. Please include Java and Docker extensions for VS Code."*

## Step 2: Creating the Detailed Plan[​](#step-2-creating-the-detailed-plan "Direct link to Step 2: Creating the Detailed Plan")

Now that we've clarified the requirements, let's ask goose to create a comprehensive plan.

### Requesting the Plan[​](#requesting-the-plan "Direct link to Requesting the Plan")

**You:** *"Based on our discussion, can you create a detailed plan for setting up this GitHub repository? I want a step-by-step approach that covers all the technical requirements we discussed. Please include specific deliverables and a way to validate each step."*

### The Generated Plan[​](#the-generated-plan "Direct link to The Generated Plan")

goose will generate a comprehensive plan similar to this:

GitHub Codespaces API Testing Environment Setup Plan

## Step 3: Detailed Implementation Planning[​](#step-3-detailed-implementation-planning "Direct link to Step 3: Detailed Implementation Planning")

Now let's ask goose to create the specific implementation prompt that will guide the execution.

### Creating the Implementation Prompt[​](#creating-the-implementation-prompt "Direct link to Creating the Implementation Prompt")

**You:** *"This plan looks comprehensive! Can you now create a detailed implementation prompt that I can use to execute this plan? I want something specific enough that goose can follow it step-by-step without needing additional clarification."*

### The Implementation Prompt[​](#the-implementation-prompt "Direct link to The Implementation Prompt")

goose will generate a detailed prompt like this:

Detailed Prompt

## Step 4: Executing the Plan[​](#step-4-executing-the-plan "Direct link to Step 4: Executing the Plan")

With our detailed plan and implementation prompt ready, we can now execute the setup systematically.

### Starting Implementation[​](#starting-implementation "Direct link to Starting Implementation")

**You:** *"Perfect! Now let's implement this plan. Here's the detailed prompt we created: \[paste the implementation prompt]"*

goose will now work through each step of the plan, creating the necessary files and configurations.

### Monitoring Progress[​](#monitoring-progress "Direct link to Monitoring Progress")

As goose implements the plan, you can verify each deliverable against the checklist we created:

1. **File Creation**: Check that each required file is created in the correct location
2. **Configuration Accuracy**: Verify that configurations match the specifications
3. **Integration Points**: Ensure services are properly connected and configured
4. **Testing Readiness**: Confirm that the environment will work as intended

### Validation and Testing[​](#validation-and-testing "Direct link to Validation and Testing")

Once implementation is complete, follow the validation steps from the plan:

```
# Test Docker setup locally
docker-compose up -d
docker ps

# Verify API accessibility
curl http://localhost:8888/api/products

# Test database connection
docker exec -it mysql mysql -u user -p api_db
```

## Step 5: Iterative Refinement[​](#step-5-iterative-refinement "Direct link to Step 5: Iterative Refinement")

If issues arise during implementation or testing, use the plan as a reference to identify and resolve problems systematically.

### Common Refinements[​](#common-refinements "Direct link to Common Refinements")

- **Port Conflicts**: Adjust port mappings if conflicts occur
- **Timing Issues**: Add health checks or startup delays
- **Permission Problems**: Update Dockerfile with proper permissions
- **Configuration Errors**: Verify environment variables and connection strings

## Best Practices for Planning with goose[​](#best-practices-for-planning-with-goose "Direct link to Best Practices for Planning with goose")

1. Start with brainstorming. Don't jump straight to asking for a plan. Have a conversation to clarify requirements and explore options.
2. Be specific about deliverables. Ask for concrete deliverables, file names, and validation criteria for each step.
3. Ask goose to identify potential issues and provide mitigation strategies.
4. Generate detailed implementation prompts that can guide execution without additional clarification.
5. Include specific ways to verify that each step worked correctly.

## Advanced Planning Techniques[​](#advanced-planning-techniques "Direct link to Advanced Planning Techniques")

### Multi-Phase Planning[​](#multi-phase-planning "Direct link to Multi-Phase Planning")

For very complex projects, break the plan into phases and tackle them incrementally:

**You:** *"This plan is quite comprehensive. Can you break it into smaller phases that I can implement and test independently?"*

### Dependency Mapping[​](#dependency-mapping "Direct link to Dependency Mapping")

Ask goose to identify dependencies between tasks:

**You:** *"Which of these tasks can be done in parallel, and which have dependencies on other tasks?"*

### Alternative Approaches[​](#alternative-approaches "Direct link to Alternative Approaches")

Explore different implementation strategies:

**You:** *"Are there alternative approaches to this setup that might be simpler or more robust?"*

## Conclusion[​](#conclusion "Direct link to Conclusion")

goose's Plan feature transforms complex technical challenges from overwhelming problems into systematic, executable roadmaps. By following this tutorial's approach:

1. **Brainstorm** to clarify requirements and explore options
2. **Plan** to break down complexity into manageable steps
3. **Detail** to create specific implementation guidance
4. **Execute** systematically with clear validation criteria
5. **Refine** iteratively based on results and feedback

You can tackle any complex development environment setup with confidence, knowing that you have a clear path forward and specific criteria for success.

The key is treating goose as a planning partner, not just a code generator. Give it the full context of what you're trying to achieve, and let it help you think through the complexity before diving into implementation.

## Next Steps[​](#next-steps "Direct link to Next Steps")

- Try this approach with your own complex setup challenges
- Experiment with different types of planning prompts
- Share your planning successes with the [goose community](https://discord.gg/goose-oss)
- Explore how planning integrates with [Lead/Worker mode](https://block.github.io/goose/docs/tutorials/lead-worker) or [Subagents](https://block.github.io/goose/docs/guides/subagents) for even more sophisticated workflows

Remember, the goal is to get the right approach, in the right order, with the right safeguards. That's what makes the difference between a quick fix and a robust, maintainable solution.