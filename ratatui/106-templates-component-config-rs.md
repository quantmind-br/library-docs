---
title: Config.rs
url: https://ratatui.rs/templates/component/config-rs/
source: crawler
fetched_at: 2026-02-01T21:13:25.459662525-03:00
rendered_js: false
word_count: 1125
summary: This document explains how to implement user-definable keybindings and styles in a Rust terminal application using external configuration files and Serde.
tags:
    - rust
    - ratatui
    - serde
    - configuration
    - key-bindings
    - tui-development
category: guide
---

At the moment, our keys are hard coded into the app.

```

impl Component for Home {
fnhandle_key_events(&mutself, key: KeyEvent) -> Action {
matchself.mode {
Mode::Normal | Mode::Processing => {
matchkey.code {
KeyCode::Char('q') => Action::Quit,
KeyCode::Char('d') ifkey.modifiers.contains(KeyModifiers::CONTROL) => Action::Quit,
KeyCode::Char('c') ifkey.modifiers.contains(KeyModifiers::CONTROL) => Action::Quit,
KeyCode::Char('z') ifkey.modifiers.contains(KeyModifiers::CONTROL) => Action::Suspend,
KeyCode::Char('?') => Action::ToggleShowHelp,
KeyCode::Char('j') => Action::ScheduleIncrement,
KeyCode::Char('k') => Action::ScheduleDecrement,
KeyCode::Char('/') => Action::EnterInsert,
_=> Action::Tick,
}
},
Mode::Insert => {
matchkey.code {
KeyCode::Esc => Action::EnterNormal,
KeyCode::Enter => Action::EnterNormal,
_=> {
self.input.handle_event(&crossterm::event::Event::Key(key));
Action::Update
},
}
},
}
}
```

If a user wants to press `Up` and `Down` arrow key to `ScheduleIncrement` and `ScheduleDecrement`, the only way for them to do it is having to make changes to the source code and recompile the app. It would be better to provide a way for users to set up a configuration file that maps key presses to actions.

For example, assume we want a user to be able to set up a keyevents-to-actions mapping in a `config.toml` file like below:

```

[keymap]
"q" = "Quit"
"j" = "ScheduleIncrement"
"k" = "ScheduleDecrement"
"l" = "ToggleShowHelp"
"/" = "EnterInsert"
"ESC" = "EnterNormal"
"Enter" = "EnterNormal"
"Ctrl-d" = "Quit"
"Ctrl-c" = "Quit"
"Ctrl-z" = "Suspend"
```

We can set up a `Config` struct using [the excellent `config` crate](https://docs.rs/config/0.13.3/config/):

```

use std::collections::HashMap;
use std::path::PathBuf;
use color_eyre::eyre::Result;
use ratatui::crossterm::event::KeyEvent;
use serde::Deserialize;
usecrate::action::Action;
#[derive(Clone, Debug, Deserialize, Default)]
pubstruct AppConfig {
#[serde(default)]
pubdata_dir: PathBuf,
#[serde(default)]
pubconfig_dir: PathBuf,
}
#[derive(Clone, Debug, Default, Deref, DerefMut)]
pubstruct KeyBindings(pub HashMap<Mode, HashMap<Vec<KeyEvent>, Action>>);
#[derive(Clone, Debug, Default, Deserialize)]
pubstruct Config {
#[serde(default, flatten)]
pubconfig: AppConfig,
#[serde(default)]
pubkeybindings: KeyBindings,
#[serde(default)]
pubstyles: Styles,
}
```

## Key Bindings and Styles

[Section titled “Key Bindings and Styles”](#key-bindings-and-styles)

We are using `serde` to deserialize from a TOML file.

Now the default `KeyEvent` serialized format is not very user friendly, so let’s implement our own version:

```

#[derive(Clone, Debug, Default, Deref, DerefMut)]
pubstruct KeyBindings(pub HashMap<Mode, HashMap<Vec<KeyEvent>, Action>>);
impl<'de> Deserialize<'de> for KeyBindings {
fndeserialize<D>(deserializer: D) -> Result<Self, D::Error>
where
D: Deserializer<'de>,
{
letparsed_map= HashMap::<Mode, HashMap<String, Action>>::deserialize(deserializer)?;
letkeybindings=parsed_map
.into_iter()
.map(|(mode, inner_map)| {
letconverted_inner_map=inner_map
.into_iter()
.map(|(key_str, cmd)| (parse_key_sequence(&key_str).unwrap(), cmd))
.collect();
(mode, converted_inner_map)
})
.collect();
Ok(KeyBindings(keybindings))
}
}
```

Now all we need to do is implement a `parse_key_event` function. [You can check the source code for an example of this implementation](https://github.com/ratatui/templates/blob/main/component/template/src/config.rs#L150-L154).

And in the `handle_key_events` we get the `Action` that should to be performed from the `HashMap` directly.

```

impl App {
fnhandle_key_events(&mutself, key: KeyEvent) -> Result<()> {
letaction_tx=self.action_tx.clone();
let Some(keymap) =self.config.keybindings.get(&self.mode) else {
return Ok(());
};
matchkeymap.get(&vec![key]) {
Some(action) => {
info!("Got action: {action:?}");
action_tx.send(action.clone())?;
}
_=> {
// If the key was not handled as a single key action,
// then consider it for multi-key combinations.
self.last_tick_key_events.push(key);
// Check for multi-key combinations
iflet Some(action) =keymap.get(&self.last_tick_key_events) {
info!("Got action: {action:?}");
action_tx.send(action.clone())?;
}
}
}
Ok(())
}
}
```

In the template, it is set up to handle `Vec<KeyEvent>` mapped to an `Action`. This allows you to map for example:

- `<g><j>` to `Action::GotoBottom`
- `<g><k>` to `Action::GotoTop`

Here’s the JSON configuration we use for the template:

```

{
"keybindings": {
"Home": {
"<q>": "Quit", // Quit the application
"<j>": "ScheduleIncrement",
"<k>": "ScheduleDecrement",
"<l>": "ToggleShowHelp",
"</>": "EnterInsert",
"<Ctrl-d>": "Quit", // Another way to quit
"<Ctrl-c>": "Quit", // Yet another way to quit
"<Ctrl-z>": "Suspend", // Suspend the application
},
},
}
```

Similarly, we have a `Styles` struct that parses custom styles from a config file.

```

#[derive(Clone, Debug, Default, Deref, DerefMut)]
pubstruct Styles(pub HashMap<Mode, HashMap<String, Style>>);
impl<'de> Deserialize<'de> for Styles {
fndeserialize<D>(deserializer: D) -> Result<Self, D::Error>
where
D: Deserializer<'de>,
{
letparsed_map= HashMap::<Mode, HashMap<String, String>>::deserialize(deserializer)?;
letstyles=parsed_map
.into_iter()
.map(|(mode, inner_map)| {
letconverted_inner_map=inner_map
.into_iter()
.map(|(str, style)| (str, parse_style(&style)))
.collect();
(mode, converted_inner_map)
})
.collect();
Ok(Styles(styles))
}
}
```

There are some helper functions in the `config.rs` file that you can use to parse the styles and keybinds.

The template has two main directories that are used for storing configuration files and data files.

Using the directories crate, we can get the XDG directories for the current user. This allows us to store the configuration and data files in a platform-agnostic way.

```

lazy_static! {
pubstaticrefPROJECT_NAME: String =env!("CARGO_CRATE_NAME").to_uppercase().to_string();
pubstaticrefDATA_FOLDER: Option<PathBuf> =
env::var(format!("{}_DATA", PROJECT_NAME.clone()))
.ok()
.map(PathBuf::from);
pubstaticrefCONFIG_FOLDER: Option<PathBuf> =
env::var(format!("{}_CONFIG", PROJECT_NAME.clone()))
.ok()
.map(PathBuf::from);
}
// -- snip --
pubfnget_data_dir() -> PathBuf {
letdirectory=iflet Some(s) =DATA_FOLDER.clone() {
s
} elseiflet Some(proj_dirs) =project_directory() {
proj_dirs.data_local_dir().to_path_buf()
} else {
PathBuf::from(".").join(".data")
};
directory
}
pubfnget_config_dir() -> PathBuf {
letdirectory=iflet Some(s) =CONFIG_FOLDER.clone() {
s
} elseiflet Some(proj_dirs) =project_directory() {
proj_dirs.config_local_dir().to_path_buf()
} else {
PathBuf::from(".").join(".config")
};
directory
}
fnproject_directory() -> Option<ProjectDirs> {
ProjectDirs::from("com", "kdheepak", env!("CARGO_PKG_NAME")) // Replace kdheepak with your name/project name.
}
```

```

use std::{collections::HashMap, env, path::PathBuf};
use color_eyre::Result;
use crossterm::event::{KeyCode, KeyEvent, KeyModifiers};
use derive_deref::{Deref, DerefMut};
use directories::ProjectDirs;
use lazy_static::lazy_static;
use ratatui::style::{Color, Modifier, Style};
use serde::{Deserialize, de::Deserializer};
use tracing::error;
usecrate::{action::Action, app::Mode};
constCONFIG:&str =include_str!("../.config/config.json5");
#[derive(Clone, Debug, Deserialize, Default)]
pubstruct AppConfig {
#[serde(default)]
pubdata_dir: PathBuf,
#[serde(default)]
pubconfig_dir: PathBuf,
}
#[derive(Clone, Debug, Default, Deserialize)]
pubstruct Config {
#[serde(default, flatten)]
pubconfig: AppConfig,
#[serde(default)]
pubkeybindings: KeyBindings,
#[serde(default)]
pubstyles: Styles,
}
lazy_static! {
pubstaticrefPROJECT_NAME: String =env!("CARGO_CRATE_NAME").to_uppercase().to_string();
pubstaticrefDATA_FOLDER: Option<PathBuf> =
env::var(format!("{}_DATA", PROJECT_NAME.clone()))
.ok()
.map(PathBuf::from);
pubstaticrefCONFIG_FOLDER: Option<PathBuf> =
env::var(format!("{}_CONFIG", PROJECT_NAME.clone()))
.ok()
.map(PathBuf::from);
}
impl Config {
pubfnnew() -> Result<Self, config::ConfigError> {
letdefault_config: Config = json5::from_str(CONFIG).unwrap();
letdata_dir=get_data_dir();
letconfig_dir=get_config_dir();
letmutbuilder= config::Config::builder()
.set_default("data_dir", data_dir.to_str().unwrap())?
.set_default("config_dir", config_dir.to_str().unwrap())?;
letconfig_files= [
("config.json5", config::FileFormat::Json5),
("config.json", config::FileFormat::Json),
("config.yaml", config::FileFormat::Yaml),
("config.toml", config::FileFormat::Toml),
("config.ini", config::FileFormat::Ini),
];
letmutfound_config=false;
for (file, format) in&config_files {
letsource= config::File::from(config_dir.join(file))
.format(*format)
.required(false);
builder=builder.add_source(source);
ifconfig_dir.join(file).exists() {
found_config=true
}
}
if!found_config {
error!("No configuration file found. Application may not behave as expected");
}
letmutcfg:Self=builder.build()?.try_deserialize()?;
for (mode, default_bindings) indefault_config.keybindings.iter() {
letuser_bindings=cfg.keybindings.entry(*mode).or_default();
for (key, cmd) indefault_bindings.iter() {
user_bindings
.entry(key.clone())
.or_insert_with(||cmd.clone());
}
}
for (mode, default_styles) indefault_config.styles.iter() {
letuser_styles=cfg.styles.entry(*mode).or_default();
for (style_key, style) indefault_styles.iter() {
user_styles.entry(style_key.clone()).or_insert(*style);
}
}
Ok(cfg)
}
}
pubfnget_data_dir() -> PathBuf {
letdirectory=iflet Some(s) =DATA_FOLDER.clone() {
s
} elseiflet Some(proj_dirs) =project_directory() {
proj_dirs.data_local_dir().to_path_buf()
} else {
PathBuf::from(".").join(".data")
};
directory
}
pubfnget_config_dir() -> PathBuf {
letdirectory=iflet Some(s) =CONFIG_FOLDER.clone() {
s
} elseiflet Some(proj_dirs) =project_directory() {
proj_dirs.config_local_dir().to_path_buf()
} else {
PathBuf::from(".").join(".config")
};
directory
}
fnproject_directory() -> Option<ProjectDirs> {
ProjectDirs::from("com", "kdheepak", env!("CARGO_PKG_NAME"))
}
#[derive(Clone, Debug, Default, Deref, DerefMut)]
pubstruct KeyBindings(pub HashMap<Mode, HashMap<Vec<KeyEvent>, Action>>);
impl<'de> Deserialize<'de> for KeyBindings {
fndeserialize<D>(deserializer: D) -> Result<Self, D::Error>
where
D: Deserializer<'de>,
{
letparsed_map= HashMap::<Mode, HashMap<String, Action>>::deserialize(deserializer)?;
letkeybindings=parsed_map
.into_iter()
.map(|(mode, inner_map)| {
letconverted_inner_map=inner_map
.into_iter()
.map(|(key_str, cmd)| (parse_key_sequence(&key_str).unwrap(), cmd))
.collect();
(mode, converted_inner_map)
})
.collect();
Ok(KeyBindings(keybindings))
}
}
fnparse_key_event(raw:&str) -> Result<KeyEvent, String> {
letraw_lower=raw.to_ascii_lowercase();
let (remaining, modifiers) =extract_modifiers(&raw_lower);
parse_key_code_with_modifiers(remaining, modifiers)
}
fnextract_modifiers(raw:&str) -> (&str, KeyModifiers) {
letmutmodifiers= KeyModifiers::empty();
letmutcurrent=raw;
loop {
matchcurrent {
restifrest.starts_with("ctrl-") => {
modifiers.insert(KeyModifiers::CONTROL);
current=&rest[5..];
}
restifrest.starts_with("alt-") => {
modifiers.insert(KeyModifiers::ALT);
current=&rest[4..];
}
restifrest.starts_with("shift-") => {
modifiers.insert(KeyModifiers::SHIFT);
current=&rest[6..];
}
_=>break, // break out of the loop if no known prefix is detected
};
}
(current, modifiers)
}
fnparse_key_code_with_modifiers(
raw:&str,
mutmodifiers: KeyModifiers,
) -> Result<KeyEvent, String> {
letc=matchraw {
"esc"=> KeyCode::Esc,
"enter"=> KeyCode::Enter,
"left"=> KeyCode::Left,
"right"=> KeyCode::Right,
"up"=> KeyCode::Up,
"down"=> KeyCode::Down,
"home"=> KeyCode::Home,
"end"=> KeyCode::End,
"pageup"=> KeyCode::PageUp,
"pagedown"=> KeyCode::PageDown,
"backtab"=> {
modifiers.insert(KeyModifiers::SHIFT);
KeyCode::BackTab
}
"backspace"=> KeyCode::Backspace,
"delete"=> KeyCode::Delete,
"insert"=> KeyCode::Insert,
"f1"=> KeyCode::F(1),
"f2"=> KeyCode::F(2),
"f3"=> KeyCode::F(3),
"f4"=> KeyCode::F(4),
"f5"=> KeyCode::F(5),
"f6"=> KeyCode::F(6),
"f7"=> KeyCode::F(7),
"f8"=> KeyCode::F(8),
"f9"=> KeyCode::F(9),
"f10"=> KeyCode::F(10),
"f11"=> KeyCode::F(11),
"f12"=> KeyCode::F(12),
"space"=> KeyCode::Char(' '),
"hyphen"=> KeyCode::Char('-'),
"minus"=> KeyCode::Char('-'),
"tab"=> KeyCode::Tab,
cifc.len() ==1=> {
letmutc=c.chars().next().unwrap();
ifmodifiers.contains(KeyModifiers::SHIFT) {
c=c.to_ascii_uppercase();
}
KeyCode::Char(c)
}
_=>return Err(format!("Unable to parse {raw}")),
};
Ok(KeyEvent::new(c, modifiers))
}
pubfnkey_event_to_string(key_event:&KeyEvent) -> String {
let char;
letkey_code=matchkey_event.code {
KeyCode::Backspace =>"backspace",
KeyCode::Enter =>"enter",
KeyCode::Left =>"left",
KeyCode::Right =>"right",
KeyCode::Up =>"up",
KeyCode::Down =>"down",
KeyCode::Home =>"home",
KeyCode::End =>"end",
KeyCode::PageUp =>"pageup",
KeyCode::PageDown =>"pagedown",
KeyCode::Tab =>"tab",
KeyCode::BackTab =>"backtab",
KeyCode::Delete =>"delete",
KeyCode::Insert =>"insert",
KeyCode::F(c) => {
char =format!("f({c})");
&char
}
KeyCode::Char(' ') =>"space",
KeyCode::Char(c) => {
char =c.to_string();
&char
}
KeyCode::Esc =>"esc",
KeyCode::Null =>"",
KeyCode::CapsLock =>"",
KeyCode::Menu =>"",
KeyCode::ScrollLock =>"",
KeyCode::Media(_) =>"",
KeyCode::NumLock =>"",
KeyCode::PrintScreen =>"",
KeyCode::Pause =>"",
KeyCode::KeypadBegin =>"",
KeyCode::Modifier(_) =>"",
};
letmutmodifiers= Vec::with_capacity(3);
ifkey_event.modifiers.intersects(KeyModifiers::CONTROL) {
modifiers.push("ctrl");
}
ifkey_event.modifiers.intersects(KeyModifiers::SHIFT) {
modifiers.push("shift");
}
ifkey_event.modifiers.intersects(KeyModifiers::ALT) {
modifiers.push("alt");
}
letmutkey=modifiers.join("-");
if!key.is_empty() {
key.push('-');
}
key.push_str(key_code);
key
}
pubfnparse_key_sequence(raw:&str) -> Result<Vec<KeyEvent>, String> {
ifraw.chars().filter(|c|*c=='>').count() !=raw.chars().filter(|c|*c=='<').count() {
return Err(format!("Unable to parse `{}`", raw));
}
letraw=if!raw.contains("><") {
letraw=raw.strip_prefix('<').unwrap_or(raw);
letraw=raw.strip_prefix('>').unwrap_or(raw);
raw
} else {
raw
};
letsequences=raw
.split("><")
.map(|seq| {
iflet Some(s) =seq.strip_prefix('<') {
s
} elseiflet Some(s) =seq.strip_suffix('>') {
s
} else {
seq
}
})
.collect::<Vec<_>>();
sequences.into_iter().map(parse_key_event).collect()
}
#[derive(Clone, Debug, Default, Deref, DerefMut)]
pubstruct Styles(pub HashMap<Mode, HashMap<String, Style>>);
impl<'de> Deserialize<'de> for Styles {
fndeserialize<D>(deserializer: D) -> Result<Self, D::Error>
where
D: Deserializer<'de>,
{
letparsed_map= HashMap::<Mode, HashMap<String, String>>::deserialize(deserializer)?;
letstyles=parsed_map
.into_iter()
.map(|(mode, inner_map)| {
letconverted_inner_map=inner_map
.into_iter()
.map(|(str, style)| (str, parse_style(&style)))
.collect();
(mode, converted_inner_map)
})
.collect();
Ok(Styles(styles))
}
}
pubfnparse_style(line:&str) -> Style {
let (foreground, background) =
line.split_at(line.to_lowercase().find("on ").unwrap_or(line.len()));
letforeground=process_color_string(foreground);
letbackground=process_color_string(&background.replace("on ", ""));
letmutstyle= Style::default();
iflet Some(fg) =parse_color(&foreground.0) {
style=style.fg(fg);
}
iflet Some(bg) =parse_color(&background.0) {
style=style.bg(bg);
}
style=style.add_modifier(foreground.1|background.1);
style
}
fnprocess_color_string(color_str:&str) -> (String, Modifier) {
letcolor=color_str
.replace("grey", "gray")
.replace("bright ", "")
.replace("bold ", "")
.replace("underline ", "")
.replace("inverse ", "");
letmutmodifiers= Modifier::empty();
ifcolor_str.contains("underline") {
modifiers|= Modifier::UNDERLINED;
}
ifcolor_str.contains("bold") {
modifiers|= Modifier::BOLD;
}
ifcolor_str.contains("inverse") {
modifiers|= Modifier::REVERSED;
}
(color, modifiers)
}
fnparse_color(s:&str) -> Option<Color> {
lets=s.trim_start();
lets=s.trim_end();
ifs.contains("bright color") {
lets=s.trim_start_matches("bright ");
letc=s
.trim_start_matches("color")
.parse::<u8>()
.unwrap_or_default();
Some(Color::Indexed(c.wrapping_shl(8)))
} elseifs.contains("color") {
letc=s
.trim_start_matches("color")
.parse::<u8>()
.unwrap_or_default();
Some(Color::Indexed(c))
} elseifs.contains("gray") {
letc=232
+s.trim_start_matches("gray")
.parse::<u8>()
.unwrap_or_default();
Some(Color::Indexed(c))
} elseifs.contains("rgb") {
letred= (s.as_bytes()[3] as char).to_digit(10).unwrap_or_default() as u8;
letgreen= (s.as_bytes()[4] as char).to_digit(10).unwrap_or_default() as u8;
letblue= (s.as_bytes()[5] as char).to_digit(10).unwrap_or_default() as u8;
letc=16+red*36+green*6+blue;
Some(Color::Indexed(c))
} elseifs=="bold black" {
Some(Color::Indexed(8))
} elseifs=="bold red" {
Some(Color::Indexed(9))
} elseifs=="bold green" {
Some(Color::Indexed(10))
} elseifs=="bold yellow" {
Some(Color::Indexed(11))
} elseifs=="bold blue" {
Some(Color::Indexed(12))
} elseifs=="bold magenta" {
Some(Color::Indexed(13))
} elseifs=="bold cyan" {
Some(Color::Indexed(14))
} elseifs=="bold white" {
Some(Color::Indexed(15))
} elseifs=="black" {
Some(Color::Indexed(0))
} elseifs=="red" {
Some(Color::Indexed(1))
} elseifs=="green" {
Some(Color::Indexed(2))
} elseifs=="yellow" {
Some(Color::Indexed(3))
} elseifs=="blue" {
Some(Color::Indexed(4))
} elseifs=="magenta" {
Some(Color::Indexed(5))
} elseifs=="cyan" {
Some(Color::Indexed(6))
} elseifs=="white" {
Some(Color::Indexed(7))
} else {
None
}
}
```