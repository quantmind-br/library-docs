---
title: Privacy | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/privacy-security-and-licensing/privacy
source: sitemap
fetched_at: 2026-04-29T15:05:52.121301968-03:00
rendered_js: false
word_count: 6472
summary: Comprehensive list of telemetry events tracked for AI features, agent management, and user interaction metrics within the application.
tags:
    - telemetry-events
    - ai-analytics
    - agent-management
    - event-tracking
    - user-behavior
    - event-logging
category: reference
optimized: true
optimized_at: 2026-04-29T15:05:52Z
---
# Privacy

Telemetry events tracked by Warp, covering AI features, agent management, and user interaction metrics.

## AI Command Search

- **`AI Command Search Modal Opened`** — Opened the modal for AI Command Search
- **`AI Execution Profile Created`** — New AI execution profile was created
- **`AI Execution Profile Deleted`** — AI execution profile was deleted
- **`AI Execution Profile: Added To Allowlist`** — Item added to AI execution profile allowlist
- **`AI Execution Profile: Added To Denylist`** — Item added to AI execution profile denylist
- **`AI Execution Profile: Model Selected`** — AI model selected for an AI execution profile
- **`AI Execution Profile: Removed From Allowlist`** — Item removed from AI execution profile allowlist
- **`AI Execution Profile: Removed From Denylist`** — Item removed from AI execution profile denylist
- **`AI Execution Profile: Setting Updated`** — AI execution profile setting was updated
- **`AI Input Not Sent`** — The AI input was not sent
- **`AI Blocklist Add Suggested Rule Clicked`** — Clicked the Add Suggested Rule button in the AI blocklist
- **`AI Suggested Rule Content Changed`** — Content changed by user in the suggested rule dialog
- **`AI Suggested Rule Edit Clicked`** — Clicked the Edit Suggested Rule button in the AI blocklist

## AIAutonomy

- **`AIAutonomy.AutoexecutedRequestedCommand`** — Autoexecuted an Agent Mode requested command
- **`AIAutonomy.ChangedAgentModeCodingPermissions`** — Changed Agent Mode permissions for coding tasks
- **`AIAutonomy.ToggledAutoexecuteReadonlyCommandsSetting`** — Toggled setting to autoexecute readonly Agent Mode requested commands

## Subshell & SSH

- **`Add Added Subshell Command`** — Added a command to be automatically Warpified via Warp's subshell wrapper
- **`Add Denylisted SSH Tmux Wrapper Host`** — Added an SSH host to the denylist for prompting for Tmux Wrapper
- **`Add Denylisted Subshell Command`** — Explicitly prevent a command from being Warpified via Warp's subshell wrapper
- **`Added Tab with Specific Shell`** — Added a tab with specific shell
- **`Attached Workflow Alias`** — Added an alias to a Warp Drive workflow

## Agent Management

- **`Agent Management View Copied Session Link`** — User copied a session link from the Agent Management View
- **`Agent Management View Opened Session`** — User opened a session from the Agent Management View
- **`Agent Management View Toggled`** — User toggled the Agent Management View open or closed
- **`Agent Mode Query Suggestion Accepted`** — Prompt Suggestion accepted
- **`Agent Mode Query Suggestions Banner Shown`** — Prompt Suggestions banner shown
- **`Agent Mode Setup Banner Accepted`** — Agent Mode setup banner accepted
- **`Agent Mode Setup Banner Dismissed`** — Agent Mode setup banner dismissed
- **`Agent Mode Setup Project Scoped Rules Action`** — User clicked a button in the Agent Mode setup project scoped rules step
- **`Agent Mode.Setup Codebase Context Action`** — User clicked a button in the Agent Mode setup Codebase Context step
- **`Agent Predict Completed`** — Completed an Agent Predict prediction
- **`Agent Tip Dismissed`** — User dismissed the use-agent toolbar

## AgentManagement

- **`AgentManagement.AgentTypeSelectorOpened`** — User opened the agent type selector from agent management
- **`AgentManagement.ArtifactClicked`** — User clicked an artifact button
- **`AgentManagement.CloudRunCancelled`** — User cancelled a cloud run
- **`AgentManagement.CloudRunOpened`** — User opened a cloud run
- **`AgentManagement.ConversationForked`** — User forked a conversation
- **`AgentManagement.ConversationLinkCopied`** — User copied a conversation link
- **`AgentManagement.ConversationOpened`** — User opened a conversation
- **`AgentManagement.DetailsPanelContinueLocally`** — User clicked Continue locally in the details panel
- **`AgentManagement.DetailsViewed`** — User clicked View details
- **`AgentManagement.DismissSetupGuide`** — User dismissed the ambient agent setup guide
- **`AgentManagement.FilterChanged`** — User changed a filter in the management view
- **`AgentManagement.OpenSetupGuide`** — User opened the ambient agent setup guide
- **`AgentManagement.SessionLinkCopied`** — User copied a session link
- **`AgentManagement.SetupGuideDocsLink`** — User clicked a docs URL in the setup guide
- **`AgentManagement.SetupGuideStepCopy`** — User copied a workflow step from the setup guide
- **`AgentManagement.SetupGuideStepRun`** — User ran a workflow step from the setup guide
- **`AgentManagement.SpawnNewCloudAgent`** — User spawned a new cloud agent from agent management
- **`AgentManagement.SpawnNewLocalAgent`** — User spawned a new local agent from agent management
- **`AgentManagement.TombstoneArtifactClicked`** — User clicked an artifact in the tombstone view
- **`AgentManagement.TombstoneContinueLocally`** — User clicked Continue locally in the tombstone
- **`AgentManagement.ViewToggled`** — User toggled the agent management view open or closed

## AgentMode

- **`AgentMode.Attached Context`** — Attached block as context to an Agent Mode query
- **`AgentMode.Attached Images`** — Attached images to an Agent Mode query
- **`AgentMode.ChangedInputType`** — Input type changed from shell to AI or AI to shell
- **`AgentMode.ClickedEntrypoint`** — Clicked on an Agent Mode entrypoint
- **`AgentMode.Code.DiffHunksNavigated`** — Agent Mode Code diff hunks navigated
- **`AgentMode.Code.DiffMatchFailed`** — Failed to match code diff
- **`AgentMode.Code.FileExceededContextLimit`** — File from AI exceeded context limit
- **`AgentMode.Code.FilesNavigated`** — Agent Mode Code files navigated
- **`AgentMode.Code.InvalidFile`** — File(s) in code diff could not be found
- **`AgentMode.Code.MalformedFinalLineProxy`** — Suggested code diff likely required malformed trailing line correction
- **`AgentMode.Code.MissingLineNumbers`** — Code diff was missing line numbers
- **`AgentMode.Code.SuggestedCodeEditedByUser`** — Agent Mode Code suggestion edited by user
- **`AgentMode.Code.SuggestedEditAcceptAndContinueClicked`** — User selected Accept and start conversation for a code diff suggestion
- **`AgentMode.Code.SuggestedEditAcceptClicked`** — User selected Accept for a code diff suggestion
- **`AgentMode.Code.SuggestedEditReceived`** — Agent Mode suggested a code edit
- **`AgentMode.Code.SuggestedEditResolved`** — Agent Mode pending code edit suggestion resolved
- **`AgentMode.CreatedBlock`** — Created an AI block in agent mode
- **`AgentMode.ErrorReceived`** — Received an error when getting Agent Mode response
- **`AgentMode.ExecutedWarpDrivePrompt`** — Executed a Warp Drive prompt
- **`AgentMode.ExitedShellProcess`** — An agent-requested command caused the shell process to exit
- **`AgentMode.FileGlob.Failed`** — The file glob tool failed to complete
- **`AgentMode.FileGlob.Succeeded`** — The file glob tool completed successfully
- **`AgentMode.GrepTool.Failed`** — The grep tool failed to complete
- **`AgentMode.GrepTool.Succeeded`** — The grep tool completed successfully
- **`AgentMode.NaturalLanguageDetection.InputBufferSubmitted`** — Natural language detection submitted
- **`AgentMode.CitationOpened`** — Opened a citation that was surfaced in agent mode
- **`AgentMode.Orchestration.TeamAgentCommunicationFailed`** — Failed to send orchestration message for a TeamAgent
- **`AgentMode.PotentialAutoDetectionFalsePositive`** — Manually toggled input to shell mode after auto-detection
- **`AgentMode.QueryAttemptAtLimit`** — Tried to send a query but reached the query limit
- **`AgentMode.RequestRetrySucceeded`** — Agent Mode request succeeded after retrying
- **`AgentMode.SetupCreateEnvironmentAction`** — User clicked a button in the Agent Mode setup create environment step
- **`AgentMode.SurfacedCitations`** — Agent mode used and cited external sources
- **`AgentMode.ToggleAutoDetectionSetting`** — Toggled natural language auto-detection setting
- **`AgentMode.NotificationShown`** — An agent notification was shown to the user
- **`AgentMode.Tip LinkClicked`** — User clicked a link or action in an Agent Tip
- **`AgentMode.Tip Selected`** — Selected an Agent Tip to show in the Agent Mode status bar
- **`AgentMode.ViewEntered`** — User entered the Agent View
- **`AgentMode.View Exited`** — User exited the Agent View

## AgentView

- **`AgentView.InlineConversationMenuItemSelected`** — User selected an item from the inline conversation menu
- **`AgentView.InlineConversationMenuOpened`** — User opened the inline conversation menu in Agent View
- **`AgentView.ShortcutsViewToggled`** — User toggled the shortcuts view in Agent View

## Agentic Onboarding

- **`AgenticOnboarding.BlockSelected`** — Selected an agentic onboarding block to execute

## AmbientAgent

- **`AmbientAgent.CloudMode.Entered`** — User entered cloud agent view
- **`AmbientAgent.CloudMode.EnvironmentSelector.Opened`** — User opened the environment selector menu
- **`AmbientAgent.CloudMode.EnvironmentSelector.Selected`** — User selected an environment from the selector
- **`AmbientAgent.CloudMode.EnvironmentSettings.GitHubAuth`** — User started GitHub authentication from the environment form
- **`AmbientAgent.CloudMode.EnvironmentSettings.LaunchedAgent`** — User launched an environment setup agent
- **`AmbientAgent.ConcurrencyModal.Dismissed`** — User dismissed the cloud agent capacity modal
- **`AmbientAgent.ConcurrencyModal.Opened`** — User opened the cloud agent capacity modal
- **`AmbientAgent.ConcurrencyModal.UpgradeClicked`** — User clicked the upgrade button in the capacity modal
- **`AmbientAgent.DispatchFailed`** — Ambient agent failed to dispatch or encountered an error
- **`AmbientAgent.EnvironmentSettings.CreatedEnvironment`** — User created a new environment
- **`AmbientAgent.EnvironmentSettings.DeletedEnvironment`** — User deleted an environment
- **`AmbientAgent.EnvironmentSettings.Image.Suggested`** — Docker image was suggested for an environment
- **`AmbientAgent.EnvironmentSettings.Image.SuggestionFailed`** — Docker image suggestion failed
- **`AmbientAgent.EnvironmentSettings.Opened`** — User opened the environment management pane
- **`AmbientAgent.EnvironmentSettings.UpdatedEnvironment`** — User updated an existing environment

## Anonymous User

- **`Anonymous User Attempted Login-Gated Feature`** — Anonymous user attempted to access a login-gated feature
- **`Anonymous User Expiration Lockout`** — Anonymous user opened Warp after their conversion deadline and was locked out
- **`Anonymous User Hit Cloud Object Limit`** — Anonymous user attempted to create a cloud object past their personal object limit
- **`Anonymous User Initiated Signup`** — An anonymous user initiated the sign up flow
- **`Anonymous User Linked from Browser`** — Received an auth payload from anonymous user after linking in browser
- **`App Installed Via`** — Whether Warp was installed from the home page or through homebrew

## Warp Drive

- **`Attached Workflow Alias Environment Variables`** — Added or removed environment variables for a Warp Drive workflow alias
- **`Deleted Notebook`** — Deleted notebook from Warp Drive team
- **`Deleted Workflow`** — Deleted workflow from Warp Drive team
- **`Edited Workflow Alias Argument`** — Edited an argument in a Warp Drive workflow alias
- **`Cloned Object`** — Cloned a Warp Drive object
- **`Exported Object`** — Exported a Warp Drive object
- **`Invoked Environment Variables`** — Invoked an environment variables object
- **`Modified Sorting`** — Modified the sorting scheme for Warp Drive objects
- **`Removed Alias`** — Removed an alias from a Warp Drive workflow
- **`Remove User`** — Remove user from Warp Drive team
- **`Created Team`** — Created a Warp Drive team
- **`Copied Team Link`** — Copied a Warp Drive team link
- **`Sent Team Invites`** — Sent email invites for Warp Drive team
- **`Sent Teammate Invites`** — Sent emails to invite teammates to join Warp Drive team
- **`Workflow Selected`** — Selected workflow and populated into the Input Editor
- **`Warp Drive Sharing Onboarding Block Shown`** — Showed onboarding block for Warp Drive sharing
- **`Warp Drive Object Opened on Desktop`** — Warp Drive object on the web was opened on the desktop

## App & Session

- **`Attempting to Relaunch for Update`** — Attempted to relaunch the app after installing an update
- **`Background Output Block Created`** — Warp created a background-output Block
- **`Block Filter Toolbelt Button Clicked`** — Clicked the block filter icon in the top-right of a block
- **`Bootstrap Block Contents`** — Contents of the bootstrap block if bootstrapping is slow
- **`Bootstrap Slow`** — Slow bootstrap on session startup
- **`Bootstrap Successful`** — Successful bootstrap for session
- **`Database Read Error`** — Database read error when trying to get app state for session restoration
- **`Database Init Failed`** — Failed to initialize sqlite upon startup
- **`Database Write Error`** — Database write error when trying to write app state for session restoration
- **`Decline Subshell Bootstrap`** — Developer declined the Warp banner to Warpify the current session
- **`Edited Input Before Precmd`** — Input edited before precmd hook completes
- **`InitialWorkingDirectoryConfigurationChanged`** — Replaced the default working directory with a different path
- **`Isolation Detected`** — Detected that Warp is running in an isolated sandbox
- **`Joined Shared Session`** — When you join another instance of Warp using shared sessions
- **`Jumped to Bottom of Block Button Clicked`** — Used the button to jump to the bottom of a Block
- **`Jumped to Previous Command`** — Jumped to a previous command
- **`Jumped to Shared Session Participant`** — Clicked on a shared session participant avatar
- **`Move Active Tab`** — Move active tab left or right
- **`Need Re-authentication`** — User needs to re-authenticate
- **`New Session From Directory`** — Dragged a file, folder, etc. into Warp to start a session
- **`Notebook Operation`** — Took an action on a notebook
- **`Opened Context Menu`** — Opened context menu
- **`Opened Launch Config`** — Opened launch config for a session
- **`Opened Launch Config YAML`** — Opened the launch config YAML file
- **`Parameterized Workflow With Environment Variables`** — Selected from environment variables dropdown
- **`Parsed Config in Settings Import`** — Parsed a terminal's settings as part of settings import
- **`Promoted Preview Code Tab`** — Promoted a preview code tab to a normal tab
- **`Received Subshell RC File DCS`** — Spawned a subshell to be automatically Warpified
- **`Remote Server Binary Check`** — Remote server binary check completed
- **`RemoteServer.ClientRequestError`** — A client request to the remote server failed
- **`RemoteServer.Disconnection`** — An established remote server connection was dropped
- **`RemoteServer.Initialization`** — Remote server connection and initialization completed
- **`RemoteServer.Installation`** — Remote server binary installation completed
- **`RemoteServer.MessageDecodingError`** — A server message could not be decoded
- **`RemoteServer.SetupDuration`** — End-to-end duration of the remote server setup flow
- **`Saved Launch Configuration`** — Saved current launch configuration
- **`Session Abandoned Before Bootstrap`** — Abandoned session before the bootstrapping completes
- **`Shell Terminated Prematurely`** — The shell process terminated prematurely
- **`Split Tab`** — Split tab into multiple panes
- **`Tab Operation`** — Took operation on a tab
- **`Tried to Execute Before Precmd`** — Attempted to execute command before precmd
- **`Triggered Command X-Ray`** — Triggered Command X-Ray
- **`Unable to Update To New Version`** — Update available but not authorized to install
- **`Reopened Tab or Window`** — Re-opened a closed tab or window
- **`Unhandled Editor Modifier Key`** — Used modifier keybinding keystroke which is not supported
- **`Unsupported Shell`** — Booted Warp with a shell that isn't supported
- **`User Initiated Closing Something`** — Attempted to either quit the app or close a window
- **`User Logged Out`** — Confirms a user has explicitly logged out of the application

## CLI

- **`CLI Subagent Action Executed`** — User approved a blocked action from the CLI subagent
- **`CLI Subagent Action Rejected`** — User rejected a blocked action from the CLI subagent
- **`CLI Subagent Control State Changed`** — Control state changed in CLI subagent
- **`CLI Subagent Input Dismissed`** — User dismissed the input in the CLI subagent
- **`CLI Subagent Responses Toggled`** — User toggled the visibility of agent responses
- **`Listed Agents`** — Listed agents from the Warp CLI
- **`CLI.Execute.Agent.Profile.List`** — Listed agent profiles from the Warp CLI
- **`CLI.Execute.Agent.Run`** — Ran an agent from the Warp CLI
- **`CLI.Execute.Agent.RunAmbient`** — Ran an ambient agent from the Warp CLI
- **`CLI.Execute.Artifact.Download`** — Downloaded an artifact from the Warp CLI
- **`CLI.Execute.Artifact.GetMetadata`** — Got artifact metadata from the Warp CLI
- **`CLI.Execute.Artifact.Upload`** — Uploaded an artifact from the Warp CLI
- **`CLI.Execute.Conversation.Get`** — Got conversation by ID from the Warp CLI
- **`CLI.Execute.Environment.Create`** — Created a cloud environment from the Warp CLI
- **`CLI.Execute.Environment.Delete`** — Deleted a cloud environment from the Warp CLI
- **`CLI.Execute.Environment.Get`** — Got cloud environment details from the Warp CLI
- **`CLI.Execute.Environment.Image.List`** — Listed available base images from the Warp CLI
- **`CLI.Execute.Environment.List`** — Listed cloud environments from the Warp CLI
- **`CLI.Execute.Environment.Update`** — Updated a cloud environment from the Warp CLI
- **`CLI.Execute.Federate.IssueGcpToken`** — Issued a GCP federated identity token from the Warp CLI
- **`CLI.Execute.Federate.IssueToken`** — Issued a federated identity token from the Warp CLI
- **`CLI.Execute.Integration.Create`** — Created an integration from the Warp CLI
- **`CLI.Execute.Integration.List`** — Listed integrations from the Warp CLI
- **`CLI.Execute.Integration.Update`** — Updated an integration from the Warp CLI
- **`CLI.Execute.Login`** — Logged in via the Warp CLI
- **`CLI.Execute.Logout`** — Logged out via the Warp CLI
- **`CLI.Execute.McpServers.List`** — Listed MCP servers from the Warp CLI
- **`CLI.Execute.Models.List`** — Listed models from the Warp CLI
- **`CLI.Execute.Provider.List`** — Listed providers from the Warp CLI
- **`CLI.Execute.Provider.Setup`** — Set up a provider via the Warp CLI
- **`CLI.Execute.Run.Conversation.Get`** — Got run conversation from the Warp CLI
- **`CLI.Execute.Schedule.Create`** — Created a scheduled agent from the Warp CLI
- **`CLI.Execute.Schedule.Delete`** — Deleted a scheduled agent from the Warp CLI
- **`CLI.Execute.Schedule.Get`** — Got scheduled agent configuration from the Warp CLI
- **`CLI.Execute.Schedule.List`** — Listed scheduled agents from the Warp CLI
- **`CLI.Execute.Schedule.Pause`** — Paused a scheduled agent from the Warp CLI
- **`CLI.Execute.Schedule.Unpause`** — Unpaused a scheduled agent from the Warp CLI
- **`CLI.Execute.Schedule.Update`** — Updated a scheduled agent from the Warp CLI
- **`CLI.Execute.Secret.Create`** — Created a secret from the Warp CLI
- **`CLI.Execute.Secret.Delete`** — Deleted a secret from the Warp CLI
- **`CLI.Execute.Secret.List`** — Listed secrets from the Warp CLI
- **`CLI.Execute.Secret.Update`** — Updated a secret from the Warp CLI
- **`CLI.Execute.Task.GetStatus`** — Got status of task from the Warp CLI
- **`CLI.Execute.Task.List`** — Listed tasks from the Warp CLI
- **`CLI.Execute.User`** — Printed current user info from the Warp CLI

## CLI Agent

- **`CLIAgentFooter.ImageAttached`** — User attached an image from the CLI agent footer
- **`CLIAgentFooter.SettingToggled`** — User toggled the CLI agent footer setting
- **`CLIAgentFooter.Shown`** — CLI agent footer was shown to the user
- **`CLIAgentFooter.VoiceInputUsed`** — User used voice input from the CLI agent footer
- **`CLIAgentPlugin.ChipClicked`** — User clicked the plugin install or update chip
- **`CLIAgentPlugin.ChipDismissed`** — User dismissed the plugin install or update chip
- **`CLIAgentPlugin.Detected`** — A CLI agent plugin was detected via a SessionStart event
- **`CLIAgentPlugin.OperationFailed`** — Auto plugin install or update failed
- **`CLIAgentPlugin.OperationSucceeded`** — Auto plugin install or update completed successfully
- **`CLIAgentRichInput.Closed`** — CLI agent Rich Input was closed
- **`CLIAgentRichInput.Opened`** — User opened CLI agent Rich Input
- **`CLIAgentRichInput.Submitted`** — User submitted a prompt via CLI agent Rich Input

## Code Review

- **`Code Review Pane Opened`** — Opened the code editor pane from various sources
- **`Code Review File Opened`** — Opened a file from code review, project explorer, or global search
- **`Code Review Context Added`** — Content added to AI context from code review
- **`Code Review Diff Base Changed`** — Diff base changed in code review
- **`CodeReview.CalculateDiffMetadataFailed`** — Failure when calculating diff metadata
- **`CodeReview.Comment Added`** — Inline code review comment added
- **`CodeReview.CommentDeleted`** — Inline code review comment deleted
- **`CodeReview.Comment Edited`** — Inline code review comment edited
- **`CodeReview.CommentEditorOpened`** — Inline code review comment editor opened
- **`CodeReview.CommentListExpanded`** — Inline code review comment list expanded
- **`CodeReview.CommentListItemClicked`** — Inline code review comment list item clicked
- **`CodeReview.CommentRelocationFailed`** — Inline code review comment relocation fell back to approximate line
- **`CodeReview.CommentResolved`** — Inline code review comment resolved
- **`CodeReview.CommentsAttached`** — Newly-imported comments relocated against editor lines
- **`CodeReview.CommentsReceived`** — Agent insert_code_review_comments tool call received
- **`Code Review File Saved`** — File saved in code review pane
- **`CodeReview.FindBarModeChanged`** — Search mode changed in code review find bar
- **`CodeReview.FindBarToggled`** — Code review find bar opened or closed
- **`Code Review Find Navigated`** — Navigated to next or previous match in code review find bar
- **`CodeReview.LoadDiffFailed`** — Failure when loading diff content
- **`CodeReview.PaneStateChanged`** — Code review pane minimized or maximized
- **`CodeReview.RevertHunkClicked`** — Revert hunk button clicked
- **`CodeReview.ReviewSubmitted`** — Inline code review submitted to agent

## CodeView

- **`CodeView.SelectionAddedAsContext`** — Added selected code as context from the code editor

## Codex

- **`Codex Modal Opened`** — User opened the Codex modal
- **`CodexModal.UseCodexClicked`** — User clicked 'Use Codex' in the Codex modal

## Command Correction

- **`Command Correction Accepted`** — Accepted command correction

## Shell Execution

- **`Shell Executable Opened`** — Opened a .cmd or unix executable file and ran it directly in Warp

## Command Palette

- **`Command Palette Search Accepted`** — Accepted a command palette search result
- **`Command Palette Search Exited`** — Exited command palette search without accepting
- **`Command Search Async Query Completed`** — Finished searching for a command in the background
- **`Command Search Exited`** — Exited command search without accepting a result
- **`Command Search Filter Changed`** — Changed command search filter
- **`Command Search Opened`** — Opened command search
- **`Command Search Result Accepted`** — Accepted command search result
- **`Select Command Palette Option`** — Selected option from Command Palette
- **`Select Navigation Palette Item`** — Selected session from the Session Navigation Palette

## Welcome & Onboarding

- **`Completed Welcome Tips`** — Completed all welcome tips items
- **`Completed Settings Import`** — Imported a terminal's settings via the settings import onboarding block
- **`Create Project Prompt Submitted`** — User submitted a prompt from the create project view
- **`Create Project Prompt Submitted Content`** — User submitted custom prompt content
- **`Clone Repo Prompt Submitted`** — User submitted a repository URL from the clone repo view
- **`Open Repo Folder Submitted`** — User selected a folder to open as a repo
- **`Get Started Skip to Terminal`** — User clicked skip to terminal from get started view
- **`Settings Import Initiated`** — Started the import settings flow for new users
- **`Clicked Reset to Defaults Button in Settings Import`** — Reset the imported settings
- **`Focused Config in Settings Import`** — Selected a terminal in the settings import
- **`onboarding_agent_slide_upgrade_clicked`** — User clicked the Upgrade button on the Customize your agent slide
- **`onboarding_callout_completed`** — User completed the callout flow
- **`onboarding_callout_displayed`** — A callout was displayed to the user
- **`onboarding_callout_next_clicked`** — User clicked next on a callout
- **`onboarding_folder_selected`** — A folder was selected during onboarding
- **`onboarding_folder_selection_started`** — User started folder selection
- **`onboarding_free_user_no_ai_upgrade_clicked`** — User clicked the upgrade button on the free-user experiment slide
- **`onboarding_get_started_clicked`** — User clicked the Get Started button
- **`onboarding_setting_changed`** — User changed a setting during onboarding
- **`onboarding_slide_navigated_back`** — User navigated to the previous slide
- **`onboarding_slide_navigated_next`** — User navigated to the next slide
- **`onboarding_slide_viewed`** — User viewed a slide in the onboarding flow
- **`onboarding_slides_completed`** — User completed the onboarding slides
- **`onboarding_started`** — User started the onboarding flow
- **`onboarding_welcome_login_clicked`** — User clicked the Log in link on the welcome slide

## Computer Use

- **`RequestComputerUse Approved`** — A RequestComputerUse action was approved
- **`RequestComputerUse Rejected`** — A RequestComputerUse action was cancelled/rejected

## Tab Completion

- **`Tab Completion Accepted`** — Accepted tab completion suggestion
- **`Tab Single Result Autocompletion`** — Accepted tab completion and inserted into Input Editor

## Context Menu

- **`Context Menu Copied`** — Clicked "Copy" in context menu
- **`Context Menu Copied Prompt`** — Clicked "Copy Prompt" in context menu
- **`Context Menu Copy Selected Text`** — Clicked "Copy selected text" in context menu
- **`Context Menu Insert Selected Text`** — Clicked "insert into input" in context menu
- **`Context Menu Toggle Git Prompt Dirty Indicator`** — Toggled indicator of dirty git prompt
- **`Context Menu: Find Within Blocks`** — Clicked "find within blocks" in context menu
- **`Context Menu: Initiate Block Sharing`** — Opened "Share" modal via context menu
- **`Context Menu: Reinput Commands`** — Clicked "reinput commands" in context menu
- **`Context Menu Share Block`** — Clicked "Share block..." in context menu
- **`Context Menu Copy Link`** — Clicked "Copy Link" on Referral Modal

## Conversation

- **`ConversationList.ItemDeleted`** — Deleted a conversation from the conversation list
- **`ConversationList.ItemOpened`** — Opened a conversation from the conversation list
- **`ConversationList.LinkCopied`** — Copied a conversation link from the conversation list
- **`ConversationList.Opened`** — Opened the conversation list view in the left panel
- **`Copied Shared Session Link`** — Copied a shared session link

## Secrets

- **`Secret Copied`** — Copied a secret's obfuscated contents to clipboard
- **`Custom Secret Regex Added`** — Custom Secret Regex Added

## Theme & Appearance

- **`Theme Created`** — Created a custom theme using the built-in theme creator
- **`Theme Deleted`** — Deleted a custom theme using the built-in theme creator
- **`Theme Chooser Opened`** — Opened theme chooser
- **`Theme Creator Opened`** — Opened theme creator modal
- **`Thin Strokes Setting Changed`** — Changed thin strokes setting
- **`Changed invite view option`** — Toggled between link and invite for invite

## Session & Blocks

- **`Jumped to Bookmark`** — Jumped to bookmarked Block
- **`Bookmark Toggled`** — Bookmarked or unbookmarked Block
- **`Block Sharing Link Generated`** — Generated Block sharing link
- **`Generate Block Sharing Link`** — Generated Block sharing link
- **`Clicked Continue Conversation Button`** — User clicked the Continue Conversation button
- **`Showed File in Finder`** — Opened a file in Finder

## Settings & Preferences

- **`Settings Features Changed`** — Changed settings in Features Page
- **`Settings Find Toggle Changed`** — Changed settings in Find Toggle
- **`Settings Environments.PageOpened`** — User opened the Environments settings page
- **`Input Editor Mode Changed`** — Changed the Input Editor Mode
- **`Input UX Mode Changed`** — Changed the input UX mode
- **`Input Context Chip Interacted`** — Interacted with a context chip

## Global Search

- **`Global Search View Opened`** — Opened the global search view
- **`Global Search Query Started`** — Started a global search

## File Tree

- **`File Tree Opened`** — Opened the file tree/project explorer
- **`FileTree.AttachedAsContext`** — Attached a file or directory as context from the file tree
- **`File Tree New File`** — Created a new file from the file tree

## Keybindings

- **`Keybinding Edited`** — Edited a custom keybinding
- **`Keybinding Removed`** — Removed / cleared a keybinding
- **`Keybinding Reset to Default`** — Reset a custom keybinding to its default
- **`Resource Center Keybindings Page Opened`** — Opened the keybinding page within the resource center

## Import & Export

- **`ITerm Profile Multiple Hotkeys`** — Attempted to import an iTerm profile with multiple hotkey bindings
- **`Antivirus Identified`** — Identified running antivirus software

## Authentication

- **`Auth Re-authenticate Started`** — Started the flow to re-authenticate the client
- **`Auth Common Question Clicked in App`** — Clicked on "Common Question" when logging in
- **`Auth: Open Privacy Settings Overlay`** — Privacy settings are open during sign-in
- **`Auth: Toggle Common Questions`** — Toggled FAQ Page when logging in
- **`Changed invite view option`** — Toggled between link and invite for invite
- **`Don't Show Sharer Grant Modal Again`** — Checked don't show again on the confirmation modal
- **`Log In Button Clicked in App`** — Clicked on "Log in" button
- **`Logged Out`** — Logged out of the Warp client
- **`Log Out Modal Cancel Pressed`** — Escaped the log out flow by canceling the modal
- **`Log Out Modal Displayed`** — When the log out modal is displayed
- **`Login Started Logged Out`** — Started Warp in the logged-out / signed-out state
- **`Login Later Button Clicked`** — Clicked "Login later" button
- **`Login Later Confirmation Button Clicked`** — Clicked "Yes, skip login" confirmation button
- **`Sign Up Button Clicked in App`** — A user clicked the sign up button
- **`Sharer Cancelled Grant Role`** — Cancelled granting a role to a shared session participant
- **`User Menu Upgrade Clicked`** — Clicked the 'Upgrade' menu item in the user menu

## LSP & Editor

- **`LSP Control Action`** — User performed an LSP control action from the footer menu
- **`LSP Find References`** — Find references card displayed via LSP
- **`LSP Goto Definition`** — User triggered goto definition via LSP
- **`LSP Hover Tooltip`** — Hover tooltip displayed with LSP content or diagnostics
- **`LSP Server Enabled`** — User enabled an LSP server for a workspace
- **`Lsp.ServerEnablementSkipped`** — User skipped LSP enablement during /init
- **`LSP Server Failed`** — LSP server failed to start
- **`Lsp.ServerInstallCompleted`** — An LSP server installation finished
- **`LSP Server Removed`** — User removed an LSP server
- **`LSP Server Started`** — LSP server successfully started and is available
- **`MCP Server Collection Pane Opened`** — MCP Server Collection Pane Opened
- **`Page Up/Down In Editor Pressed`** — Pressed `PAGE-UP` or `PAGE-DOWN` within the Input Editor

## Notifications

- **`Notification Clicked`** — Clicked desktop notification sent from Warp
- **`Notification Failed to Send`** — Failed to send desktop notification
- **`Notification Permissions Requested`** — Requested permission for desktop notification permissions
- **`Notification Request Permissions Outcome`** — Recorded outcome of attempting to request notification permissions
- **`Notification Sent`** — Sent desktop notification
- **`Notifications Discovery Banner Action`** — Showed banner introducing the notifications feature
- **`Notifications Error Banner Action`** — Showed error banner for notifications feature
- **`ShowNotificationsDiscoveryBanner`** — Showed notifications discovery banner in the block list
- **`ShowNotificationsErrorBanner`** — Showed error banner for notifications feature

## Pane Management

- **`Pane Drag Ended`** — Ended dragging a pane via the pane header
- **`Pane Drag Initiated`** — Initiated dragging a pane via the header

## Quit & Alerts

- **`Quit Modal Cancel Pressed`** — `Cancel` button on the alert modal was pressed
- **`Quit Modal Disabled`** — The quit modal dialog has been disabled
- **`Quit Warning Displayed`** — Showed an alert modal to warn the user about closing the app

## Recent Items

- **`Recent Menu Item Selected`** — User selected an item from the recents list on the new tab zero state

## Resource Center

- **`Resource Center Pane Opened`** — Opened Resource Center pane
- **`Resource Center Tips Completed`** — Completed resource center tips
- **`Resource Center Tips Skipped`** — Skipped welcome tips for new users

## SSH

- **`SSH Session Bootstrap Attempted`** — Attempted bootstrapping for an SSH session
- **`SSH ControlMaster Error`** — Encountered a ControlMaster error during an SSH session
- **`SSH Install Tmux Block Accepted`** — User accepted an ssh install tmux block
- **`SSH Install Tmux Block Dismissed`** — User dismissed an ssh install tmux block
- **`SSH Install Tmux Block Displayed`** — Displayed an ssh install tmux block
- **`SSH Interactive Session Detected`** — An interactive SSH session was detected
- **`SSH Remote Server Choice Do Not Ask Again Toggled`** — Toggled the 'Don't ask me this again' checkbox
- **`SSH Tmux Warpification Error Block`** — Ssh tmux warpification errored out
- **`SSH Tmux Warpification Succeeded`** — Ssh tmux warpification succeeded
- **`SSH Tmux Warpify Block Accepted`** — User accepted an ssh tmux warpify block
- **`SSH Tmux Warpify Block Dismissed`** — User dismissed an ssh tmux warpify block

## Subshell Management

- **`Remove Added Subshell Command`** — Removed a command from the list of commands to automatically Warpify
- **`Remove Denylisted SSH Tmux Wrapper Host`** — Removed an SSH host from the denylist
- **`Remove Denylisted Subshell Command`** — Removed a command from the list of commands to IGNORE

## Tab Configs

- **`TabConfigs.ExistingConfigOpened`** — User opened an existing saved tab config
- **`TabConfigs.GuidedModalOpened`** — User opened the guided Create a tab config modal
- **`TabConfigs.GuidedModalSubmitted`** — User submitted the guided Create a tab config modal
- **`TabConfigs.MenuCreateNewTabConfigClicked`** — User clicked the New tab config entry
- **`TabConfigs.NewWorktreeConfigOpened`** — User opened a new worktree config
- **`OpenAndWarpifyDockerSubshell`** — Warpifying a docker subshell from using the docker extension
- **`Opened Workflows Search`** — Opened workflows search in command search pane

## Tools & Skills

- **`Skill Opened`** — A skill was opened from an 'open skill' button or /edit-skill command
- **`Skill Read`** — A skill was read via the ReadSkill tool call

## Slash Commands

- **`Slash Commands Menu Opened`** — Opened the slash commands menu
- **`Slash Command Accepted`** — User accepted a slash command

## Suggestions

- **`Suggestion Menu Opened`** — Opened a suggestion menu
- **`Static Prompt Suggestion Accepted`** — Static Prompt Suggestion accepted
- **`Static Prompt Suggestions Banner Shown`** — Static Prompt Suggestions banner shown
- **`Suggested Code Diff Banner Shown`** — Suggested Code Diff banner shown
- **`Suggested Code Diff Failed`** — Suggested Code Diff Failed
- **`Suggested Prompt Accepted`** — Suggested prompt accepted
- **`Suggested Prompt Cancelled`** — Suggested prompt cancelled
- **`Zero State Prompt Suggestion Used`** — Used a zero state prompt suggestion

## Warp AI

- **`Warp AI Toggled`** — Toggled Warp AI
- **`Warp AI Question Issued`** — Issued a question to Warp AI
- **`Warp AI Action Executed`** — Executed a Warp AI action: Restart, Copy, Insert into terminal
- **`Warp AI Character Limit Exceeded`** — Attempted to ask a question longer than 1k chars
- **`Used Warp AI Prepared Prompt`** — Used one of the Warp-provided prompts
- **`Generated Metadata For Workflow Error`** — Failed to generate metadata for a workflow
- **`Generated Metadata For Workflow Success`** — Successfully generated metadata for a workflow

## Input Editor

- **`Input Editor Context Menu Opened`** — Opened the Input Editor's context menu
- **`Input Editor AI Context Menu Opened`** — Opened AI Command Search via the Input Editor's context menu
- **`Input Editor Ask Warp AI Clicked`** — Clicked "Ask Warp AI" from the Input Editor's context menu
- **`Input Editor Command Search Context Menu Opened`** — Opened Command Search via the Input Editor's context menu
- **`Input Editor Copy`** — Copied selected text from Input Editor
- **`Input Editor Paste`** — Pasted text into the Input Editor's via its context menu
- **`Input Editor Select All`** — Selected all the text in the Input Editor via its context menu
- **`Input Editor Sent`** — Sent text from Input Editor

## Welcome Tips

- **`Welcome Tips Opened`** — Opened welcome tips in app
- **`Changelog Opened`** — Opened the changelog link within the App

## Session Sharing

- **`Shared Session Link Copied`** — Copied a shared session link
- **`Sharing Settings Opened`** — Opened the sharing settings dialog
- **`Web Session Opened on Desktop`** — Shared session viewed on the web was opened on the desktop
- **`Rewind Confirmation Dialog Opened`** — User opened the rewind confirmation dialog
- **`Conversation Rewind Executed`** — User executed a rewind to a previous conversation state
- **`Save As Workflow Modal Opened`** — Opened the modal to create a new workflow

## Command Search

- **`Command Search Opened from Input Editor`** — Opened command search via the Input Editor's context menu

## Warpify

- **`Warpify Footer Accepted`** — User clicked Warpify in the warpify footer
- **`Warpify Footer Displayed`** — Displayed the warpify footer for a detected subshell or SSH session

## Toggle Settings

- **`Toggle Active AI Enablement`** — Toggled active AI enablement
- **`Toggle Agent Mode Codebase Context`** — Toggled on/off the enablement of codebase context
- **`Toggle Agent Mode Query Suggestions Setting`** — Toggled on/off the prompt suggestions setting
- **`Toggle Block Filter Case Sensitivity`** — Toggled on/off case sensitivity within the block filter editor
- **`Toggle Block Filter Invert`** — Toggled on/off invert within the block filter editor
- **`Toggle Block Filter Query`** — Toggled on/off a block filter query
- **`Toggle Block Filter Regex`** — Toggled on/off regex within the block filter editor
- **`Toggle Code Suggestions Setting`** — Toggled on/off the code suggestions setting
- **`Toggle Codebase Context Autoindexing`** — Toggled on/off the enablement of autoindexing
- **`Toggle Dim Inactive Panes`** — Whether the dim inactive panes feature has been toggled
- **`Toggle Focus Pane On Hover`** — Toggled on/off focus pane on hover feature
- **`Toggle Git Operations Autogen Setting`** — Toggled on/off the git operations autogen setting
- **`Toggle Global AI Enablement`** — Toggled global AI enablement
- **`Toggle Intelligent Autosuggestions Setting`** — Toggled on/off the intelligent autosuggestions setting
- **`Toggle Jump to Bottom of Block Button`** — Enabled or disabled the Jump to Bottom of Block Button
- **`Toggle Ligature Rendering`** — Toggled ligature rendering
- **`Toggle New Windows at Custom Size`** — Whether the new windows at custom size feature has been toggled
- **`Toggle Preserve Active Tab Color`** — Enabled or disabled preserving the active tab color
- **`Toggle Session Restoration`** — Toggled session restoration
- **`Toggle SSH Tmux Wrapper Setting`** — Changed the setting for SSH sessions to prompt for Tmux Wrapper
- **`Toggle SSH Warpify Setting`** — Changed the setting for SSH sessions to be Warpified
- **`Toggle Same Line Prompt`** — Toggled on/off same line prompt
- **`Toggle Secret Redaction`** — Toggled on/off the setting for Secret Redaction
- **`Toggle SharedBlock Title Generation`** — Toggled on/off the shared block title generation setting
- **`Toggle Agent Tips`** — Toggled the Show Agent Tips setting in AI settings
- **`Toggle Show Block Dividers`** — Enabled or disabled the Show Block Dividers Button
- **`Toggle Sticky Command Header`** — Expanded or collapsed the sticky command header
- **`Toggle Sync Inputs Across All Panes in All Tabs`** — Enable the synchronization across all panes in all tabs
- **`Toggle Sync Inputs Across All Panes in Current Tab`** — Enable the synchronization across panes in current tab
- **`Toggle Tab Indicators`** — Enabled or disabled the tab indicators
- **`Toggle Voice Input Setting`** — Toggled on/off the voice input setting
- **`Toggled Tab Bar Visibility`** — Toggled when to display the tab bar
- **`Disable Input Sync Inputs`** — Disabled / turn off the Input Synchronization
- **`Input Sync Toggled`** — Enabled or disabled Input Synchronization
- **`Expanded Code Diff Suggestion`** — Expanded the passive code diff suggestion
- **`Alias Expansion Banner Dismissed`** — Dismissed the banner to enable automatic alias expansion
- **`Alias Expansion Enabled From Banner`** — Enabled automatic alias expansion from the banner
- **`Show Alias Expansion Banner`** — Displayed the banner asking about alias expansion
- **`Show Subshell Warpify Banner`** — Displayed the banner to Warpify the current session
- **`Show SSH Warpify Banner`** — Displayed the banner to Warpify the current SSH session
- **`Trigger Subshell Bootstrap`** — Attempted to Warpify the current session
- **`Vim Keybindings Banner Dismissed`** — Dismissed the banner to enable Vim keybindings
- **`Vim Keybindings Banner Displayed`** — Displayed the banner asking about Vim keybindings
- **`Vim Keybindings Enabled from Banner`** — Enabled Vim keybindings from the banner
- **`Update Block Filter Query`** — When a new filter is applied to a block
- **`Update Block Filter Query With Context Lines`** — When context lines for block filter is updated
- **`Update Tab Close Button Position`** — Updated the tab close button position
- **`Updated Alt Screen Padding Mode`** — Updated the custom padding setting for the alt-screen
- **`UseAgentToolbar.SettingToggled`** — User toggled the Use Agent footer setting
- **`Set Line Height`** — Set line height through Settings
- **`Set New Windows at Custom Size`** — Set new windows at custom size
- **`Set Blur Radius`** — Changed the blur radius from Settings
- **`Set Opacity`** — Changed the opacity from Settings
- **`Set SSH Extension Install Mode`** — Changed the SSH extension install mode

## Teams Modal

- **`Teams Modal Toggled`** — Opened or closed teams modal

## Free Tier & Revenue

- **`FreeTierLimitHitInterstitial.Closed`** — User closed the free tier limit hit interstitial
- **`FreeTierLimitHitInterstitial.Displayed`** — The free tier limit hit interstitial was displayed
- **`FreeTierLimitHitInterstitial.UpgradeButtonClicked`** — User clicked the 'Upgrade' button
- **`Shared Object Limit Hit Banner View Plans Button Clicked`** — Clicked the 'View Plans' button on the banner
- **`Tier Limit Hit`** — User hit the tier limit for a feature
- **`revenue.AutoReloadModalClosed`** — User closed the auto-reload modal
- **`revenue.AutoReloadToggledFromBillingSettings`** — User toggled auto-reload in Billing & Usage settings
- **`revenue.OutOfCreditsBannerClosed`** — User closed the 'Out of credits' banner

## Experiments & Performance

- **`experiments.client.enroll_client`** — Client assigned to A/B test
- **`perf_metrics.memory_usage_high`** — Total application memory usage exceeded a significant threshold
- **`perf_metrics.resource_usage`** — Periodic report on application resource usage statistics

## Repo Metadata

- **`RepoMetadata.BuildTree.Failed`** — Failed to build file tree for repo metadata

## Linear Integration

- **`Linear Deep Link Opened`** — User opened a warp://linear deeplink to work on an issue

## Alt Screen

- **`Alt Screen Find Bar Opened`** — Opened the Find bar in the Alt Screen

## Vertical Tabs

- **`VerticalTabs.DiffStatsChipClicked`** — User clicked a diff stats chip in the vertical tabs panel
- **`VerticalTabs.DisplayOptionChanged`** — User updated a display option in the vertical tabs settings
- **`VerticalTabs.PrChipClicked`** — User clicked a GitHub PR chip in the vertical tabs panel
