---
title: Remote files
title: Remote file
word_count: 265
summary: This document explains how to use the kitty terminal emulator to interact with, edit, and transfer files over an existing SSH connection.
category: guide
word_count: 265
optimized: true
optimized_at: 2026-05-04T20:44:49Z
---
optimized: true
optimized_at: 2026-05-04T18:00:00Z
# Remote files

|kitty| has the ability to easily *Edit*, *Open* or *Download* files from a
computer into which you are SSHed. In your SSH session run:

```
ls --hyperlink=auto
```

Then hold down Ctrl+Shift and click the name of the file.

![Remote file actions](../screenshots/remote_file.png)

|kitty| will ask you what you want to do with the remote file. You can choose
to *Edit* it in which case kitty will download it and open it locally in your
EDITOR. As you make changes to the file, they are automatically
transferred to the remote computer. Note that this happens without needing
to install *any* special software on the server, beyond ls that
supports hyperlinks.

> [!NOTE]
> See the edit-in-kitty <edit_file> command
>
>

> [!NOTE]
> See the transfer kitten
>
>

> [!NOTE]
> For best results, use this kitten with the ssh kitten <./ssh>.
> Otherwise, nested SSH sessions are not supported. The kitten will always try to copy
> remote files from the first SSH host. This is because, without the ssh
> kitten, there is no way for
> |kitty| to detect and follow a nested SSH session robustly. Use the
> transfer kitten for such situations.

> [!NOTE]
> If you have not setup automatic password-less SSH access, and are not using
> the ssh kitten, then, when editing
> starts you will be asked to enter your password just once, thereafter the SSH
> connection will be re-used.

Similarly, you can choose to save the file to the local computer or download
and open it in its default file handler.
