---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/dev/widgets/todo
source: crawler
fetched_at: 2026-02-23T05:20:36.923618-03:00
rendered_js: false
word_count: 57
---

The Todo widget provides a simple task management interface directly in your YASB bar. It displays the number of tasks, completed tasks, and allows you to add, check, categorize, and delete tasks. The widget is highly customizable with icons, categories, and menu options. Widget data is stored in a JSON file (`todo.json`) in the YASB config directory.

```
todo:
type:"yasb.todo.TodoWidget"
options:
label:"\uf0ae{count}/{completed}"
label_alt:"\uf0aeTasks:{count}"
# data_path: "~/Documents/my-todos.json"  # Optional: custom JSON file path
menu:
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"system"
alignment:"center"
direction:"down"
offset_top:6
offset_left:0
icons:
add:"\uf501NewTask"
edit:"Edit"
delete:"Delete"
date:"\ue641"
category:"\uf412"
checked:"\udb80\udd34"
unchecked:"\udb80\udd30"
sort:"\ueab4"
no_tasks:"\uf4a0"
categories:
default:
label:"General"
soon:
label:"Completesoon"
today:
label:"Endofday"
urgent:
label:"Urgent"
important:
label:"Important"
callbacks:
on_left:"toggle_menu"
on_middle:"do_nothing"
on_right:"toggle_label"
```

```
.todo-widget{}
.todo-widget.icon{}
.todo-widget.label{}
/* todo-menu styles */
.todo-menu{}
.todo-menu.header{}
.todo-menu.header.add-task-button{}
.todo-menu.header.tab-buttons{}
.todo-menu.header.tab-buttons.in-progress{}
.todo-menu.header.tab-buttons.completed{}
.todo-menu.header.tab-buttons.in-progress:checked{}
.todo-menu.header.tab-buttons.completed:checked{}
.todo-menu.header.tab-buttons.sort{}
.todo-menu.header.tab-buttons.sort:pressed{}
.todo-menu.header.toggle-tab.in-progress{}
.todo-menu.no-tasks{}
.todo-menu.no-tasks-icon{}
/* todo-menu task item styles */
.todo-menu.task-item{}
.todo-menu.task-item.expanded{}
/* todo-menu task item styles based on category */
.todo-menu.task-item.important{}
.todo-menu.task-item.urgent{}
.todo-menu.task-item.soon{}
.todo-menu.task-item.today{}
.todo-menu.task-item.default{}

.todo-menu.task-item.drop-highlight{}
.todo-menu.task-item.drop-highlight:hover{}
.todo-menu.task-item.drop-highlight:focus{}
.todo-menu.task-item.title{}
.todo-menu.task-item.completed.title{}
.todo-menu.task-item.completed.description{}
.todo-menu.task-item.description{}
.todo-menu.task-checkbox{}
.todo-menu.task-checkbox:checked{}
.todo-menu.task-info-row{}
.todo-menu.task-info-row.date-text{}
.todo-menu.task-info-row.category-text{}
.todo-menu.task-info-row.date-icon{}
.todo-menu.task-info-row.category-icon{}
.todo-menu.task-info-row.category-text.important{}
.todo-menu.task-info-row.category-icon.important{}
.todo-menu.task-info-row.category-text.urgent{}
.todo-menu.task-info-row.category-icon.urgent{}
.todo-menu.task-info-row.category-text.soon{}
.todo-menu.task-info-row.category-icon.soon{}
.todo-menu.task-info-row.category-text.today{}
.todo-menu.task-info-row.category-icon.today{}
.todo-menu.task-info-row.edit-task-button{}
.todo-menu.task-info-row.delete-task-button{}
/* todo-menu dialog styles */
.todo-menu.app-dialog{}
.todo-menu.app-dialog.buttons-container{}
.todo-menu.app-dialog.title-field{}
.todo-menu.app-dialog.desc-field{}
.todo-menu.app-dialog.title-field:focus{}
.todo-menu.app-dialog.desc-field:focus{}
.todo-menu.app-dialog.buttons-container.button{}
.todo-menu.app-dialog.button{}
.todo-menu.app-dialog.button:pressed{}
.todo-menu.app-dialog.button.add{}
.todo-menu.app-dialog.button.add:pressed{}
.todo-menu.app-dialog.warning-message{}
.todo-menu.app-dialog.category-button{}
.todo-menu.app-dialog.category-button.urgent{}
.todo-menu.app-dialog.category-button.soon{}
.todo-menu.app-dialog.category-button.today{}
.todo-menu.app-dialog.category-button.important{}
.todo-menu.app-dialog.category-button:checked{}
```

```
/* Todo Widget Styles */
.todo-widget{
padding:06px06px;
}
.todo-widget.icon{
color:#00f8d7;
padding:0;
}
.todo-widget.label{
font-size:12px;
padding:0;
}
/* Todo Menu Styles */
.todo-menu{
background-color:rgba(24,25,27,0.8);
min-width:400px;
max-width:400px;
min-height:500px;
max-height:500px;
}
.todo-menu.header{
margin:16px10px
}
.todo-menu.header.add-task-button,
.todo-menu.header.tab-buttons{
border:none;
border-radius:13px;
color:#ffffff;
padding:4px8px;
font-size:14px;
font-weight:600;
margin:0px;
font-family:'Segoe UI','JetBrainsMono NFP';
}
.todo-menu.header.tab-buttons{
margin:0;
font-size:12px;
}
.todo-menu.header.add-task-button:hover{
background-color:#0f91e7;
}
.todo-menu.header.tab-buttons.in-progress,
.todo-menu.header.tab-buttons.completed{
background-color:transparent;
}
.todo-menu.header.tab-buttons.in-progress:checked{
color:#7fffd4;
}
.todo-menu.header.tab-buttons.completed:checked{
color:#ff583b;
}
.todo-menu.header.tab-buttons.sort{
background-color:rgba(255,255,255,0.1);
color:#ffffff;
border-radius:10px;
min-height:20px;
min-width:20px;
max-width:20px;
max-height:20px;
padding:0;
margin:08px00;
font-family:'JetBrainsMono NFP';
}
.todo-menu.header.tab-buttons.sort:pressed{
background-color:rgba(255,255,255,0.2);
}
.todo-menu.no-tasks{
font-family:'Segoe UI';
font-size:18px;
color:#979fa0;
font-weight:400;
margin-top:16px;
}
.todo-menu.no-tasks-icon{
font-size:80px;
color:#979fa0;
font-family:"JetBrainsMono NFP";
margin-top:64px;
font-weight:400;
}

/* Task item styles */
.todo-menu.task-item{
background-color:rgba(0,0,0,0.1);
border-radius:8px;
margin:0px12px8px12px;
border:1pxsolidrgba(255,255,255,0.1);
padding:8px0;
}
.todo-menu.task-item.expanded{
background-color:rgba(211,214,219,0.1);
border:1pxsolidrgba(255,255,255,0.2);
}
.todo-menu.task-item.drop-highlight,
.todo-menu.task-item.drop-highlight:hover,
.todo-menu.task-item.drop-highlight:focus{
background-color:rgba(0,120,212,0.26);
border:1pxsolid#007acc;
}
.todo-menu.task-item.title{
color:#ebebeb;
font-size:13px;
font-weight:600;
font-family:'Segoe UI';
padding:08px8px8px;
margin-top:6px;
}
.todo-menu.task-item.completed.title,
.todo-menu.task-item.completed.description{
text-decoration:line-through;
color:#7f8c8d;
}
.todo-menu.task-item.description{
color:#bdc3c7;
font-size:12px;
font-weight:600;
padding:08px8px8px;
font-family:'Segoe UI';
}
.todo-menu.task-checkbox{
background-color:transparent;
border:none;
margin-left:12px;
margin-top:5px;
font-size:18px;
color:#ebebeb;
font-family:'JetBrainsMono NFP';
}
.todo-menu.task-checkbox:checked{
color:#7f8c8d;
}

/* Task info row styles */
.todo-menu.task-info-row{
margin-left:8px;
margin-bottom:8px;
}
.todo-menu.task-info-row.date-text,
.todo-menu.task-info-row.category-text{
font-family:'Segoe UI';
font-weight:600;
color:#7e7f88;
font-size:13px;
padding-left:0px;
margin-right:12px;
}
.todo-menu.task-info-row.date-icon,
.todo-menu.task-info-row.category-icon{
font-weight:400;
color:#a7a8b3;
font-size:14px;
font-family:'JetBrainsMono NFP';
margin-top:1px;
}
.todo-menu.task-info-row.category-text.important,
.todo-menu.task-info-row.category-icon.important{
color:#ff2600;
}
.todo-menu.task-info-row.category-text.urgent,
.todo-menu.task-info-row.category-icon.urgent{
color:#ff583b;
}
.todo-menu.task-info-row.category-text.soon,
.todo-menu.task-info-row.category-icon.soon{
color:#7fffd4;
}
.todo-menu.task-info-row.category-text.today,
.todo-menu.task-info-row.category-icon.today{
color:#f9e2af;
}
.todo-menu.task-info-row.delete-task-button{
background-color:rgb(160,160,160);
color:#000000;
font-family:'Segoe UI';
font-weight:600;
font-size:12px;
padding:08px;
border-radius:10px;
min-height:20px;
max-height:20px;
margin-right:8px;
}

/* App dialog style */
.todo-menu.app-dialog{
font-family:'Segoe UI';
background-color:#202020;
}
.todo-menu.app-dialog.buttons-container{
background-color:#171717;
margin-top:16px;
border-top:1pxsolid#000;
max-height:80px;
min-height:80px;
padding:020px020px;
}

.todo-menu.app-dialog.title-field,
.todo-menu.app-dialog.desc-field{
background-color:#181818;
border:1pxsolid#303030;
border-radius:4px;
padding:06px;
font-family:'Segoe UI';
font-size:12px;
font-weight:600;
color:#FFFFFF;
margin:10px0px5px0;
min-height:30px;
}
.todo-menu.app-dialog.desc-field{
max-height:60px;
}
.todo-menu.app-dialog.title-field:focus,
.todo-menu.app-dialog.desc-field:focus{
border-bottom-color:#4cc2ff;
}
.todo-menu.app-dialog.button{
background-color:#2d2d2d;
border:none;
border-radius:4px;
font-family:'Segoe UI';
font-size:12px;
font-weight:600;
color:#FFFFFF;
min-width:80px;
padding:06px;
margin:10px05px6px;
min-height:28px;
outline:none;
}
.todo-menu.app-dialog.buttons-container.button{
margin:10px05px0px;
font-size:13px;
}
.todo-menu.app-dialog.button:focus{
border:2pxsolid#adadad;
}
.todo-menu.app-dialog.button:focus,
.todo-menu.app-dialog.button:hover{
background-color:#4A4A4A;
}
.todo-menu.app-dialog.button:pressed{
background-color:#3A3A3A;
}
.todo-menu.app-dialog.button.add{
background-color:#0078D4;
}
.todo-menu.app-dialog.button.add:focus,
.todo-menu.app-dialog.button.add:hover{
background-color:#0066B2;
}
.todo-menu.app-dialog.button.add:pressed{
background-color:#00509E;
}
.todo-menu.app-dialog.warning-message{
background-color:#2b0b0e;
border:1pxsolid#5a303c;
border-radius:4px;
color:#cc9b9f;
font-family:'Segoe UI';
font-size:12px;
font-weight:600;
padding:8px12px;
margin:4px0px;
}
.todo-menu.app-dialog.category-button{
background-color:#2d2d2d;
border:none;
border-radius:4px;
font-family:'Segoe UI';
font-size:11px;
font-weight:700;
color:#afafaf;
padding:06px;
margin-top:8px;
min-height:24px;
outline:none;
}
.todo-menu.app-dialog.category-button:checked{
background-color:#535353;
color:#ffffff;
}
```