---
title: Tips And Tricks
url: https://github.com/asmvik/yabai/wiki/Tips-and-tricks
source: wiki
fetched_at: 2026-02-11T07:33:54.886483-03:00
rendered_js: false
word_count: 1027
summary: A collection of practical tips, scripts, and troubleshooting steps for optimizing the yabai tiling window manager on macOS. It explains how to handle configuration management, automate updates, and refine window behavior.
tags:
    - yabai
    - macos
    - window-management
    - shell-scripts
    - configuration-management
    - automation
category: guide
---

### Quickly restart the yabai launch agent

When running as a service, the following command can be used:

```sh
yabai --restart-service

# e.g. bind to key in skhd:
# ctrl + alt + cmd - r : yabai --restart-service"
```

### Split yabai configuration across multiple files

The below script loads all executable files (`chmod +x`) in `~/.config/yabai/` and executes them. Why? Because then parts of your config can be reloaded individually from signals or external triggers.

```sh
# find all executable files in ~/.config/yabai and execute them
find "${HOME}/.config/yabai" -type f -perm +111 -exec {} \;
```

### Fix folders opened from desktop not tiling

When opening a folder on the desktop there's an animation that conflicts with yabai trying to tile the window. This animation can be disabled:

```sh
defaults write com.apple.finder DisableAllAnimations -bool true
killall Finder # or logout and login

# to reset system defaults, delete the key instead
# defaults delete com.apple.finder DisableAllAnimations
```

### Fix spaces reordering automatically

In System Preferences, navigate to Mission Control and uncheck the option "Automatically rearrange Spaces based on most recent use". 


### Auto updating from HEAD via brew

The below snippet makes yabai check for updates whenever it starts and automatically installs them for you, only requiring you to enter your password (or use Touch ID) if you want to update the scripting addition as well. Just put it at the end of your yabai configuration file and forget about it.

Note that this is only works for installations from HEAD (`brew install yabai --HEAD`).

<details>
<summary>Click to expand snippet</summary>

#### Method 1

This downloads an up-to-date version of the yabai autoupdate script hosted by [@dominiklohmann](https://github.com/dominiklohmann) and executes it whenever yabai starts.

```sh
YABAI_CERT=yabai-cert sh -c "$(curl -fsSL "https://git.io/update-yabai")" &
```

#### Method 2

This does the same as above, except the update snippet doesn't update itself. Check back for changes. Last update: 2019-07-12.

```sh
# set codesigning certificate name here (default: yabai-cert)
YABAI_CERT=

function main() {
    if check_for_updates; then
        install_updates ${YABAI_CERT}
    fi
}

# WARNING
# -------
# Please do not touch the code below unless you absolutely know what you are
# doing. It's the result of multiple long evenings trying to get this to work
# and relies on terrible hacks to work around limitations of launchd.
# For questions please reach out to @dominiklohmann via GitHub.

LOCKFILE="${TMPDIR}/yabai_update.lock"
if [ -e "${LOCKFILE}" ] && kill -0 $(cat "${LOCKFILE}"); then
	echo "Update already in progress"
	exit
fi

trap "rm -f ${LOCKFILE}; exit" INT TERM EXIT
echo "$$" > ${LOCKFILE}

function check_for_updates() {
	set -o pipefail

	# avoid GitHub rate limitations when jq is installed by using the GitHub 
	# API instead of ls-remote
	if command -v jq > /dev/null 2>&1; then
		installed="$(brew info --json /yabai \
			| jq -r '.[0].installed[0].version')"
		remote="$(curl -fsSL "https://api.github.com/repos/asmvik/yabai/commits" \
			| jq -r '"HEAD-" + (.[0].sha | explode | .[0:7] | implode)')"
	else
		installed="$(brew info /yabai | grep 'HEAD-' \
			| awk '{print substr($1,length($1)-6)}')"
		remote="$(git ls-remote 'https://github.com/asmvik/yabai.git' HEAD \
			| awk '{print substr($1,1,7)}')"
	fi

	[ ${?} -eq 0 ] && [ "${installed}" != "${remote}" ](./-"${installed}"-!=-"${remote}"-.md)
}

function install_updates() {

	echo "[yabai-update] reinstalling yabai"
	brew reinstall yabai > /dev/null 2>&1
	
	echo "[yabai-update] codesigning yabai"
	codesign -fs "${1:-yabai-sign}" "$(brew --prefix yabai)/bin/yabai" > /dev/null

	echo "[yabai-update] checking installed scripting addition"
	if yabai --check-sa; then
		osascript > /dev/null <<- EOM
			display dialog "A new version of yabai was just installed and yabai will restart shortly." with title "$(yabai --version)" buttons {"Okay"} default button 1
		EOM
	else
		echo "[yabai-update] prompting to reinstall scripting addition"
		script="$(mktemp)"
		cat > ${script} <<- EOF
			#! /usr/bin/env sh
			sudo yabai --uninstall-sa
			sudo yabai --install-sa
			pkill -x Dock
		EOF
		chmod +x "${script}"
		osascript > /dev/null <<- EOM
			display dialog "A new version of yabai was just installed and yabai will restart shortly.\n\nDo you want to reinstall the scripting addition (osascript will prompt for elevated privileges)?" with title "$(yabai --version)" buttons {"Install", "Cancel"} default button 2
			if button returned of result = "Install" then
				do shell script "${script}" with administrator privileges
			end if
		EOM
		rm -f "${script}"
	fi
	
	echo "[yabai-update] restarting yabai"
	yabai --restart-service
}

(main && rm -f "${LOCKFILE}") &
```

</details>

### Tiling Emacs

Emacs is not a well-behaved citizen of macOS. Try using [&rightarrow;&nbsp;emacs-mac](https://bitbucket.org/mituharu/emacs-mac) from the Homebrew tap [&rightarrow;&nbsp;emacsmacport](https://github.com/railwaycat/homebrew-emacsmacport).

If Emacs is still not recognized by yabai, try enabling menu-bar-mode.

```emacs-lisp
(menu-bar-mode t)
```

### Flash highlight to identify focused window 

The following command can be bound to a hotkey to identify the focused window on demand.
```
yabai -m window --opacity 0.1 && sleep $(yabai -m config window_opacity_duration) && yabai -m window --opacity 0.0
```

The following signal can be added to your yabai config to automatically flash the focused window when focus changes.
```
yabai -m signal --add label="flash_focus" event="window_focused" action="yabai -m window \$YABAI_WINDOW_ID --opacity 0.1 && sleep $(yabai -m config window_opacity_duration) && yabai -m window \$YABAI_WINDOW_ID --opacity 0.0"
```

### Constrain space focus to current display with optional cycling

Focus next space of current display. No-op if the current space is the last space of its display.

space_focus_next.sh
```
if [[ $(yabai -m query --spaces --display | jq '.[-1]."has-focus"') == "false" ]]; then yabai -m space --focus next; fi
```

Focus previous space of current display. No-op if the current space is the first space of its display.

space_focus_prev.sh
```
if [[ $(yabai -m query --spaces --display | jq '.[0]."has-focus"') == "false" ]]; then yabai -m space --focus prev; fi
```

Focus next space of current display. Wrap to the first space of the current display if the current space is the last space of its display.

space_cycle_next.sh
```
info=$(yabai -m query --spaces --display)
last=$(echo $info | jq '.[-1]."has-focus"')

if [ $last == "false" ](./-$last-==-"false"-.md); then
    yabai -m space --focus next
else
    yabai -m space --focus $(echo $info | jq '.[0].index')
fi
```

Focus previous space of current display. Wrap to the last space of the current display if the current space is the first space of its display.

space_cycle_prev.sh
```
info=$(yabai -m query --spaces --display)
first=$(echo $info | jq '.[0]."has-focus"')

if [ $first == "false" ](./-$first-==-"false"-.md); then
    yabai -m space --focus prev
else
    yabai -m space --focus $(echo $info | jq '.[-1].index')
fi
```