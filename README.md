# issues

Work on your issues offline. In your terminal.

### Why?

There are plenty of command line issues manager for your GitLab/GitHub/BitBucket etc. None of them provides a way to work offline.

If you like to hack on your side projects on a train, plane, or maybe you are just offline, then this tool should help increase your productivity.

### Supported systems

- GitLab

### Supported SCM

- Git

*I have no plans to implement integration with other SCM right now. Feel free to open issue for this.*

### TODO

- Attach issue info to a commit through `git-notes(1)`?
- When listing all issues provide a commit hash with reference.
- Render markdown to terminal
- Render emoji in your terminal

### Usage

#### Configuration

It uses `git-config(1)` for configuration.

```sh
# URL for your GitLab instance. Consider using git config --global.
git config gitlab.url "URL of your GitLab instance"
# Auth token. Consider using git config --global.
git config gitlab.token "your private auth token"
# Name of project. Without namespace.
git config gitlab.project "name of project on GitLab"
# SQLite3 database that provides cache for downloaded issues
git config gitlab.cache "issues.sqlite3"
```

##### Operations

###### issues sync

Downloads all issues to disk. Uses `gitlab.cache` option to determine SQLite3 database location.

If it encounters any outgoing issues (posted with **new** command) in cache then it creates them on a server.

###### issues new

Opens `$EDITOR` so you can write new issue **locally**. Accepted format for your issue:

```sh
Title of your issue.

This is a long description for your issue.

# 
# Those lines are comments and are ignored
#
```

Write empty message to cancel.

###### issues list

Lists your cached issues.

### Authors

- Michał Papierski <michal@papierski.net>
