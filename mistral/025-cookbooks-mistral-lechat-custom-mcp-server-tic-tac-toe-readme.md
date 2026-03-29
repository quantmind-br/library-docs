---
title: 'Build a Custom MCP Server on LeChat: Tic-Tac-Toe with MistralAI - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/mistral-lechat_custom_mcp_server-tic-tac-toe-readme
source: crawler
fetched_at: 2026-01-29T07:33:44.163385891-03:00
rendered_js: false
word_count: 2470
summary: This tutorial teaches how to build a custom MCP server for a tic-tac-toe game that integrates with Mistral AI and LeChat, using a room-based session architecture.
tags:
    - mcp-server
    - mistral-ai
    - python
    - flask
    - tic-tac-toe
    - lechat
    - session-management
category: tutorial
---

## What You'll Create

By the end of this tutorial, you'll have built a **fully functional MCP server** that allows you to play tic-tac-toe directly inside our chat interface - LeChat.

## Demo Video

[Watch the video on YouTube](https://docs.mistral.ai/cookbooks/mistral-lechat_custom_mcp_server-tic-tac-toe-readme)

## What happens when you play on LeChat:

1. User types "create a new tic-tac-toe game" in LeChat
2. LeChat calls your MCP server's `create_room()` tool
3. Your server creates a new game session and returns the board
4. User makes a move: "I'll play position 4"
5. LeChat calls `make_move(4)` on your server
6. Your server processes the move, calls Mistral AI for the counter-move
7. Game state is updated and returned with trash talk from the AI
8. The cycle continues until someone wins!

## Project Structure

## Python Dependencies

Create `requirements.txt` with these dependencies:

## Get Mistral API key

You will need a Mistral API key in your environment.

Follow these steps to obtain one:

1. Go to [console.mistral.ai](https://docs.mistral.ai/cookbooks/mistral-lechat_custom_mcp_server-tic-tac-toe-readme)
2. Sign up or log in (a free tier is available)
3. Create a new API key

## End to End Workflow Steps:

We will here show you end to end Custom MCP connecor setup in 4 steps:

1. Building the Game Logic Foundation(app.py)
2. Building the MCP Server Layer(mcp\_server.py)
3. Deploying to HuggingFace spaces
4. LeChat Integration.

## Building the Game Logic Foundation

Now let's build the core tic-tac-toe game logic with AI integration. This will be the foundation that our MCP server will use.

Before diving into code, let's understand **why** we're building this way and **what** we're creating.

### The Challenge: Multiple Users, Multiple Games

When your MCP server is deployed, you'll have:

- **Multiple users** connecting simultaneously via LeChat
- **Multiple games** happening at the same time
- **Each user** might want to play several games
- **Game state** needs to persist across interactions

A simple single-game approach won't work because: ❌ Users would interfere with each other's games  
❌ No way to resume games later  
❌ Can't support multiple concurrent games  
❌ State gets lost between MCP tool calls

### The Solution: Room-Based Sessions

We create a **"Room"** for each game session: ✅ **Isolated state** - Each game has its own board and history  
✅ **Unique identifiers** - Room IDs prevent game conflicts  
✅ **Persistent sessions** - Games survive between tool calls  
✅ **Multi-room support** - Users can play multiple games  
✅ **Easy cleanup** - Old rooms can be removed when inactive

### What We're Building

#### Architecture Overview

#### Component Flow

#### What Each Room Contains

- **Game Board**: Current 3x3 state (positions 0-8)
- **Game Status**: Active, won, or draw
- **Player Tracking**: Whose turn it is
- **AI Integration**: Mistral AI as intelligent opponent
- **Chat History**: Conversation between human and AI
- **Metadata**: Creation time, activity tracking, move counts

#### The Flask API Layer

We'll also create REST endpoints so you can:

- **Test locally** without MCP complexity
- **Debug issues** with direct HTTP calls
- **Understand the flow** before adding MCP layer
- **Verify AI integration** works correctly

#### Step 1: Create the Room Class

The `Room` class is the heart of our game logic. It encapsulates everything needed for one tic-tac-toe game session.

##### What the Room Class Does:

- **State Management**: Tracks board positions, whose turn, win/draw status
- **Session Isolation**: Each room is independent - no games interfere with each other
- **AI Integration**: Coordinates with Mistral AI for intelligent gameplay
- **Chat System**: Maintains conversation history between human and AI
- **Data Persistence**: Survives between MCP tool calls
- **Rich Display**: Converts game state to beautiful markdown format

Create `app.py` and start with the basic setup and Room class structure:

#### Step 2: Add Game Logic Methods

Now we'll add the core methods that make our tic-tac-toe game work. Each method has a specific purpose:

###### Methods We're Adding:

- **`make_move(position, player)`** : Validates and executes moves, checks for wins
- **`check_winner()`** : Determines if someone has won the game
- **`add_chat_message(message, sender)`** : Manages conversation history
- **`to_markdown()`** : Creates beautiful game display for users
- **`to_dict()`** : Converts room to JSON format for API responses

###### Why These Methods?

- **Game Rules**: `make_move()` and `check_winner()` enforce tic-tac-toe rules
- **User Experience**: `to_markdown()` makes games visually appealing
- **Communication**: `add_chat_message()` enables AI personality
- **API Integration**: `to_dict()` provides structured data for MCP tools

Add these methods to the `Room` class:

#### Step 3: In memory rooms storage

We need to keep track of the state of rooms in memory, so we initialize a dictionary called `rooms` for this purpose.

#### Step 4: Mistral AI Integration

The AI opponent is what makes this game engaging! We need two functions to handle AI interactions.

###### AI Functions We're Creating:

- **`get_ai_move_for_room(room)`** : Gets AI's next move with strategic thinking and trash talk
- **`get_ai_chat_for_room(room, user_message)`** : Handles conversational responses during gameplay

###### Why AI Integration?

- **Intelligent Opponent**: AI analyzes the board and makes strategic moves
- **Personality**: AI responds with witty comments and competitive banter
- **Engagement**: Makes the game fun and interactive, not just mechanical
- **Context Awareness**: AI sees current game state and responds appropriately

###### How It Works:

1. **Game State Analysis**: AI receives current board layout
2. **Strategic Thinking**: AI evaluates possible moves and picks the best one
3. **Personality Response**: AI adds a comment about the move or situation
4. **JSON Response**: Returns structured data with move and message

Add these functions for AI opponent:

##### Step 5: Flask API Endpoints

Now we create REST API endpoints so you can test the game logic locally before adding MCP complexity.

##### Endpoints We're Building:

- **`POST /rooms`** : Creates a new game room - starts a fresh game
- **`GET /rooms/<room_id>`** : Gets current room state - check game status anytime
- **`POST /rooms/<room_id>/move`** : Makes a move - handles human move + AI response
- **`POST /rooms/<room_id>/chat`** : Sends chat message - talk with AI during game

##### Why These Endpoints?

- **Testing**: Verify game logic works before MCP integration
- **Debugging**: Easy to test with curl/Postman if something breaks
- **Understanding**: See the data flow clearly with direct HTTP calls
- **Validation**: Confirm AI integration responds correctly

##### API Design Philosophy:

- **RESTful**: Standard HTTP methods for predictable behavior
- **Room-Centric**: All operations revolve around room IDs
- **Rich Responses**: Include both raw data and formatted markdown
- **Error Handling**: Clear error messages for debugging

Add these endpoints for testing:

#### Step 6: Local Testing

Time to verify everything works! We'll test each component systematically.

##### What We're Testing:

- **Room Creation**: Can we create new games?
- **Move Validation**: Does the game accept valid moves and reject invalid ones?
- **AI Response**: Does Mistral AI make intelligent counter-moves?
- **Win Detection**: Does the game correctly identify wins and draws?
- **Chat System**: Can we have conversations with the AI?
- **State Persistence**: Do rooms maintain state between requests?

Now let's test our game logic!

##### Start the Flask server:

##### Test with curl commands:

Each test validates a specific piece of functionality:

**1. Create a new game:** *(Tests room creation and initialization)*

*Save the room\_id from the response!*

**2. Make a move:** *(Tests move validation, AI response, game logic)*

**3. Chat with AI:** *(Tests conversational system and AI personality)*

**4. Check game state:** *(Tests data retrieval and markdown formatting)*

**🎉 Success!** Your game logic foundation is solid. You now have:

- A working tic-tac-toe engine
- AI opponent integration
- REST API for testing
- Rich data formatting
- Proper error handling

Next we'll wrap this robust foundation with MCP tools to make it accessible from LeChat!

## Building the MCP Server Layer

Now we'll create the MCP server that wraps our game logic and makes it accessible to LeChat. This layer translates between MCP protocol and our Flask-based game logic.

### Understanding the MCP Layer

#### What MCP Does

MCP (Model Context Protocol) is a bridge between AI assistants and your applications. Think of it as a **translator** that:

- **Exposes Functions**: Your code becomes "tools" that AI assistants can call
- **Handles Communication**: Manages the back-and-forth between LeChat and your game
- **Maintains Context**: Keeps track of game sessions across conversations
- **Formats Responses**: Converts your data into formats AI assistants understand

MCP provides: ✅ **Tool Interface** - AI can directly call game functions  
✅ **Self-Documenting** - Each tool explains when to use it ✅ **Session State** - Maintains game context between calls  
✅ **Rich Responses** - Formatted data that AI can present beautifully

#### The Translation Layer

#### Step 1: Basic MCP Server Structure

##### What We're Building

- **FastMCP Server**: The core MCP protocol handler
- **Session State**: Tracks current user's active game
- **Tool Functions**: 6 functions that wrap our game logic
- **SSE Transport**: Server-Sent Events for real-time communication

Create `mcp_server.py`:

#### Step 2: Create Room Management Tools

Now we'll create the foundational MCP tools that handle game room lifecycle.

##### Tools We're Building:

- **`create_room()`** : Starts new game sessions - the entry point for gameplay
- **`get_room_state(room_id)`** : Checks game status - lets users see current board anytime

##### How They Work:

1. **AI Decides**: Based on user input, AI chooses which tool to call
2. **MCP Validates**: Checks parameters and session state
3. **Game Logic**: Calls our Room class methods
4. **Response Formatting**: Converts results to AI-friendly format
5. **Display**: AI presents formatted results to user

Add the room creation and status tools:

#### Step 3: Implement Game Play Tools

This is where the magic happens! We'll create the tools that handle actual gameplay.

##### Core Gameplay Tool:

- **`make_move(position, room_id)`** : The heart of the game - handles human moves and AI responses

##### What Happens in make\_move():

1. **Validation**: Check if move is legal (valid position, player's turn, game active)
2. **Human Move**: Place X on the board, check for win/draw
3. **AI Response**: If game continues, get AI's counter-move with personality
4. **AI Move**: Place O on board, check for AI win/draw
5. **Formatting**: Create beautiful response with game state and AI trash talk
6. **Return**: Send everything back for AI to display to user

This tool does the work of multiple REST API calls in one function, making the user experience seamless.

Add the core gameplay functionality:

#### Step 4: Add Chat and Utility Tools

Now we'll add the remaining tools that make the game experience complete and user-friendly.

##### Remaining Tools:

- **`send_chat(message, room_id)`** : Talk with AI opponent during games
- **`list_rooms()`** : See all active game sessions
- **`get_help()`** : Show instructions and available commands

Complete the MCP server with chat and helper tools:

#### Step 5: Server Startup

Finally, we'll add the code that actually starts our MCP server and makes it available to the world.

##### What Server Startup Does:

- **Initializes MCP**: Starts the FastMCP server instance
- **Binds to Port**: Makes server accessible on port 7860 (Hugging Face standard)
- **Enables SSE**: Sets up Server-Sent Events transport for real-time communication
- **Logs Status**: Shows what tools are available and confirms readiness

Add the server startup code:

#### Understanding the MCP Tools

Now let's understand how our 6 tools work together to create a complete gaming experience:

##### Primary Game Flow Tools:

- **`create_room()`** : **Entry point** - Initializes new game sessions, sets up AI opponent
- **`make_move(position)`** : **Core gameplay** - Handles human moves + AI responses in one action
- **`get_room_state()`** : **Status check** - Shows current board, whose turn, game outcome

##### Enhanced Experience Tools:

- **`send_chat(message)`** : **Social interaction** - Talk with AI opponent, add personality
- **`list_rooms()`** : **Session management** - Navigate between multiple concurrent games
- **`get_help()`** : **User guidance** - Instructions and tips for new players

##### How They Connect:

Next, we will deploy to Hugging Face Spaces and test with LeChat!

## Deployment to Hugging Face Spaces

Now let's deploy your MCP server to Hugging Face Spaces so it's accessible to LeChat and other MCP clients via the internet.

### Why Hugging Face Spaces?

- **Free hosting** for personal projects
- **Docker support** for custom environments
- **HTTPS by default** (required for MCP/SSE)
- **Easy deployment** from Git repositories
- **Automatic restarts** and health monitoring

#### Step 1: Prepare Your Files

Ensure your project structure looks like this:

#### Step 2: Prepare the Dockerfile

#### Step 3: Create Hugging Face Space

##### 3.1 Create Account

1. Go to [huggingface.co](https://docs.mistral.ai/cookbooks/mistral-lechat_custom_mcp_server-tic-tac-toe-readme)
2. Sign up for a free account
3. Verify your email

##### 3.2 Create New Space

1. Click "Create new" → "Space"
2. **Space name**: `tictactoe-mcp-server` (or your preferred name)
3. **License**: MIT
4. **SDK**: Docker
5. **Visibility**: Public (for free accounts)
6. Click "Create Space"

#### Step 4: Upload Your Code

##### Option A: Git Upload (Recommended)

##### Option B: Web Upload

Use the web interface to upload each file

##### Step 4: Configure Environment Variables

Set Mistral API Key

1. In your Space, click "Settings" tab
2. Scroll to "Variables and secrets"
3. Click "New secret"
4. **Name**: `MISTRAL_API_KEY`
5. **Value**: Your actual Mistral API key
6. Click "Save"

#### Step 5: Monitor Deployment

##### 5.1 Watch Build Process

1. Go to your Space page
2. Watch the "Logs" tab for build progress
3. Look for successful container startup

##### 5.2 Expected Log Output

Now you will have the following details to integrate with LeChat:

1. Space URL: `https://YOUR_USERNAME-tictactoe-mcp-server.hf.space`
2. SSE Endpoint: `https://YOUR_USERNAME-tictactoe-mcp-server.hf.space/sse`

## LeChat Integration

Now that your MCP server is deployed on Hugging Face Spaces, let's connect it to LeChat so you can play tic-tac-toe directly in your chat interface!

### Prerequisites

Before starting, make sure you have:

- ✅ **Deployed MCP Server**: Your tic-tac-toe server running on Hugging Face Spaces
- ✅ **Server URL**: Your Hugging Face Space SSE URL (e.g., `https://yourname-tictactoe-mcp-server.hf.space/sse`)
- ✅ **LeChat Account**: Access to LeChat with MCP connector support

#### Step 1: Add New MCP Connector

Start by adding a new MCP connector to LeChat.

**What's happening here:**

- Navigate to your LeChat settings or connectors section
- Look for "Add Connector" or "New MCP Server" button
- Click to start the connector setup process

This is your **entry point** to connecting external MCP servers like your tic-tac-toe game.

![Add Connector](https://docs.mistral.ai/cookbooks/mistral/lechat_custom_mcp_server/tic-tac-toe/assets/add_connector.png)

#### Step 2: Enter Connector Details

Configure your MCP server connection with the correct details.

**Fill in these details:**

### Server Information:

- **Server Name**: `Tic-Tac-Toe Game` (or your preferred name)
- **Server URL**: `https://yourname-tictactoe-mcp-server.hf.space/sse`
- **Description**: `Interactive tic-tac-toe game with AI opponent`

### Important Note:

- ✅ **Include `/sse` path** - LeChat needs the SSE endpoint, not just the base URL

![Enter Connector Details](https://docs.mistral.ai/cookbooks/mistral/lechat_custom_mcp_server/tic-tac-toe/assets/connector_details.png)

#### Step 3: Select and Enable Connector

Choose your newly configured connector from the available options.

**What you're seeing:**

- Your tic-tac-toe MCP server appears in the connector list
- You can see the server description and capabilities
- Checkbox to enable the connector

If you see errors, double-check:

- Server is running (check Hugging Face Space status)
- URL includes `/sse` endpoint
- No typos in the server URL

![Select Connector](https://docs.mistral.ai/cookbooks/mistral/lechat_custom_mcp_server/tic-tac-toe/assets/select_connector.png)

##### Step 4: Connector Successfully Enabled

Confirm your MCP connector is active and ready to use.

**Success indicators:**

- ✅ **Active connection** indicator
- ✅ **Tools available** - LeChat can see your MCP tools

**What happens next:**

- LeChat can now call your tic-tac-toe MCP tools
- You can start playing games by chatting naturally
- AI assistant will use your tools when appropriate
- Real-time communication established via SSE

![Connector Enabled](https://docs.mistral.ai/cookbooks/mistral/lechat_custom_mcp_server/tic-tac-toe/assets/connector_enabled.png)

##### Success! You can now play Tic-Tac-Toe in LeChat with MistralAI

🎉 **Congratulations!** You now have:

- ✅ **Custom MCP Server** deployed and running
- ✅ **LeChat Integration** with real-time communication
- ✅ **Interactive Gameplay** with intelligent AI opponent
- ✅ **Rich Experience** with markdown game boards and chat
- ✅ **Multi-Session Support** for concurrent games

### What You've Accomplished

You've built a complete **end-to-end integration** from custom application logic to AI chat interface:

1. **Game Logic Foundation** - Room-based tic-tac-toe with AI
2. **MCP Server Layer** - Tools that AI assistants can call
3. **Cloud Deployment** - Production server on Hugging Face Spaces
4. **Chat Integration** - Real-time gameplay in conversational interface

**You've mastered the complete MCP development workflow on LeChat** 🚀

* * *

*Congratulations on building your first custom MCP server integration!*