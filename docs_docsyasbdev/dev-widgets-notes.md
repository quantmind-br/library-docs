---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/dev/widgets/notes
source: crawler
fetched_at: 2026-02-23T05:20:36.557771-03:00
rendered_js: false
word_count: 0
---

```
notes:
type:"yasb.notes.NotesWidget"
options:
label:"<span>\udb82\udd0c</span>{count}"
label_alt:"{count}notes"
# data_path: "~/Documents/my-notes.json"  # Optional: custom JSON file path
menu:
blur:true
round_corners:true
round_corners_type:"normal"
border_color:"System"
alignment:"right"
direction:"down"
offset_top:6
offset_left:0
max_title_size:150
show_date_time:true
icons:
note:"\udb82\udd0c"
delete:"\ueab8"
copy:"\uebcc"
callbacks:
on_left:"toggle_menu"
on_middle:"do_nothing"
on_right:"toggle_label"
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
/* Main widget container */
.notes-widget{}
.notes-widget.your_class{}/* If you are using class_name option */
/* Labels and icons */
.notes-widget.label{}
.notes-widget.icon{}
/* Popup menu */
.notes-menu{}
/* Note items inside the menu */
.notes-menu.note-item{}
/* Title text within each note item */
.notes-menu.title{}
/* Date text shown under the title */
.notes-menu.date{}
/* Message shown when no notes exist */
.notes-menu.empty-list{}
/* Buttons in the menu for add & cancel */
.notes-menu.add-button,
.notes-menu.cancel-button{}
/* Scroll area that contains all notes */
.notes-menu.scroll-area{}
/* Text input for adding notes */
.notes-menu.note-input{}
/* Focus style for the note input */
.notes-menu.note-input:focus{}
/* Button to delete a note */
.notes-menu.delete-button{}
/* Button hover effect */
.notes-menu.delete-button:hover{}
/* Button pressed effect */
.notes-menu.delete-button:pressed{}
/* Button to copy text */
.notes-menu.copy-button{}
/* Button hover effect */
.notes-menu.copy-button:hover{}
/* Button pressed effect */
.notes-menu.copy-button:pressed{}
/* Button pressed effect */
```

```
.notes-widget{
padding:0;
}
.notes-widget.label{
font-size:14px;
color:#dbfeb4;
}
.notes-widget.icon{
font-size:16px;
color:#dbfeb4;
}
/* Notes Widget Menu */
.notes-menu{
min-width:400px;
max-width:400px;
background-color:rgba(17,17,27,0.4);
}
.notes-menu.note-item{
background-color:transparent;
border-bottom:1pxsolidrgba(255,255,255,0.1);
}
.notes-menu.note-item:hover{
background-color:rgba(255,255,255,0.1);
}
.notes-menu.note-item.icon{
font-size:16px;
padding:04px;
}
.notes-menu.delete-button{
color:#ff6b6b;
background:transparent;
border:none;
font-size:8px;
padding:7px8px;
border-radius:3px;
}
.notes-menu.delete-button:hover{
background-color:rgba(128,128,128,0.5);
}
.notes-menu.copy-button{
color:#babfd3;
background:transparent;
border:none;
font-size:16px;
padding:4px8px;
border-radius:3px;
}
.notes-menu.copy-button:hover{
background-color:rgba(128,128,128,0.5);
}
.notes-menu.copy-button:pressed{
color:#ffffff;
}
.notes-menu.note-item.title{
font-size:13px;
font-family:'Segoe UI'
}
.notes-menu.note-item.date{
font-size:12px;
font-family:'Segoe UI';
color:rgba(255,255,255,0.4);
}
.notes-menu.empty-list{
font-family:'Segoe UI';
color:rgba(255,255,255,0.2);
font-size:24px;
font-weight:600;
padding:10px020px0;
}
.notes-menu.add-button,
.notes-menu.cancel-button{
padding:8px;
background-color:rgba(255,255,255,0.1);
border:none;
border-radius:4px;
color:white;
font-family:'Segoe UI'
}
.notes-menu.cancel-button{
margin-left:4px;
}
.notes-menu.add-button:hover,
.notes-menu.cancel-button:hover{
background-color:rgba(255,255,255,0.2);
}
.notes-menu.scroll-area{
background:transparent;
border:none;
border-radius:0;
}
.notes-menu.note-input{
background-color:rgba(17,17,27,0.2);
border:1pxsolidrgba(255,255,255,0.1);
font-family:'Segoe UI';
font-size:14px;
max-height:30px;
padding:4px;
border-radius:6px;
}
.note-input:focus{
border:1pxsolid#89b4fa;
}
```