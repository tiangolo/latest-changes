# Latest Changes

Automatically add the changes from each PR to the release notes in a file.

## How to use

Install this GitHub action by creating a file in your repo at `.github/workflows/latest-changes.yml`.

A minimal example could be:

```YAML
name: Latest Changes

on:
  pull_request_target:
    branches:
      - main
      # Or use the branch "master" if that's your main branch:
      # - master
    types:
      - closed
  # For manually triggering it
  workflow_dispatch:
    inputs:
      number:
        description: PR number
        required: true

jobs:
  latest-changes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: docker://tiangolo/latest-changes:0.0.3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

**Note**: you can also use the GitHub action directly intead of with Docker, but that would take an extra minute:

```YAML
      # - uses: docker://tiangolo/latest-changes:0.0.3
      # This is slower but also works
      - uses: tiangolo/latest-changes:0.0.3
```

In this minimal example, it uses all the default configurations.

After merging a PR to the main branch, it will:

* Find a file `README.md`
* Inside of that file, find a "header" with the text:

```Markdown
### Latest Changes


```

...including the two breaking lines.

* Right after that, it will add a new list item with the changes:
    * Using the title from the PR.
        * **Tip**: make sure the PR has the title you want before merging it.
    * Including the PR number, with a link to the PR itself.
    * Including the PR author, with a link as well.

It will look something like:

> ### Latest Changes
>
> * ✨ Add support for Jinja2 templates for latest changes messages. PR [#23](https://github.com/tiangolo/latest-changes/pull/23) by [@tiangolo](https://github.com/tiangolo).

You can see an example of how it works in this same file, at the bottom, in [Latest Changes - Latest Changes 🤷](##latest-changes---latest-changes-).

* Then it will commit the changes, and push them to your repo. 🚀

As the changes are simply written to a file in your repo, you can later tweak them however you want. You can add links, extend the information, remove irrelevant changes, etc. ✨

## Existing PRs - Running Manually

For this GitHub Action to work automatically, the workflow file has to be in the repository _before_ the PR is created, so that the PR also includes it. That's just how GitHub Actions work.

Nevertheless, if you have some PRs that were open before adding this GitHub Action to your project and you still want to use it, you can create workflows manually. It will take the PR number, and then it will do the rest automatically.

You can "dispatch" a workflow/run from the "Actions" tab:

* Select this GitHub Action with the name you used, e.g. "Latest Changes".
* Click on "Run Workflow".
* It will ask you for the PR number and do all the rest.

So, in those cases, it won't do everything automatically, you will have to manually start it and set the PR number. But it can still save you from most of the work, and from a bunch of human errors. 🤓 🎉

## Configuration

You can configure:

* `latest_changes_file`: The file to modify with the latest changes. For example: `./docs/latest-changes.rst`.
* `latest_changes_header`: The header to look for before adding a new message. for example: `# CHANGELOG \n\n`.
* `template_file`: A custom Jinja2 template file to use to generate the message, you could use this to generate a different message or to use a different format, for example, HTML instead of the default Markdown.
* `debug_logs`: Set to `'true'` to show logs with the current settings.

## Configuration example

A full example, using all the configurations, could be as follows.

You could have a custom Jinja2 template with the message to write at `./.github/workflows/release-notes.jinja2` containing:

```Jinja2
This changed: {{pr.title}}. Done by [the GitHub user {{pr.user.login}}]({{pr.user.html_url}}). Check the [Pull Request {{pr.number}} with the changes and stuff]({{pr.html_url}}). now back to code. 🤓


```

**Note**: you can use any location in your repository for the Jinja2 template.

**Tip**: The `pr` object is a [PyGitHub `PullRequest` object](https://pygithub.readthedocs.io/en/latest/github_objects/PullRequest.html), you can extract any other information you need from it.

Notice that the Jinja2 template has 2 trailing newlines. Jinja2 we need one so that the next message shows below, instead of the same line, and Jinja2 eats one 🤷, so we put 2.

Then you could have a workflow like:

```YAML
name: Latest Changes

on:
  pull_request_target:
    branches:
      - master
    types:
      - closed
  workflow_dispatch:
    inputs:
      number:
        description: PR number
        required: true

jobs:
  latest-changes:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: tiangolo/latest-changes:0.0.3
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        latest_changes_file: docs/release-notes.md
        latest_changes_header: '# Release Notes\n\n'
        template_file: ./.github/workflows/release-notes.jinja2
        debug_logs: true
```

In this custom config:

* The main branch is `master` instead of `main`.
* It uses the GitHub action directly:

```
tiangolo/latest-changes:0.0.3
```

instead of with Docker:

```
docker://tiangolo/latest-changes:0.0.3
```

**Note**: that would make every run about 1 min slower, but you can do that if you prefer it 🤷.

* It modifies the file `docs/release-notes.md` instead of the default `README.md`.
* It looks for a header in that file with:

```Markdown
# Release Notes


```

**Note**: The `latest_changes_header` is a [regular expression](https://regex101.com/). In this case it has two newlines, and the mesage will be added right after that (without adding an extra newline).

So it will generate messages like:

```Markdown
# Release Notes

* This changed: ✨ Add support for Jinja2 templates for changes notes. Done by [the GitHub user tiangolo](https://github.com/tiangolo). Check the [Pull Request 23 with the changes and stuff](https://github.com/tiangolo/latest-changes/pull/23). now back to code. 🤓
```

And that Markdown will be shown like:

> # Release Notes
>
> * This changed: ✨ Add support for Jinja2 templates for changes notes. Done by [the GitHub user tiangolo](https://github.com/tiangolo). Check the [Pull Request 23 with the changes and stuff](https://github.com/tiangolo/latest-changes/pull/23). now back to code. 🤓

**Note**: if you use the default of `### Latest Changes\n\n`, or add one like the one in this example with two newlines, this GitHub action will expect the two newlines to exist. But if your release notes are empty and the file only contains:

```Markdown
# Release Notes
```

then this action won't be able to add the first message. So, make sure the latest changes file has the format expected, for example with the two newlines:

```Markdown
# Release Notes


```

* Lastly, it will show a lot of debugging information.

## Protected Branches

If you have a protected branch (for example `main` or `master`), this action wouldn't be able to write and push the updated latest changes to it.

But it's easy to fix if you are an admin in the repo and can push directly to the protected branch.

You need to create a new GitHub access token. For example, a [personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token). You will probably need to give it `repo` permissions.

Then, in your repository, go to "Settings" -> "Secrets", and [create a new "repository secret"](https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository). Use the access token as the value, and for the name, it could be something like `ACTIONS_TOKEN`. Just remember to use the same name in the configurations shown below.

Then in your configuration, pass that token to the action `actions/checkout@v2`:

```YAML
      - uses: actions/checkout@v2
        with:
          token: ${{ secrets.ACTIONS_TOKEN }}
```

**Note**: you pass that token to the official `actions/checkout@v2`, not to this `latest-changes` action.

The complete example would look like:

```YAML
name: Latest Changes

on:
  pull_request_target:
    branches:
      - main
      # Or use the branch "master" if that's your main branch:
      # - master
    types:
      - closed
  # For manually triggering it
  workflow_dispatch:
    inputs:
      number:
        description: PR number
        required: true

jobs:
  latest-changes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          token: ${{ secrets.ACTIONS_TOKEN }}
      - uses: docker://tiangolo/latest-changes:0.0.3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

### How does it work?

By passing the custom access token to the action `actions/checkout@v2`, this action will configure `git` with those credentials.

And then when `latest-changes` runs and executes some commands with `git`, including `git push`, they will be done with your access token.

Your access token will be used to push the changes, but don't worry, the commits will not be associated with your personal user account.

`latest-changes` still configures the `git` user with:

* username: `github-actions`
* email: `github-actions@github.com`

So, the commits will still be shown as made by `github-actions`.

## Release Notes

### Latest Changes - Latest Changes 🤷

### 0.0.3

* 🚚 Update Python module name to latest_changes to avoid conflicts with any repo directory "app". PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
* 🐛 Fix default Jinja2 path in Action yaml. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).

### 0.0.2

* ✨ Check if the latest changes message was already added before adding it. PR [#35](https://github.com/tiangolo/latest-changes/pull/35) by [@tiangolo](https://github.com/tiangolo).
* 📝 Add docs for running manually, with a workflow dispatch. PR [#34](https://github.com/tiangolo/latest-changes/pull/34) by [@tiangolo](https://github.com/tiangolo).
* ✨ Refactor and add support for triggering with workflow dispatch events. PR [#32](https://github.com/tiangolo/latest-changes/pull/32) by [@tiangolo](https://github.com/tiangolo).
* 🐛 Fix basic example in README, include checkout step. PR [#31](https://github.com/tiangolo/latest-changes/pull/31) by [@tiangolo](https://github.com/tiangolo).

### 0.0.1

* 📝 Add note about updating the PR title. PR [#30](https://github.com/tiangolo/latest-changes/pull/30) by [@tiangolo](https://github.com/tiangolo).
* 🐛 Fix internal latest changes, use a custom header so it doesn't break the examples. PR [#29](https://github.com/tiangolo/latest-changes/pull/29) by [@tiangolo](https://github.com/tiangolo).
* 🐛 Fix default action config for template file. PR [#28](https://github.com/tiangolo/latest-changes/pull/28) by [@tiangolo](https://github.com/tiangolo).
* ✨ Add support for Jinja2 templates for changes notes. PR [#23](https://github.com/tiangolo/latest-changes/pull/23) by [@tiangolo](https://github.com/tiangolo).
* 🔥 Remove unnecessary note from release notes. PR [#22](https://github.com/tiangolo/latest-changes/pull/22) by [@tiangolo](https://github.com/tiangolo).
* 🔥 Remove unnecessary note from latest changes. PR [#21](https://github.com/tiangolo/latest-changes/pull/21) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Update tmate config keys. PR [#20](https://github.com/tiangolo/latest-changes/pull/20) by [@tiangolo](https://github.com/tiangolo).
* 🔒 Update tmate config for keys. PR [#19](https://github.com/tiangolo/latest-changes/pull/19) by [@tiangolo](https://github.com/tiangolo).
* ✏️ Fix incorrect URL. PR [#18](https://github.com/tiangolo/latest-changes/pull/18) by [@tiangolo](https://github.com/tiangolo).
* 🔒 Try to secure tmate. PR [#17](https://github.com/tiangolo/latest-changes/pull/17) by [@tiangolo](https://github.com/tiangolo).
* 📝 Update release notes URLs. PR [#16](https://github.com/tiangolo/latest-changes/pull/16) by [@tiangolo](https://github.com/tiangolo).

## License

This project is licensed under the terms of the MIT license.
