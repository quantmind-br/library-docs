---
title: mbot Extension | goose
url: https://block.github.io/goose/docs/mcp/mbot-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:24.050648131-03:00
rendered_js: true
word_count: 246
summary: This tutorial explains how to configure and use the MQTT MCP server to control a MakeBlock mbot2 rover through the Goose CLI extension.
tags:
    - mbot2
    - mqtt
    - mcp-server
    - robotics
    - goose-cli
    - iot
    - automation
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

This tutorial will get you started with [deemkeen's MQTT MCP server](https://github.com/deemkeen/mbotmcp) for the [MakeBlock mbot2 rover](https://www.makeblock.com/products/buy-mbot2), and outline some code changes we made along the way.

TLDR

**Command**

```
/path/to/java -jar /path/to/mbotmcp-0.0.1-SNAPSHOT.jar
```

**Environment Variables**

```
MQTT_SERVER_URI: tcp://1.2.3.4:1883
MQTT_PASSWORD: <string or blank>
MQTT_USERNAME: <string or blank>
```

## Configuration[​](#configuration "Direct link to Configuration")

- goose CLI

<!--THE END-->

1. Run the `configure` command:

<!--THE END-->

2. Choose to add a `Command-line Extension`.

```
┌   goose-configure
│
◇  What would you like to configure?
│  Add Extension
│
◆  What type of extension would you like to add?
│  ○ Built-in Extension
│  ● Command-line Extension (Run a local command or script)
│  ○ Remote Extension (Streamable HTTP)
└
```

3. Give your extension a name.

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension
│
◆  What would you like to call this extension?
│  mbot2
└
```

4. Enter the command to run when this extension is used.

info

Replace `/path/to/java` and `/path/to/mbotmcp-0.0.1-SNAPSHOT.jar` with your actual Java installation and JAR file paths.

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension 
│
◇  What would you like to call this extension?
│  mbot2
│
◆  What command should be run?
│  /path/to/java -jar /path/to/mbotmcp-0.0.1-SNAPSHOT.jar
└
```

5. Enter the number of seconds goose should wait for actions to complete before timing out. Default is `300` seconds.

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension
│
◇  What would you like to call this extension?
│  mbot2
│
◇  What command should be run?
│  /path/to/java -jar /path/to/mbotmcp-0.0.1-SNAPSHOT.jar
│
◆  Please set the timeout for this tool (in secs):
│  300
└
```

6. Enter a description for this extension.

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension
│
◇  What would you like to call this extension?
│  mbot2
│
◇  What command should be run?
│  /path/to/java -jar /path/to/mbotmcp-0.0.1-SNAPSHOT.jar
│
◇  Please set the timeout for this tool (in secs):
│  300
│
◆  Enter a description for this extension:
│  Control a MakeBlock mbot2 rover through MQTT and MCP
└
```

7. Add environment variables for this extension.

info

MQTT\_SERVER\_URI has a value like `tcp://1.2.3.4:1883`. MQTT\_USERNAME and MQTT\_PASSWORD are required to exist, but can be empty strings if your MQTT server does not require authentication.

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension
│
◇  What would you like to call this extension?
│  mbot2
│
◇  What command should be run?
│  /path/to/java -jar /path/to/mbotmcp-0.0.1-SNAPSHOT.jar
│
◇  Please set the timeout for this tool (in secs):
│  300
│
◇  Enter a description for this extension:
│  Control a MakeBlock mbot2 rover through MQTT and MCP
│
◆  Would you like to add environment variables?
│  Yes
│
◇  Environment variable name:
│  MQTT_SERVER_URI
│
◇  Environment variable value:
│  ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
│
◇  Add another environment variable?
│  Yes
│
◇  Environment variable name:
│  MQTT_USERNAME
│
◇  Environment variable value:
│  ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
│
◇  Add another environment variable?
│  Yes
│
◇  Environment variable name:
│  MQTT_PASSWORD
│
◇  Environment variable value:
│  ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
│
◇  Add another environment variable?
│  No
│
└  Added mbot2 extension
```

## Example Usage[​](#example-usage "Direct link to Example Usage")

The available commands allow you to drive the mbot2 rover around, including:

- "turn left" or "turn right""
- drive "forward" or "backward"
- "explore" randomly
- "stop" exploring
- "beep"

The default distance to travel is 70cm (about 27 inches), and the turn angles are set to 90 degrees. You can change these values in the [Python code on the mbot2](https://github.com/deemkeen/mbotmcp/blob/main/assets/mbot-mqtt.py). The mbot2 has a lot of other capabilities with the proximity sensors, lights, and color detection sensor on the bottom of the unit that you can add to the Python code, and will need to update [the Java code](https://github.com/deemkeen/mbotmcp/blob/main/src/main/java/de/emkeen/mbotmcp/service/BotService.java) to include those commands via MCP.

#### goose Interaction[​](#goose-interaction "Direct link to goose Interaction")

```
( O)> Let my mbot2 explore the area

    Okay, let's get the mbot2 rover moving. I will send it on a mission to explore the area.

    > Mbotexplore

( O)> stop the rover, turn left and move forward

    Alright, I will stop the rover, turn to the left, and then move it forward.

    > Mbotstop

    > Mbotleft

    > Mbotforward

( O)> let's move backward and beep so I know when it's finished

    Sure, I will move the rover backward and beep when it's done.

    > Mbotbackward

    > Mbotbeep

    Okay, the mbot2 has moved and beeped. What else would you like to do with the rover?

```