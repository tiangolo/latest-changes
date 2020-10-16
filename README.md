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
      - uses: docker://tiangolo/latest-changes:0.0.1
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

**Note**: you can also use the GitHub action directly intead of with Docker, but that would take an extra minute:

```YAML
      # - uses: docker://tiangolo/latest-changes:0.0.1
      # This is slower but also works
      - uses: tiangolo/latest-changes:0.0.1
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

You can see an example of how it works in this same file, at the bottom, in [Latest Changes](#latest-changes-1).

* Then it will commit the changes, and push them to your repo. 🚀

As the changes are simply written to a file in your repo, you can later tweak them however you want. You can add links, extend the information, remove irrelevant changes, etc. ✨

## Configuration

You can configure:

* `latest_changes_file`: The file to modify with the latest changes. For example: `./docs/latest-changes.rst`.
* `latest_changes_header`: The header to look for before adding a new message. for example: `# CHANGELOG \n\n`.
* `template_file`: A custom Jinja2 template file to use to generate the message, you could use this to generate a different message or to use a different format, for example, HTML instead of the default Markdown.
* `debug_logs`: Set to `'true'` to show lots of logs with the current config and PR event objects. It can be useful while creating a custom template.

## Configuration example

A full example, using all the configurations, could be as follows.

You could have a custom Jinja2 template with the message to write at `./.github/workflows/release-notes.jinja2` containing:

```Jinja2
This changed: {{github_event.pull_request.title}}. Done by [the GitHub user {{github_event.pull_request.user.login}}]({{github_event.pull_request.user.html_url}}). Check the [Pull Request {{github_event.pull_request.number}} with the changes and stuff]({{github_event.pull_request.html_url}}). now back to code. 🤓


```

**Note**: you can use any location in your repository for the Jinja2 template.

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
    - uses: tiangolo/latest-changes:0.0.1
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
tiangolo/latest-changes:0.0.1
```

instead of with Docker:

```
docker://tiangolo/latest-changes:0.0.1
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

## Release Notes

### Latest Changes - Latest Changes 🤷

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
