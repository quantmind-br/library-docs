---
title: docker debug
url: https://docs.docker.com/reference/cli/docker/debug/
source: llms
fetched_at: 2026-01-24T14:35:52.753347414-03:00
rendered_js: false
word_count: 864
summary: Explains how to use the docker debug CLI tool to access interactive shells and diagnostic tools in Docker containers and images, even those without an internal shell.
tags:
    - docker-debug
    - cli-tools
    - container-debugging
    - slim-images
    - troubleshooting
    - docker-desktop
category: reference
---

DescriptionGet a shell into any container or image. An alternative to debugging with \`docker exec\`.Usage`debug [OPTIONS] {CONTAINER|IMAGE}`

Requires: Docker Desktop 4.49 and later. For Docker Desktop versions 4.48.0 and earlier, you must have a Pro, Team, or Business subscription

Docker Debug is a CLI command that helps you follow best practices by keeping your images small and secure. With Docker Debug, you can debug your images while they contain the bare minimum to run your application. It does this by letting you create and work with slim images or containers that are often difficult to debug because all tools have been removed. For example, while typical debug approaches like `docker exec -it my-app bash` may not work on a slim container, `docker debug` will work.

With `docker debug` you can get a debug shell into any container or image, even if they don't contain a shell. You don't need to modify the image to use Docker Debug. However, using Docker Debug still won't modify your image. Docker Debug brings its own toolbox that you can easily customize. The toolbox comes with many standard Linux tools pre-installed, such as `vim`, `nano`, `htop`, and `curl`. Use the builtin `install` command to add additional tools available on [https://search.nixos.org/packages](https://search.nixos.org/packages). Docker Debug supports `bash`, `fish`, and `zsh`. By default it tries to auto-detect your shell.

Custom builtin tools:

- `install [tool1] [tool2]`: Add Nix packages from: [https://search.nixos.org/packages](https://search.nixos.org/packages), see [example](#managing-your-toolbox-using-the-install-command).
- `uninstall [tool1] [tool2]`: Uninstall Nix packages.
- `entrypoint`: Print, lint, or run the entrypoint, see [example](#understanding-the-default-startup-command-of-a-container-entry-points).
- `builtins`: Show custom builtin tools.

> For images and stopped containers, all changes are discarded when leaving the shell. At no point, do changes affect the actual image or container. When accessing running or paused containers, all filesystem changes are directly visible to the container. The `/nix` directory is never visible to the actual image or container.

OptionDefaultDescription`--shell``auto`Select a shell. Supported: `bash`, `fish`, `zsh`, `auto`.`-c, --command`Evaluate the specified commands instead of starting an interactive session, see [example](#running-commands-directly-eg-for-scripting).`--host`Daemon docker socket to connect to. E.g.: `ssh://root@example.org`, `unix:///some/path/docker.sock`, see [example](#remote-debugging-using-the---host-option).

### [Debugging containers that have no shell (slim containers)](#debugging-containers-that-have-no-shell-slim-containers)

The `hello-world` image is very simple and only contains the `/hello` binary. It's a good example of a slim image. There are no other tools and no shell.

Run a container from the `hello-world` image:

The container exits immediately. To get a debug shell inside, run:

The debug shell allows you to inspect the filesystem:

The file `/hello` is the binary that was executed when running the container. You can confirm this by running it directly:

After running the binary, it produces the same output.

### [Debugging (slim) images](#debugging-slim-images)

You can debug images directly by running:

You don't even need to pull the image as `docker debug` will do this automatically like the `docker run` command.

### [Modifying files of a running container](#modifying-files-of-a-running-container)

Docker debug lets you modify files in any running container. The toolbox comes with `vim` and `nano` pre-installed.

Run an nginx container and change the default `index.html`:

To confirm nginx is running, open a browser and navigate to http://localhost:8080. You should see the default nginx page. Now, change it using vim:

Change the title to "Welcome to my app!" and save the file. Now, reload the page in the browser and you should see the updated page.

### [Managing your toolbox using the `install` command](#managing-your-toolbox-using-the-install-command)

The builtin `install` command lets you add any tool from [https://search.nixos.org/packages](https://search.nixos.org/packages) to the toolbox. Keep in mind adding a tool never modifies the actual image or container. Tools get added to only your toolbox. Run `docker debug` and then install `nmap`:

You can confirm `nmap` is now part of your toolbox by getting a debug shell into a different image:

`nmap` is still there.

### [Understanding the default startup command of a container (entry points)](#understanding-the-default-startup-command-of-a-container-entry-points)

Docker Debug comes with a builtin tool, `entrypoint`. Enter the `hello-world` image and confirm the entrypoint is `/hello`:

The `entrypoint` command evaluates the `ENTRYPOINT` and `CMD` statement of the underlying image and lets you print, lint, or run the resulting entrypoint. However, it can be difficult to understand all the corner cases from [Understand how CMD and ENTRYPOINT interact](https://docs.docker.com/reference/dockerfile/#understand-how-cmd-and-entrypoint-interact). In these situations, `entrypoint` can help.

Use `entrypoint` to investigate what actually happens when you run a container from the Nginx image:

The output tells you that on startup of the nginx image, a script `/docker-entrypoint.sh` is executed with the arguments `nginx -g daemon off;`. You can test the entrypoint by using the `--run` option:

This starts nginx in your debug shell without having to actually run a container. You can shutdown nginx by pressing `Ctrl`+`C`.

### [Running commands directly (e.g., for scripting)](#running-commands-directly-eg-for-scripting)

Use the `--command` option to evaluate a command directly instead of starting an interactive session. For example, this is similar to `bash -c "arg1 arg2 ..."`. The following example runs the `cat` command in the nginx image without starting an interactive session.

### [Remote debugging using the --host option](#remote-debugging-using-the---host-option)

The following examples shows how to use the `--host` option. The first example uses SSH to connect to a remote Docker instance at `example.org` as the `root` user, and get a shell into the `my-container` container.

The following example connects to a different local Docker Engine, and gets a shell into the `my-container` container.