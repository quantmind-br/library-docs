---
title: Git for developers | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/guides/git
source: sitemap
fetched_at: 2026-02-17T15:05:14.438034-03:00
rendered_js: false
word_count: 2920
summary: This document provides a comprehensive guide for developers on setting up and using Git for Moodle development, covering installation, configuration, and standard contribution workflows. It explains how to manage local and public repositories while integrating with tools like the Moodle Developer Kit.
tags:
    - git-workflow
    - moodle-development
    - version-control
    - github-setup
    - repository-management
    - developer-tools
category: guide
---

A reasonable knowledge of the Git basics is a good idea before you start to use it for development. If you are new to Git, you are encouraged to go to the [See also](#see_also) section on this page for some more general reading.

Moodle has also created a tool known as [MDK (Moodle Developer Kit)](https://moodledev.io/general/development/tools/mdk) to streamline a lot of the processes detailed on this page. It is recommended that you consider MDK as it is a very powerful tool and can be used together with Git to make Moodle development much easier.

## General workflow[​](#general-workflow "Direct link to General workflow")

A detailed explanation of Moodle's workflow can be found on the [Development process](https://moodledev.io/general/development/process) page. In short, Moodle development with Git looks like this:

![git-pushpull-model.png](https://moodledev.io/assets/images/git-pushpull-model-6367a95eaa3e56d99d7d2488385cd3d2.png)

1. You, the contributor, commit changes to your personal repository.
2. You push the changes to your public repository and publish links to your changes in the Moodle Tracker.
3. You request a peer review of your code from another developer.
4. When the peer reviewer is happy, they submit the issue for integration.
5. Moodle integrators pull the changes from your public repository, and if approved, they merge them into Moodle's integration repository.
6. The integrated change are tested and finally pushed into Moodle's production repository.
7. You synchronise your local repository with Moodle's production repository and the process repeats.

This workflow runs in weekly cycles. The integration happens on Monday and Tuesday and the testing on Wednesday. On Thursday (or Friday if testing takes too long), the production repository (moodle.git) is usually updated with changes from the last development week.

Most Moodle developers have their public repositories hosted at [GitHub](http://github.com/). In these examples, we'll assume you've set up your public repository there too.

note

When you first register on Moodle Tracker you can not assign issues to yourself or send them for peer review. You will be added to the developers group after your first bug fix is integrated. Before that, just comment on the issue with a link to your branch and a component lead, or another developer, will send the issue for peer review for you.

## Installing Git on your computer[​](#installing-git-on-your-computer "Direct link to Installing Git on your computer")

### Installing Git[​](#installing-git "Direct link to Installing Git")

Most Linux distributions have Git available as a package to install.

#### Debian/Ubuntu[​](#debianubuntu "Direct link to Debian/Ubuntu")

#### MacOS (Homebrew)[​](#macos-homebrew "Direct link to MacOS (Homebrew)")

#### Windows[​](#windows "Direct link to Windows")

Download the latest Git installer at [Git for Windows](https://gitforwindows.org/).

## Configuring Git[​](#configuring-git "Direct link to Configuring Git")

After installation, set your name and email. Your name and email will become part of your commits and can't be changed later once your commits are accepted into Moodle code. Therefore we ask contributors to use their real names written in with proper capitalisation. E.g. "John Smith" and not "john smith", or even "john5677".

```
git config --global user.name "Your Name"
git config --global user.email yourmail@domain.tld
```

Unless you are the repository maintainer, it is wise to set your Git to not push changes in file permissions:

```
git config --global core.filemode false
```

It's recommended to verify that the your Git installation is not performing any transformation between LFs and CRLFs. Moodle use **only LFs** and you should configure your editor/IDE the same way. Note that having any "magic" enabled is known to cause [problems with unit tests](https://docs.moodle.org/dev/Common_unit_test_problems#The_test_file_.22evolution.test.22_should_not_contain_section_named_.22.5Blots_of_content.5D.22) execution. We recommend you to set:

```
git config --global core.autocrlf false
```

## Setting-up your public repository[​](#setting-up-your-public-repository "Direct link to Setting-up your public repository")

There are many different options when considering where to host your git repository. [GitHub](http://github.com/) is a popular option that many developers use because it is free and well supported. Moodle also incorporates a series of GitHub Actions that are used to verify your code automatically and can help identify issues.

1. Go to [GitHub](http://github.com/) and create an account.
2. Go to the official [Moodle GitHub repository](http://github.com/moodle/moodle) and click on the Fork button. You now have your own GitHub Moodle repository.
3. Set up your SSH public key so you can push to your GitHub Moodle repository from your local Moodle repository. Over at GitHub, navigate to your Settings page and look for a section called **SSH and GPG keys**. Configuring your SSH key can be a little tricky, but following [GitHub's SSH setup steps](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent) will ensure the hardest part of this setup is done correctly.
4. Optionally, you can set up [GitHub Actions](https://moodledev.io/general/development/tools/gha) to automatically test your code. This provides the advantage of catching issues without having to set up a testing environment locally and provides helpful feedback before you submit your code for review.

## Setting-up your local repository[​](#setting-up-your-local-repository "Direct link to Setting-up your local repository")

Create a local clone of your GitHub repository by using this command in your terminal:

```
git clone git@github.com:YOUR_GITHUB_USERNAME/moodle.git
```

This command does several jobs for you:

- Creates a new folder
- Initialises a new local Git repository
- Sets your GitHub repository as the remote repository called 'origin'
- Makes a local checkout of the branch 'main'

tip

[MDK](https://moodledev.io/general/development/tools/mdk) features many commands that aid in the creation and management of your Moodle branches. If you haven't checked it out already, see how MDK can streamline your Moodle development.

## Keeping your public repository up-to-date[​](#keeping-your-public-repository-up-to-date "Direct link to Keeping your public repository up-to-date")

Your fork at GitHub is not updated automatically. To keep it synced with the upstream Moodle repository, you have to fetch the recent changes from the official moodle.git repository. To avoid conflicts, it is strongly recommended that you never modify the standard Moodle branches. Never commit directly into `main` and `MOODLE_XXX_STABLE` branches, but instead create topic branches to work on. In Git terminology, the `main` branch and `MOODLE_XXX_STABLE` branches should always be fast-forwardable.

![git-sync-github.png](data:image/png;base64,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)

To keep your public repository up-to-date, we will register the remote repository `git@github.com:moodle/moodle.git` under the **upstream** alias. Then we create a script to be run regularly that fetches changes from the upstream repository and pushes them to your public repository. Note that this procedure will not affect your local repository.

To register the upstream remote use the following command in your Moodle installation root folder:

```
git remote add upstream git://git.moodle.org/moodle.git
```

The following commands can be used to keep the your forked Moodle branches at your GitHub repository synced with Moodle's upstream repository. You may wish to store them in a script so that you can run it every week after the upstream repository is updated.

```
#!/bin/bash
git fetch upstream
for BRANCH in MOODLE_{19..39}_STABLE MOODLE_{310..311}_STABLE MOODLE_{400..404}_STABLE main; do
    git push origin refs/remotes/upstream/$BRANCH:refs/heads/$BRANCH
done
```

caution

Never commit directly into `main` and `MOODLE_XXX_STABLE` branches

tip

[MDK](https://moodledev.io/general/development/tools/mdk) keeps track of the official Moodle remotes for you. If you're using MDK, just issue the following command in your repository directory:

### How it works[​](#how-it-works "Direct link to How it works")

The `git fetch` command does not modify your current working directory. It just downloads all recent changes from a remote repository and stores them into remote-tracking branches. The `git push` command takes these remote-tracking branches from upstream and pushes them to GitHub under the same name. Understanding this fully requires a bit of knowledge and experience with Git.

note

There is no need to switch your local branch during this. You can even execute this via cron at your machine. Just note that the upstream repository updates typically just once a week.

### New branches[​](#new-branches "Direct link to New branches")

Occasionally, Moodle will create a new branch that does not exist in your public repository. If you try to push this new branch, you will see an error such as the following:

```
error: unable to push to unqualified destination: MOODLE_99_STABLE
The destination refspec neither matches an existing ref on the remote
nor begins with refs/, and we are unable to guess a prefix based on the source ref.
error: failed to push some refs to 'git@github.com:YOUR_GITHUB_USERNAME/moodle.git'
```

In the above example, `MOODLE_99_STABLE`, is the name of the new branch that does not exist in your public repository. To fix the error, you need to create the new branch on your public repository using the following commands, replacing `MOODLE_99_STABLE` with the name of the new branch you wish to create:

```
git checkout MOODLE_99_STABLE
git push origin MOODLE_99_STABLE:MOODLE_99_STABLE
```

The above code will create a new copy of the `MOODLE_99_STABLE` branch in your local repository. If you do not need to keep a local copy of the new branch (probably the case), you can remove it from your local repository as follows:

```
git checkout main
git branch -D MOODLE_99_STABLE
```

## Preparing a patch[​](#preparing-a-patch "Direct link to Preparing a patch")

### Creating a new branch[​](#creating-a-new-branch "Direct link to Creating a new branch")

As mentioned earlier, you never work on standard Moodle branches directly. Every time you are going to edit something, switch to a local branch. Fork the local branch off Moodle's standard branch that you think it should be eventually merged to.

For example, if you are working on a patch for **4.1**, fork the branch off `MOODLE_401_STABLE`. Patches for the next [major version](https://docs.moodle.org/dev/Moodle_versions) should be based on the `main` branch.

```
git checkout -b MDL-xxxxx-main_brief_name origin/main
```

If you forget to specify the branch you want to fork from, the new branch will be based on the currently checked-out branch. It is recommended you always specify this.

To check the current branch you are on:

The current branch should be highlighted in the resulting list.

### Committing your changes[​](#committing-your-changes "Direct link to Committing your changes")

Once you have worked on some code, you should commit your changes to your local branch. The commit message used should be reflective of the issue you are developing for and respect the guidelines set out in our [Coding style](https://moodledev.io/general/development/policies/codingstyle#git-commits).

```
git status
git add .
git commit -m "MDL-XXXXX example: Developed an amazing new feature"
```

At this stage your commit has only been recorded locally. Nothing has been sent to any other server yet. To see the history of all Git commits, use:

Your local branch changes may consist of several commits. Once you are happy with it, and you have checked it against Moodle's [Coding styles](https://moodledev.io/general/development/policies/codingstyle), publish your changes by pushing to your public repository.

```
git push origin MDL-xxxxx-main_brief_name
```

Now your branch is published and you can ask Moodle core developers to review it and eventually integrate it into Moodle's main repository.

### Changing commit messages[​](#changing-commit-messages "Direct link to Changing commit messages")

It often happens that you make a mistake in your patch, or in the commit message, and CiBot (our CI application) directs your attention to changes that must/should be made. You can "rewrite history" and change the existing commits.

There are a couple of ways this can be achieved.

#### Reset all changes and commit again[​](#reset-all-changes-and-commit-again "Direct link to Reset all changes and commit again")

The following command will preserve your changes, but all commits on top of `main` branch will be gone and become **unstaged** and ready to be added and committed again.

```
git reset --mixed origin/main
```

#### Rebase your changes[​](#rebase-your-changes "Direct link to Rebase your changes")

The `git rebase` command is a powerful tool that can change the sequence of commits, change commit messages, squash commits, and more. We will not cover it all here, but there are [many articles](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) on the Internet about it.

Rebase your branch using the following command:

Whichever option you chose, you have "rewritten history". If you had already pushed your branch to your remote repository, you may encounter issues when trying to push the updated branch. If you try `git push MDL-xxxxx-main_brief_name` you will get an error message suggesting you to `force push`.

To force push the changed commits use:

```
git push -f origin MDL-xxxxx-main_brief_name
```

If an error occurs because you are still using the git protocol (read only), use this command:

```
git remote set-url origin https://github.com/YOUR_GITHUB_USERNAME/moodle.git
```

A prompt will ask for your credentials. If you previously setup your SSH public key, you can also use this command:

```
git remote set-url origin git@github.com:YOUR_GITHUB_USERNAME/moodle.git
```

### Checking if a branch has already been merged[​](#checking-if-a-branch-has-already-been-merged "Direct link to Checking if a branch has already been merged")

After some time contributing to Moodle, you will have accumulated many branches, both in your local repository and in your public repository. To prune these branches and delete those that were accepted by Moodle's upstream, use the following:

```
git fetch upstream
git branch --merged upstream/main
git branch --merged upstream/MOODLE_XXX_STABLE
```

#### Pruning local branches[​](#pruning-local-branches "Direct link to Pruning local branches")

The `git fetch upstream` command fetches the changes from your upstream repository (remember that `git fetch` does not modify your working directory, so it is safe to run it whenever). The `git branch --merged` commands displays all branches that are merged into the Moodle's upstream `main` branch and `MOODLE_XXX_STABLE` branch, respectively. To delete these local branches, use:

```
git branch -d MDL-xxxxx-main_accepted_branch
```

#### Pruning remote branches[​](#pruning-remote-branches "Direct link to Pruning remote branches")

A similar approach can be used to check the branches published at your origin repository (e.g. github.com).

```
git fetch origin
git fetch upstream
git branch -r --merged upstream/main
git branch -r --merged upstream/MOODLE_XXX_STABLE
```

The `git fetch upstream` command makes sure that you have all your branches from your origin repository recorded as the remote tracking branch locally. The `git branch -r --merged` commands work the same as in the previous example, but they list remote tracking branches only ([see -r param](http://www.kernel.org/pub/software/scm/git/docs/git-branch.html)).

To delete a branch on your origin repository, use:

```
git push origin :MDL-xxxxx-main_branch_to_delete
```

This syntax may look unfamiliar, however it is pretty logical. The general syntax of the `git push` command is:

```
git push <repository> <source ref>:<target ref>
```

Deleting a remote branch can be understood as pushing an "empty (null) reference" to it.

## Peer-reviewing someone else's code[​](#peer-reviewing-someone-elses-code "Direct link to Peer-reviewing someone else's code")

To review a branch on someone else's public repository, you do not need to register a new remote (unless you prefer to work that way).

Let us imagine your friend Alice pushed a work-in-progress branch called `wip-feature` into her GitHub repository and asked you to review it. All you need to know is the read-only address of the repository and the name of the branch.

```
git fetch git://github.com/alice/moodle.git wip-feature
```

This command will download all required data and keep the *pointer* to the tip of the `wip-feature` branch in a local, symbolic reference known as `FETCH_HEAD`. To see what's there on that branch, use:

To see how a particular file looks on Alice's branch, use:

```
git show FETCH_HEAD:admin/blocks.php
```

To create a new local branch called `alice-wip-feature` containing the work by Alice, use:

```
git checkout -b alice-wip-feature FETCH_HEAD
```

To merge Alice's work into your current branch, use:

To see what would be merged into the current branch without actually modifying anything, use:

Once you have acquired the code and are ready to review it, reference Moodle's [Peer Review Checklist](https://moodledev.io/general/development/process/peer-review).

## Rebasing a branch[​](#rebasing-a-branch "Direct link to Rebasing a branch")

Rebasing is a process when you cut off the branch from its current start point and transplant it to another point. Let us assume the following history exists:

The result of the command `git rebase main topic` would transplant the `topic` branch on top of the `main` branch and look like this:

### A typical scenario[​](#a-typical-scenario "Direct link to A typical scenario")

You may be asked to rebase your branch if the submitted branch was based on an outdated commit. Consider this example:

On Tuesday, we create a new topic branch, forked off the upstream `main` branch. On Wednesday, the upstream `main` branch is updated with all the changes from the last integration cycle. To make our branch easier to integrate, we rebase our branch against the newly updated `main` branch.

```
git rebase main MDL-xxxxx-main_topic_branch
```

Note that rebasing effectively rewrites the history of the branch. **Do not rebase the branch if there is a chance that somebody has already forked it and based their own branch on it.** For this reason, many Git tutorials discourage from rebasing any branch that has been published.

caution

All branches submitted for Moodle integration are potentially rebased and you should not base your own branches on them.

### Conflicts during rebase[​](#conflicts-during-rebase "Direct link to Conflicts during rebase")

During the rebase procedure, conflicts may appear. The `git status` command is useful for reporting any conflicting files. Investigate them carefully and fix them before adding and continuing your rebase.

```
vim conflicted.php
git add conflicted.php
git rebase --continue
```

## Applying changes from one branch to another[​](#applying-changes-from-one-branch-to-another "Direct link to Applying changes from one branch to another")

Most bugs are fixed on each stable branch (e.g. `MOODLE_400_STABLE`, `MOODLE_311_STABLE`). If you are working on an fix based on one of these branches, it is possible you will need to prepare a patch for other affected stable branches too.

In Moodle, we separately maintain the stable branches and the current development branch (main). We do not merge stable branches into the main one. Typically, the contributor prepares at least two branches: one with the fix for the affected stable branch(es), and one with the fix for the main branch.

Let's assume you have a patch prepared, based on `MOODLE_400_STABLE`, called `MDL-xxxxx-400_topic`. It is possible to apply this patch to other stable branches. There are a few ways we could achieve this.

### Cherry-picking a single commit[​](#cherry-picking-a-single-commit "Direct link to Cherry-picking a single commit")

Let's assume we have two local Git repositories:

1. `~/public_html/moodle_400` containing a local installation of Moodle 4.0, and
2. `~/public_html/moodle_main` containing a local installation of the most recent development version of Moodle.

They both use your public repository at github.com as the origin. You have a branch in `moodle_400` called `MDL-xxxxx-400_topic` that was forked off `MOODLE_400_STABLE`. It contains one commit. Now, you want to apply this commit to a new branch in `moodle_main` called `MDL-xxxxx-main_topic`.

```
cd ~/public_html/moodle_main
git checkout -b MDL-xxxxx-main_topic origin/main
git fetch ../moodle_400 MDL-xxxxx-400_topic
git cherry-pick FETCH_HEAD
```

1. The `git checkout -b MDL-xxxxx-main_topic origin/main` command creates new local branch, forked off `main`.
2. The `git fetch ../moodle_400 MDL-xxxxx-400_topic` command fetches all data needed to apply the topic branch, and sets the pointer to the tip of that branch with `FETCH_HEAD` as a symbolic reference.
3. The `git cherry-pick FETCH_HEAD` command picks the tip of the branch (the top-most commit) and tries to apply it on the current branch.

tip

There's a variant of the `git cherry-pick` command that supports multiple commits. Use `$ git cherry-pick A^..B` if you want to include commits from "A" to "B" (inclusive). Commit "A" should be older than "B".

### Applying a set of patches[​](#applying-a-set-of-patches "Direct link to Applying a set of patches")

Consider the branch `MDL-xxxxx-400_topic` from the previous example. Imagine the branch consisted of several commits. It may be easier to use the `git format-patch` and `git am` commands to apply the whole set of patches (patchset).

Firstly, you will need to export all commits from the topic branch to separate files.

```
cd ~/public_html/moodle_400
mkdir .patches
git format-patch -o .patches MOODLE_400_STABLE..MDL-xxxxx-400_topic
```

The `git format-patch -o .patches MOODLE_400_STABLE..MDL-xxxxx-400_topic` command takes all commits from the topic branch that are not in `MOODLE_400_STABLE` and exports them, one by one, to the output directory `.patches`. The generated files will contain the patch itself (in diff format), and additional information about the commit. This format allows you to easily email the files to another person for peer-review.

In this example, we will apply them to another repository.

```
cd ~/public_html/moodle_main
git checkout -b MDL-xxxxx-main_topic origin/main
git am -3 ../moodle_400/.patches/*
```

The `git am -3 ../moodle_400/.patches/*` command applies all the files from the `.patches` directory. When a patch does not apply cleanly, the command tries to fallback on a three-way merge (see the -3 parameter). If conflicts occur during the procedure, you can resolve them and use `git am --continue`, or abort the whole procedure with `git am --abort`.

## See also[​](#see_also "Direct link to See also")

- [Git tips](https://docs.moodle.org/dev/Git_tips)
- [Git commit cheat sheet](https://docs.moodle.org/dev/Commit_cheat_sheet)
- [Moodle's Git commit policy](https://moodledev.io/general/development/policies/codingstyle#git-commits)
- [MDK (Moodle Developer Kit)](https://moodledev.io/general/development/tools/mdk)
- [Renaming master branch to main](https://moodledev.io/general/community/plugincontribution/master2main)

### Moodle forum discussions[​](#moodle-forum-discussions "Direct link to Moodle forum discussions")

- [GIT help needed](http://moodle.org/mod/forum/discuss.php?d=168094)
- [Best way to manage CONTRIB code with GIT](http://moodle.org/mod/forum/discuss.php?d=165236)
- [Handy Git tip for tracking 3rd-party modules and plugins](http://moodle.org/mod/forum/discuss.php?d=167063)
- [Moodle Git repositories](http://moodle.org/mod/forum/discuss.php?d=167730)
- [Git help!! I don't understand rebase enough...](http://moodle.org/mod/forum/discuss.php?d=183409)
- [add MOODLE\_24\_STABLE to github.com repository](http://moodle.org/mod/forum/discuss.php?d=217617)

### External resources[​](#external-resources "Direct link to External resources")

- [Everyday GIT With 20 Commands Or So](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/giteveryday.html)
- ['Pro Git' complete book](https://git-scm.com/book/en/v2)
- [Getting git by Scott Chacon](http://vimeo.com/14629850) - an recording of an excellent 1-hour presentation that introducing git, including a simple introduction to what is going on under the hood.
- [Tim Hunt's blog: Fixing a bug in Moodle core: the mechanics](http://tjhunt.blogspot.co.uk/2012/03/fixing-bug-in-moodle-core-mechanics.html)
- [Flight rules for Git](https://github.com/k88hudson/git-flight-rules/blob/master/README.md#flight-rules-for-git)