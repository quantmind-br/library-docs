---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/windows-desktops
source: crawler
fetched_at: 2026-02-23T05:28:48.712683-03:00
rendered_js: false
word_count: 0
---

```
windows_workspaces:
type:"yasb.windows_desktops.WorkspaceWidget"
options:
label_workspace_btn:"\udb81\udc3d"
label_workspace_active_btn:"\udb81\udc3e"
btn_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
.windows-desktops{}/*Style for widget.*/
.windows-desktops.widget-container{}/*Style for widget container.*/
.windows-desktops.ws-btn{}/*Style for buttons.*/
.windows-desktops.ws-btn.active{}/*Style for the active workspace button.*/
.windows-workspaces.ws-btn.button-1{}/*Style for first button.*/
.windows-workspaces.ws-btn.button-2{}/*Style for second  button.*/
.windows-workspaces.ws-btn.active.button-1{}/*Style for the active first workspace button.*/
.windows-workspaces.ws-btn.active.button-2{}/*Style for the active second workspace button.*/

.windows-desktops.context-menu{}/*Style for context menu.*/
.windows-desktops.context-menu.menu-item{}/*Style for context menu items.*/
.windows-desktops.context-menu.menu-item:hover{}/*Style for selected context menu items.*/
.windows-desktops.context-menu.separator{}/*Style for context menu separator.*/

.windows-desktops.rename-dialog{}/*Style for rename dialog.*/
.windows-desktops.rename-dialogQPushButton{}/*Style for rename dialog buttons.*/
.windows-desktops.rename-dialogQPushButton:hover{}/*Style for rename dialog buttons hover.*/
.windows-desktops.rename-dialogQLabel{}/*Style for rename dialog labels.*/
.windows-desktops.rename-dialogQLineEdit{}/*Style for rename dialog line edit.*/
```

```
.windows-desktops{
padding:04px014px;
}
.windows-desktops.widget-container{
background-color:#11111b;
margin:4px04px0;
border-radius:12px;
}
.windows-desktops.ws-btn{
color:#7f849c;
border:none;
font-size:14px;
margin:03px;
padding:0
}
.windows-desktops.ws-btn.active{
color:#89b4fa;
}

.windows-desktops.context-menu{
background-color:rgba(17,17,27,0.75);
border:none;
border-radius:2px;
padding:8px0;
}
.windows-desktops.context-menu.menu-item{
padding:6px16px;
}
.windows-desktops.context-menu.menu-item:hover{
background-color:rgba(255,255,255,0.05);
color:#ffffff;
}
.windows-desktops.context-menu.separator{
margin:2px0px2px0px;
height:1px;
background-color:rgba(255,255,255,0.1);
}

.windows-desktops.rename-dialog{
background-color:rgba(17,17,27,0.75);
}
.windows-desktops.rename-dialogQPushButton{
background-color:rgba(255,255,255,0.1);
color:#ffffff;
border:none;
padding:4px12px;
border-radius:4px;
}
.windows-desktops.rename-dialogQPushButton:hover{
background-color:#585858;
color:#ffffff;
border:none;
padding:4px12px;
border-radius:4px;
}

.windows-desktops.rename-dialogQLabel{
color:#ffffff;
}
.windows-desktops.rename-dialogQLineEdit{
background-color:transparent;
border:1pxsolid#89b4fa;
padding:4px;
color:#ffffff;
}
```