---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/vscode
source: crawler
fetched_at: 2026-02-23T05:18:09.413014-03:00
rendered_js: false
word_count: 532
---

Option Type Default Description `label` string `'<span>\udb82\ude1e</span>'` The format string for the widget. `label_alt` string `'<span>\udb82\ude1e</span> recents'` The alternative format string for the widget. `menu_title` string `<span style='font-weight:bold'>VScode</span> recents` The title of the menu. `folder_icon` string `'\uf114'` The icon for the folders to display in the menu. `file_icon` string `'\uf016'` The icon for the files to display in the menu. `hide_folder_icon` bool `false` Whether to hide the folder icon in the menu. `hide_file_icon` bool `false` Whether to hide the file icon in the menu. `truncate_to_root_dir` bool `false` Whether to truncate the path to the projects root directory. `max_number_of_folders` int `30` The maximum number of folders to display in the menu. `max_number_of_files` int `30` The maximum number of files to display in the menu. `max_field_size` int `100` The maximum number of characters in the title before truncation. `state_storage_path` string `''` Absolute path to the folder containing editor data, examples are shown below. `modified_date_format` string `'Date modified: %Y-%m-%d %H:%M'` The format for the modified date of the files and folders. `cli_command` string `'code'` The CLI command to execute when a workspace is clicked, doesn't need to contain folder name. For example, `code`, `windsurf`. `menu` dict `{'blur': True, 'round_corners': True, 'round_corners_type': 'normal', 'border_color': 'System', 'alignment': 'right', 'direction': 'down', 'offset_top': 6, 'offset_left': 0}` Menu settings for the widget. `callbacks` dict `{'on_left': 'toggle_menu', 'on_middle': 'do_nothing', 'on_right': 'toggle_label'}` Callbacks for mouse events on the widget. `animation` dict `{'enabled': True, 'type': 'fadeInOut', 'duration': 200}` Animation settings for the widget. `container_shadow` dict `None` Container shadow options. `label_shadow` dict `None` Label shadow options.

## Example Configuration

```
vscode:
type:"yasb.vscode.VSCodeWidget"
options:
label:"<span>\udb82\ude1e</span>"
label_alt:"<span>\udb82\ude1e</span>recents"
menu_title:"<spanstyle='font-weight:bold'>VScode</span>recents"
max_field_size:50
folder_icon:"\uf114"
file_icon:"\uf016"
truncate_to_root_dir:false
hide_folder_icon:false
hide_file_icon:false
max_number_of_folders:30
max_number_of_files:30# set to 0 if you only want folders
modified_date_format:"Datemodified:%Y-%m-%d%H:%M"
cli_command:"code"# or "codium" or "windsurf" or any other CLI command to open the workspace
menu:
blur:true
round_corners:true
round_corners_type:"small"
alignment:'center'
offset_top:0
```

## Description of Options

- **label:** The format string for the widget.
- **label\_alt:** The alternative format string for the widget.
- **menu\_title:** The title of the menu.
- **folder\_icon:** The icon for the folders to display in the menu.
- **file\_icon:** The icon for the files to display in the menu.
- **hide\_folder\_icon:** Whether to hide the folder icon in the menu.
- **truncate\_to\_root:** Whether to truncate the path to the projects root directory. Example `C:\Users\user\Documents\Projects\ProjectName` will be truncated to `ProjectName`.
- **max\_number\_of\_folders:** The maximum number of folders to display in the menu.
- **max\_number\_of\_files:** The maximum number of files to display in the menu (set to 0 if you only want folders).
- **max\_field\_size:** The maximum number of characters in the title before truncation.
- **state\_storage\_path:** Absolute path to the folder containing editor data. For example, `C:\Users\user\AppData\Roaming\Code\User\globalStorage\state.vscdb` for Visual Studio Code, `C:\Users\user\AppData\Roaming\Windsurf\User\globalStorage\state.vscdb` for Windsurf, etc. If left empty, it will use the default VSCode path.
- **modified\_date\_format:** The date format for the modified date of the files and folders. It uses Python's `strftime` format. For example, '%Y-%m-%d %H:%M' for `2025-06-01 12:00`.
- **cli\_command:** The cli command to execute when a workspace is clicked, doesn't need to contain folder name. For example, `code`, `windsurf`.
- **callbacks:** A dictionary specifying the callbacks for mouse events. The keys are `on_left`, `on_middle`, and `on_right`, and the values are the names of the callback functions.
- **callback functions**:
  
  - `toggle_menu`: Toggles the menu of the widget.
  - `toggle_label`: Toggles the label of the widget.
- **animation:** A dictionary specifying the animation settings for the widget. It contains three keys: `enabled`, `type`, and `duration`. The `type` can be `fadeInOut` and the `duration` is the animation duration in milliseconds.
- **container\_shadow:** Container shadow options.
- **label\_shadow:** Label shadow options.

```
.vscode-widget{}
.vscode-widget.widget-container{}
.vscode-widget.widget-container.label{}
.vscode-widget.widget-container.icon{}
/* Popup menu*/
.vscode-menu{}
.vscode-menu.header{}
.vscode-menu.contents{}
.vscode-menu.contents.item{}
.vscode-menu.contents.item.title{}
.vscode-menu.contents.item.modified-date{}
.vscode-menu.contents.item.folder-icon{}
.vscode-menu.contents.item.file-icon{}
.vscode-menu.no-recent{}
```

```
.vscode-widget.widget-container.icon{
color:#89b4fa;
}

.vscode-menu{
max-height:500px;
min-width:300px;
}

.vscode-menu.header{
border-bottom:1pxsolidrgba(255,255,255,0.1);
font-size:15px;
font-weight:400;
padding:8px;
color:#cdd6f4;
background-color:rgba(17,17,27,0.4);
}

.vscode-menu.contents{
background-color:rgba(17,17,27,0.4);
}

.vscode-menu.contents.item{
min-height:30px;
border-bottom:1pxsolidrgba(255,255,255,0.075);
}

.vscode-menu.contents.item.title{
font-size:12px;
margin-right:5px;
}

.vscode-menu.contents.item.modified-date{
font-size:11px;
margin-right:5px;
color:#797e91;
}

.vscode-menu.contents.item.folder-icon{
font-size:16px;
margin-left:8px;
color:#f2cdcd;
}

.vscode-menu.contents.item.file-icon{
font-size:16px;
margin-left:8px;
color:#cba6f7;
}

.vscode-menu.contents.item:hover{
background-color:#45475a;
border-bottom:1pxsolidrgba(255,255,255,0);
}
```

![VSCode YASB Widget](https://docs.yasb.dev/latest/widgets/assets/ee9942e2-56694a11-2a9c-0b46-0b1f1f5401b0.png)