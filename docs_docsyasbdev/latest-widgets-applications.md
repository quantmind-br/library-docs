---
title: YASB Reborn - Yet Another Status Bar
url: https://docs.yasb.dev/latest/widgets/applications
source: crawler
fetched_at: 2026-02-23T05:28:31.300151-03:00
rendered_js: false
word_count: 0
---

```
apps:
type:"yasb.applications.ApplicationsWidget"
options:
label:"{data}"
app_list:

-{icon:"\uf0a2", launch:"notification_center", name:"NotificationCenter"}# launch notification center
-{icon:"\ueb51", launch:"quick_settings"}# launch quick settings
-{icon:"\uf422", launch:"search"}# launch search
-{icon:"\uf489", launch:"wt", name:"WindowsTerminal"}# launch terminal
-{icon:"C:\\Users\\marko\\icons\\vscode.png", launch:"C:\\Users\\Username\\AppData\\Local\\Programs\\MicrosoftVSCode\\Code.exe"}# open vscode
-{icon:"\udb81\udc4d",launch:"\"C:\\ProgramFiles\\MozillaFirefox\\firefox.exe\"-new-tabwww.reddit.com"}# open reddit in new tab in firefox
-{icon:"\udb81\udc4d",launch:"\"C:\\ProgramFiles\\MozillaFirefox\\firefox.exe\"-new-windowwww.reddit.com"}# open reddit in new window in firefox
-{icon:"\udb81\udc4d",launch:"\"C:\\ProgramFiles\\MozillaFirefox\\firefox.exe\"-private-windowwww.reddit.com"}# open reddit in private window in firefox
label_shadow:
enabled:true
color:"black"
radius:3
offset:[1,1]
```

```
.apps-widget{}
.apps-widget.widget-container{}
.apps-widget.widget-container.label{/*icons*/}
```