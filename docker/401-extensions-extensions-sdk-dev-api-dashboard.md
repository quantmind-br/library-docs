---
title: Dashboard
url: https://docs.docker.com/extensions/extensions-sdk/dev/api/dashboard/
source: llms
fetched_at: 2026-01-24T14:27:38.143112673-03:00
rendered_js: false
word_count: 248
summary: This document outlines how to use the Docker Desktop Extension SDK to interact with the host UI, including displaying toast notifications, opening file dialogs, and launching external URLs.
tags:
    - docker-extension-sdk
    - desktop-ui
    - toast-notifications
    - file-selection
    - navigation
    - external-links
category: api
---

Table of contents

* * *

## [User notifications](#user-notifications)

Toasts provide a brief notification to the user. They appear temporarily and shouldn't interrupt the user experience. They also don't require user input to disappear.

### [success](#success)

▸ **success**(`msg`): `void`

Use to display a toast message of type success.

```
ddClient.desktopUI.toast.success("message");
```

### [warning](#warning)

▸ **warning**(`msg`): `void`

Use to display a toast message of type warning.

```
ddClient.desktopUI.toast.warning("message");
```

### [error](#error)

▸ **error**(`msg`): `void`

Use to display a toast message of type error.

```
ddClient.desktopUI.toast.error("message");
```

For more details about method parameters and the return types available, see [Toast API reference](https://docs.docker.com/reference/api/extensions-sdk/Toast/).

> Deprecated user notifications
> 
> These methods are deprecated and will be removed in a future version. Use the methods specified above.

```
window.ddClient.toastSuccess("message");
window.ddClient.toastWarning("message");
window.ddClient.toastError("message");
```

## [Open a file selection dialog](#open-a-file-selection-dialog)

This function opens a file selector dialog that asks the user to select a file or folder.

▸ **showOpenDialog**(`dialogProperties`): `Promise`&lt; [`OpenDialogResult`](https://docs.docker.com/reference/api/extensions-sdk/OpenDialogResult/)&gt;:

The `dialogProperties` parameter is a list of flags passed to Electron to customize the dialog's behaviour. For example, you can pass `multiSelections` to allow a user to select multiple files. See [Electron's documentation](https://www.electronjs.org/docs/latest/api/dialog) for a full list.

```
const result = await ddClient.desktopUI.dialog.showOpenDialog({
  properties: ["openDirectory"],
});
if (!result.canceled) {
  console.log(result.paths);
}
```

## [Open a URL](#open-a-url)

This function opens an external URL with the system default browser.

▸ **openExternal**(`url`): `void`

```
ddClient.host.openExternal("https://docker.com");
```

> The URL must have the protocol `http` or `https`.

For more details about method parameters and the return types available, see [Desktop host API reference](https://docs.docker.com/reference/api/extensions-sdk/Host/).

> Deprecated user notifications
> 
> This method is deprecated and will be removed in a future version. Use the methods specified above.

```
window.ddClient.openExternal("https://docker.com");
```

## [Navigation to Dashboard routes](#navigation-to-dashboard-routes)

From your extension, you can also [navigate](https://docs.docker.com/extensions/extensions-sdk/dev/api/dashboard-routes-navigation/) to other parts of the Docker Desktop Dashboard.