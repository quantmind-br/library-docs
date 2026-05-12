---
title: Uncommon tips & tricks
url: https://wiki.hypr.land/Configuring/Uncommon-tips--tricks/
source: sitemap
fetched_at: 2026-04-26T09:49:28.546800456-03:00
rendered_js: false
word_count: 785
summary: This document provides a collection of common configuration patterns, scripts, and customization techniques for the Hyprland compositor.
tags:
    - hyprland
    - configuration
    - keyboard-layout
    - keybinds
    - scripts
    - xkb
    - desktop-customization
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Switchable keyboard layouts

Set layouts via XKB:

```ini
input {
    kb_layout = us,cz
    kb_variant = ,qwerty
    kb_options = grp:alt_shift_toggle
}
```

Variants are set per layout.

> [!warning]
> The first layout defined in the input section is used for binds by default. For `us,ua` → binds use `SUPER, A`, while `ua,us` → `SUPER, Cyrillic_ef`.

Change behavior globally/per-device with `resolve_binds_by_sym = 1`. Binds activate when the typed symbol matches the bind symbol. For `us,fr` with `SUPER, A`, press the first letter on the second row while `us` is active, first row while `fr` is active.

Bind a key to `hyprctl switchxkblayout` for more freedom. See [[066-configuring-using-hyprctl|Using hyprctl]].

Find valid layouts and `kb_options` in `/usr/share/X11/xkb/rules/base.lst`:

```sh
grep -i 'persian' /usr/share/X11/xkb/rules/base.lst
grep 'grp:.*toggle' /usr/share/X11/xkb/rules/base.lst
```

## Disabling keybinds with one master keybind

Use a submap with only a keybind to exit it:

```ini
bind = MOD, KEY, submap, clean
submap = clean
bind = MOD, KEY, submap, reset
submap = reset
```

## Remapping Caps Lock

Customize Caps Lock behavior with `kb_options`. View available options:

```sh
grep 'caps' /usr/share/X11/xkb/rules/base.lst
```

Remap Caps Lock to Ctrl:

```ini
input {
    kb_options = ctrl:nocaps
}
```

Swap Caps Lock and Escape:

```ini
input {
    kb_options = caps:swapescape
}
```

Additional `kb_options` are in `/usr/share/X11/xkb/rules/base.lst`.

## F13-F24 as usual function keys

By default, F13-F24 are mapped by xkb as XF86 keysyms, causing binding issues in programs like OBS Studio. This option maps them back to expected F13-F24 values.

> [!warning]
> Requires `xkeyboard-config` version 2.43 or greater.

```ini
input {
    kb_options = fkeys:basic_13-24
}
```

## Minimize windows using special workspaces

Uses special workspaces to mimic minimize, handling one window at a time:

```sh
#!/usr/bin/env bash
if [[ -z $(hyprctl workspaces | grep special:magic) ]]; then
    hyprctl dispatch movetoworkspacesilent special:magic
else
    hyprctl --batch 'dispatch togglespecialworkspace magic;dispatch movetoworkspace +0'
fi
```

Bind it:

```ini
bind = $mainMod, S, exec, <PATH_TO_SCRIPT>
```

## Show desktop

Same principle as minimize. Moves all windows from current workspace to `special:desktop`. State is remembered per workspace.

```sh
#!/bin/env sh
TMP_FILE="$XDG_RUNTIME_DIR/hyprland-show-desktop"
CURRENT_WORKSPACE=$(hyprctl monitors -j | jq '.[] | .activeWorkspace | .name' | sed 's/"//g')
if [ -s "$TMP_FILE-$CURRENT_WORKSPACE" ]; then
  readarray -d $'\n' -t ADDRESS_ARRAY <<< $(< "$TMP_FILE-$CURRENT_WORKSPACE")
  for address in "${ADDRESS_ARRAY[@]}"
  do
    CMDS+="dispatch movetoworkspacesilent name:$CURRENT_WORKSPACE,address:$address;"
  done
  hyprctl --batch "$CMDS"
  rm "$TMP_FILE-$CURRENT_WORKSPACE"
else
  HIDDEN_WINDOWS=$(hyprctl clients -j | jq --arg CW "$CURRENT_WORKSPACE" '.[] | select (.workspace .name == $CW) | .address')
  readarray -d $'\n' -t ADDRESS_ARRAY <<< $HIDDEN_WINDOWS
  for address in "${ADDRESS_ARRAY[@]}"
  do
    address=$(sed 's/"//g' <<< $address )
    if [[ -n address ]]; then
      TMP_ADDRESS+="$address\n"
    fi
    CMDS+="dispatch movetoworkspacesilent special:desktop,address:$address;"
  done
  hyprctl --batch "$CMDS"
  echo -e "$TMP_ADDRESS" | sed -e '/^$/d' > "$TMP_FILE-$CURRENT_WORKSPACE"
fi
```

```ini
bind = $mainMod , D, exec, <PATH TO SCRIPT>
```

## Minimize Steam instead of killing

Steam exits entirely when its last window is closed with `killactive`. Minimize to tray instead:

```sh
if [ "$(hyprctl activewindow -j | jq -r ".class")" = "Steam" ]; then
    xdotool getactivewindow windowunmap
else
    hyprctl dispatch killactive ""
fi
```

## Shimeji

For Shimeji programs like [this](https://codeberg.org/thatonecalculator/spamton-linux-shimeji):

```ini
windowrule {
    name = shimeji
    match:class = com-group_finity-mascot-Main
    float = true
    no_blur = true
    no_focus = true
    no_shadow = true
    border_size = 0
}
```

> [!note]
> The app indicator probably won't show. Use `killall -9 java` to kill them.

## Toggle animations/blur/etc hotkey

For performance in games or fewer distractions:

1. Create `~/.config/hypr/gamemode.sh`:

```bash
#!/usr/bin/env sh
HYPRGAMEMODE=$(hyprctl getoption animations:enabled | awk 'NR==1{print $2}')
if [ "$HYPRGAMEMODE" = 1 ] ; then
    hyprctl --batch "\
        keyword animations:enabled 0;\
        keyword animation borderangle,0; \
        keyword decoration:shadow:enabled 0;\
        keyword decoration:blur:enabled 0;\
	    keyword decoration:fullscreen_opacity 1;\
        keyword general:gaps_in 0;\
        keyword general:gaps_out 0;\
        keyword general:border_size 1;\
        keyword decoration:rounding 0"
    hyprctl notify 1 5000 "rgb(40a02b)" "Gamemode [ON]"
    exit
else
    hyprctl notify 1 5000 "rgb(d20f39)" "Gamemode [OFF]"
    hyprctl reload
    exit 0
fi
exit 1
```

2. Add to `hyprland.conf`:

```ini
bind = WIN, F1, exec, ~/.config/hypr/gamemode.sh
```

## Zoom

Use Hyprland's built-in zoom utility.

> [!warning]
> If mouse wheel bindings work only for the first time, reduce reset time with `binds:scroll_event_delay`.

```ini
bind = $mod, mouse_down, exec, hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor -j | jq '.float * 1.1')
bind = $mod, mouse_up, exec, hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor -j | jq '(.float * 0.9) | if . < 1 then 1 else . end')
binde = $mod, equal, exec, hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor -j | jq '.float * 1.1')
binde = $mod, minus, exec, hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor -j | jq '(.float * 0.9) | if . < 1 then 1 else . end')
binde = $mod, KP_ADD, exec, hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor -j | jq '.float * 1.1')
binde = $mod, KP_SUBTRACT, exec, hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor -j | jq '(.float * 0.9) | if . < 1 then 1 else . end')
bind = $mod SHIFT, mouse_up, exec, hyprctl -q keyword cursor:zoom_factor 1
bind = $mod SHIFT, mouse_down, exec, hyprctl -q keyword cursor:zoom_factor 1
bind = $mod SHIFT, minus, exec, hyprctl -q keyword cursor:zoom_factor 1
bind = $mod SHIFT, KP_SUBTRACT, exec, hyprctl -q keyword cursor:zoom_factor 1
bind = $mod SHIFT, 0, exec, hyprctl -q keyword cursor:zoom_factor 1
```

## Alt tab behaviour

Mimics DE alt-tab behavior using foot, fzf, grim, and chafa.

![alttab](https://github.com/user-attachments/assets/2a260809-b1b0-4f72-8644-46cc9d8b8971)

Dependencies: foot, fzf, grim, chafa, jq

1. Add to config:

```ini
exec-once = foot --server -c $XDG_CONFIG_HOME/foot/foot.ini
bind = ALT, TAB, exec, $HOME/.config/hypr/scripts/alttab/enable.sh 'down'
bind = ALT SHIFT, TAB, exec, $HOME/.config/hypr/scripts/alttab/enable.sh 'up'
submap=alttab
bind = ALT, tab, sendshortcut, , tab, class:alttab
bind = ALT SHIFT, tab, sendshortcut, shift, tab, class:alttab
bindrt = ALT, ALT_L, exec, $XDG_CONFIG_HOME/hypr/scripts/alttab/disable.sh ; hyprctl -q dispatch sendshortcut , return,class:alttab
bindrt = ALT SHIFT, ALT_L, exec, $XDG_CONFIG_HOME/hypr/scripts/alttab/disable.sh ; hyprctl -q dispatch sendshortcut , return,class:alttab
bind = ALT, Return, exec, $XDG_CONFIG_HOME/hypr/scripts/alttab/disable.sh ; hyprctl -q dispatch sendshortcut , return, class:alttab
bind = ALT SHIFT, Return, exec, $XDG_CONFIG_HOME/hypr/scripts/alttab/disable.sh ; hyprctl -q dispatch sendshortcut , return, class:alttab
bind = ALT, escape, exec, $XDG_CONFIG_HOME/hypr/scripts/alttab/disable.sh ; hyprctl -q dispatch sendshortcut , escape,class:alttab
bind = ALT SHIFT, escape, exec, $XDG_CONFIG_HOME/hypr/scripts/alttab/disable.sh ; hyprctl -q dispatch sendshortcut , escape,class:alttab
submap = reset
workspace = special:alttab, gapsout:0, gapsin:0, bordersize:0
windowrule = match:class alttab, no_anim
windowrule = match:class alttab, stay_focused
windowrule = match:class alttab, workspace special:alttab
windowrule = match:class alttab, border_size 0
```

2. Create `$XDG_CONFIG_HOME/hypr/scripts/alttab/alttab.sh`:

```bash
#!/usr/bin/env bash
hyprctl -q dispatch submap alttab
address=$(hyprctl -j clients | jq -r 'sort_by(.focusHistoryID) | .[] | select(.workspace.id >= 0) | "\(.stableId)\t\(.title)\t\(.address)"' |
	      fzf --color prompt:green,pointer:green,current-bg:-1,current-fg:green,gutter:-1,border:bright-black,current-hl:red,hl:red \
		  --cycle \
		  --sync \
		  --bind tab:down,shift-tab:up,start:"$1",double-click:ignore \
		  --wrap \
		  --delimiter=$'\t' \
		  --with-nth=2 \
		  --preview "$XDG_CONFIG_HOME/hypr/scripts/alttab/preview.sh {}" \
		  --preview-window=down:80% \
		  --layout=reverse |
	      awk -F"\t" '{print $3}')
if [ -n "$address" ] ; then
	echo "$address" > $XDG_RUNTIME_DIR/hypr/alttab/address
fi
hyprctl -q dispatch submap reset
```

Excludes windows in special workspaces. Remove `select(.workspace.id >= 0)` to include them.

3. Create `$XDG_CONFIG_HOME/hypr/scripts/alttab/preview.sh`:

```bash
#!/usr/bin/env bash
line="$1"
IFS=$'\t' read -r stableId _ <<< "$line"
dim=${FZF_PREVIEW_COLUMNS}x${FZF_PREVIEW_LINES}
grim -t png -l 0 -T "$stableId" $XDG_RUNTIME_DIR/hypr/alttab/preview.png
chafa --animate false --dither=none -s "$dim" $XDG_RUNTIME_DIR/hypr/alttab/preview.png
```

4. Create `$XDG_CONFIG_HOME/hypr/scripts/alttab/disable.sh`:

```bash
#!/usr/bin/env bash
hyprctl -q keyword animations:enabled true
hyprctl -q --batch "keyword unbind ALT, TAB ; keyword unbind ALT SHIFT, TAB ; keyword bind ALT, TAB, exec, $HOME/.config/hypr/scripts/alttab/enable.sh 'down' ; keyword bind ALT SHIFT, TAB, exec, $HOME/.config/hypr/scripts/alttab/enable.sh 'up'"
```

5. Create `$XDG_CONFIG_HOME/hypr/scripts/alttab/enable.sh`:

```bash
#!/usr/bin/env bash
mkdir -p $XDG_RUNTIME_DIR/hypr/alttab
hyprctl -q --batch "keyword animations:enabled false; keyword unbind ALT, TAB ; keyword unbind ALT SHIFT, TAB"
footclient -a alttab $HOME/.config/hypr/scripts/alttab/alttab.sh $1
hyprctl --batch -q "dispatch focuswindow address:$(cat $XDG_RUNTIME_DIR/hypr/alttab/address) ; dispatch alterzorder top"
```

## Config versioning

Since Hyprland 0.53, a variable is exported for each major version:

```hyprlang
# hyprlang if HYPRLAND_V_0_53

someValue = 0.53

# hyprlang endif

# hyprlang if !HYPRLAND_V_0_53

someValue = 0.52

# hyprlang endif
```

The `-git` branch exports the variable for the next major release. All future releases export all past variables (e.g. 0.54 exports 0.53).

## Per-workspace layouts

Use workspace rules:

```ini
workspace = 2, layout:scrolling
```
