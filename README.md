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
      - uses: actions/checkout@v4
      - uses: tiangolo/latest-changes@0.4.0
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

In this minimal example, it uses all the default configurations.

After merging a PR to the main branch, it will:

* Find a file `README.md`
* Inside of that file, find a "header" with the text:

```Markdown
### Latest Changes
```

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

## Using Labels

You can also use labels in the PRs to configure which sections they should show up in the release notes.

By default, it will use these labels and headers:

* `breaking`: `Breaking Changes`
* `security`: `Security Fixes`
* `feature`: `Features`
* `bug`: `Fixes`
* `refactor`: `Refactors`
* `upgrade`: `Upgrades`
* `docs`: `Docs`
* `lang-all`: `Translations`
* `infra`: `Infrastructure`
* `internal`: `Internal`

So, if you have a PR with a label `feature`, by default, it will show up in the section about features, like:

> ### Latest Changes
>
> #### Features
>
> * ✨ Add support for Jinja2 templates for latest changes messages. PR [#23](https://github.com/tiangolo/latest-changes/pull/23) by [@tiangolo](https://github.com/tiangolo).

You can configure the labels and headers used in the GitHub Action `labels` workflow configuration, and you can configure the header prefix, by default `#### `.

Read more about it in the section about configuration.

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
* `latest_changes_header`: The header to look for before adding a new message. for example: `# CHANGELOG`.
* `template_file`: A custom Jinja2 template file to use to generate the message, you could use this to generate a different message or to use a different format, for example, HTML instead of the default Markdown.
* `end_regex`: A RegEx string that marks the end of this release, so it normally matches the start of the header of the next release section, normally the same header level as `latest_changes_header`, so, if the `latest_changes_header` is `### Latest Changes`, the content for the next release below is probably something like `### 0.2.0`, then the `end_regex` should be `^### `. This is used to limit the content updated as this will read the existing sub sections and possibly update them using the labels configuration and the labels in the PR. By default it is `(^### .*)|(^## .*)` to detect a possible next header, e.g. for the license.
* `debug_logs`: Set to `'true'` to show logs with the current settings.
* `labels`: A JSON array of JSON objects with a `label` that you would put in each PR and the `header` that would be used in the release notes. See the example below.
* `label_header_prefix`: A prefix to put before each label's header. This is also used to detect where the next label header starts. By default it is `#### `, so the headers will look like `#### Features`.

### Configuring Labels

The `labels` configuration takes a JSON array of JSON objects that contain a key `label` with the label you would add to each PR, and a key `header` with the header text that should be added to the release notes for that label.

The order is important, the first label from the list that is found in your PR is the one that will be used. So, if you have a PR that has both labels `feature` and `bug`, if you use the default configuration, it will show up in the section for features, as that comes first. If you want it to show up in the section for bugs you would need to change the order of the list of this configuration to have `bug` first.

Note that this JSON has to be passed as a string because that's the only thing that GitHub Actions support for configurations.

If you want to keep the same default labels but change the header level, so, add or remove hash symbols, you can set the `label_header_prefix` configuration. You could also use it to set a different header prefix, but the common case is changing the section header level.

## Configuration example

A full example, using all the configurations, could be as follows.

You could have a custom Jinja2 template with the message to write at `./.github/workflows/release-notes.jinja2` containing:

```Jinja2
This changed: {{pr.title}}. Done by [the GitHub user {{pr.user.login}}]({{pr.user.html_url}}). Check the [Pull Request {{pr.number}} with the changes and stuff]({{pr.html_url}}). now back to code. 🤓
```

**Note**: you can use any location in your repository for the Jinja2 template.

**Tip**: The `pr` object is a [PyGitHub `PullRequest` object](https://pygithub.readthedocs.io/en/latest/github_objects/PullRequest.html), you can extract any other information you need from it.

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
    - uses: tiangolo/latest-changes@0.4.0
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        latest_changes_file: docs/release-notes.md
        latest_changes_header: '# Release Notes'
        template_file: ./.github/workflows/release-notes.jinja2
        # The next release will start with this RegEx, for example "## 0.2.0"
        end_regex: '^## '
        debug_logs: true
        # Here we use a yaml multiline string to pass a JSON array of JSON objects in a more readable way
        # In these case we use the same default labels and the same header titles, but the headers use 3 hash symbols instead of the default of 4
        # We also add a custom last label "egg" for PRs with easter eggs.
        labels: >
          [
            {"label": "breaking", "header": "Breaking Changes"},
            {"label": "security", "header": "Security Fixes"},
            {"label": "feature", "header": "Features"},
            {"label": "bug", "header": "Fixes"},
            {"label": "refactor", "header": "Refactors"},
            {"label": "upgrade", "header": "Upgrades"},
            {"label": "docs", "header": "Docs"},
            {"label": "lang-all", "header": "Translations"},
            {"label": "infra", "header": "Infrastructure"},
            {"label": "internal", "header": "Internal"},
            {"label": "egg", "header": "Easter Eggs"}
          ]
        # This will be added to the start of each label's header and
        # will be used to detect existing label headers
        label_header_prefix: '### '
```

In this custom config:

* The main branch is `master` instead of `main`.
* It modifies the file `docs/release-notes.md` instead of the default `README.md`.
* It looks for a header in that file with:

```Markdown
# Release Notes
```

**Note**: The `latest_changes_header` is a [regular expression](https://regex101.com/).

So it will generate messages like:

```Markdown
# Release Notes

* This changed: ✨ Add support for Jinja2 templates for changes notes. Done by [the GitHub user tiangolo](https://github.com/tiangolo). Check the [Pull Request 23 with the changes and stuff](https://github.com/tiangolo/latest-changes/pull/23). now back to code. 🤓
```

And that Markdown will be shown like:

> # Release Notes
>
> * This changed: ✨ Add support for Jinja2 templates for changes notes. Done by [the GitHub user tiangolo](https://github.com/tiangolo). Check the [Pull Request 23 with the changes and stuff](https://github.com/tiangolo/latest-changes/pull/23). now back to code. 🤓

* It will expect that the end of the content starts with the regular expression `^## `, normally because that's how the next release starts. This will be used to organize the content in the sections with the headers from the `labels` configuration.

* It will show a lot of debugging information.

* It will use the same default labels and headers plus another one for easter eggs.

* It will show those section headers from labels with 3 hash symbols instead of the default of 4. And it will also find any existing header checking for that prefix (it will use a regular expression like `^### `).

## Protected Branches

If you have a protected branch (for example `main` or `master`), this action wouldn't be able to write and push the updated latest changes to it.

But it's easy to fix if you are an admin in the repo and can push directly to the protected branch.

You need to create a new GitHub access token. For example, a [personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).

You can create a "**Fine-grained token**" with "**Contents**" permissions for "**Read and write**" access.

Then, in your repository, go to "Settings" -> "Secrets", and [create a new "repository secret"](https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository). Use the access token as the value, and for the name, it could be something like `ACTIONS_TOKEN`. Just remember to use the same name in the configurations shown below.

Then in your configuration, pass that token to the action `actions/checkout@v4`:

```YAML
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.ACTIONS_TOKEN }}
```

**Note**: you pass that token to the official `actions/checkout@v4`, not to this `latest-changes` action.

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
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.ACTIONS_TOKEN }}
      - uses: tiangolo/latest-changes@0.4.0
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

### How does it work?

By passing the custom access token to the action `actions/checkout@v4`, this action will configure `git` with those credentials.

And then when `latest-changes` runs and executes some commands with `git`, including `git push`, they will be done with your access token.

Your access token will be used to push the changes, but don't worry, the commits will not be associated with your personal user account.

`latest-changes` still configures the `git` user with:

* username: `github-actions`
* email: `github-actions@github.com`

So, the commits will still be shown as made by `github-actions`.

## Release Notes

### Latest Changes - Latest Changes 🤷

#### Docs

* 📝 Tweak docs with new label infra. PR [#80](https://github.com/tiangolo/latest-changes/pull/80) by [@tiangolo](https://github.com/tiangolo).

#### Internal

* ⬆ Bump actions/setup-python from 5 to 6. PR [#82](https://github.com/tiangolo/latest-changes/pull/82) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/upload-artifact from 4 to 5. PR [#84](https://github.com/tiangolo/latest-changes/pull/84) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/issue-manager from 0.5.1 to 0.6.0. PR [#83](https://github.com/tiangolo/latest-changes/pull/83) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/checkout from 4 to 5. PR [#81](https://github.com/tiangolo/latest-changes/pull/81) by [@dependabot[bot]](https://github.com/apps/dependabot).

### 0.4.0

#### Features

* ✨ Add new default `infra` label. PR [#79](https://github.com/tiangolo/latest-changes/pull/79) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Update GitHub Actions bot user configuration. PR [#78](https://github.com/tiangolo/latest-changes/pull/78) by [@malvex](https://github.com/malvex).

#### Upgrades

* ⬆ Update httpx requirement from <0.28.0,>=0.15.5 to >=0.15.5,<0.29.0. PR [#77](https://github.com/tiangolo/latest-changes/pull/77) by [@dependabot[bot]](https://github.com/apps/dependabot).

### 0.3.2

#### Features

* ✨ Prevent CI workflows from running on a latest changes commit, add `[skip ci]` to commit message. PR [#76](https://github.com/tiangolo/latest-changes/pull/76) by [@patrick91](https://github.com/patrick91).

#### Refactors

* ♻️ Refactor usage of internal `number_of_trials` variable, it was not being used, fix typo. PR [#75](https://github.com/tiangolo/latest-changes/pull/75) by [@nghiahsgs](https://github.com/nghiahsgs).

#### Docs

* 📝 Tweak and fix tag to use. PR [#71](https://github.com/tiangolo/latest-changes/pull/71) by [@tiangolo](https://github.com/tiangolo).

#### Internal

* ⬆ Bump tiangolo/issue-manager from 0.5.0 to 0.5.1. PR [#74](https://github.com/tiangolo/latest-changes/pull/74) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/build-push-action from 5 to 6. PR [#72](https://github.com/tiangolo/latest-changes/pull/72) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update `issue-manager.yml`. PR [#73](https://github.com/tiangolo/latest-changes/pull/73) by [@tiangolo](https://github.com/tiangolo).

### 0.3.1

Now you can (and should) use the native GitHub Action directly, as in:

```yaml
...
      - uses: tiangolo/latest-changes@0.3.1
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

instead of using the Docker image:

```yaml
...
      - uses: docker://tiangolo/latest-changes:0.3.1
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

This way, Dependabot will be able to send you PRs updating the version automatically. 🚀

The internal code and build setup was refactored so that the native GitHub Action still re-uses a prebuilt Docker image, so it's still fast. 😎

#### Fixes

* 🐛 Fix race condition with retries, when more than one latest-changes is running. PR [#69](https://github.com/tiangolo/latest-changes/pull/69) by [@tiangolo](https://github.com/tiangolo).

#### Refactors

* ♻️ Make using the native GitHub Action re-use the existing Docker image instead of building from scratch. PR [#70](https://github.com/tiangolo/latest-changes/pull/70) by [@tiangolo](https://github.com/tiangolo).

#### Docs

* 📝 Update README docs for token permissions. PR [#68](https://github.com/tiangolo/latest-changes/pull/68) by [@tiangolo](https://github.com/tiangolo).

#### Internal

* ⬆ Update httpx requirement from <0.26.0,>=0.15.5 to >=0.15.5,<0.28.0. PR [#65](https://github.com/tiangolo/latest-changes/pull/65) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/cache from 3 to 4. PR [#64](https://github.com/tiangolo/latest-changes/pull/64) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/upload-artifact from 3 to 4. PR [#61](https://github.com/tiangolo/latest-changes/pull/61) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/setup-python from 4 to 5. PR [#60](https://github.com/tiangolo/latest-changes/pull/60) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Add GitHub templates for discussions and issues, and security policy. PR [#67](https://github.com/tiangolo/latest-changes/pull/67) by [@alejsdev](https://github.com/alejsdev).

### 0.3.0

#### Features

* ✨ Add retries to handle race conditions. PR [#63](https://github.com/tiangolo/latest-changes/pull/63) by [@tiangolo](https://github.com/tiangolo).

### 0.2.1

#### Fixes

* 🐛 Detect if there's a second level header after the release content, to support the first change in a README with a last section for a license. PR [#59](https://github.com/tiangolo/latest-changes/pull/59) by [@tiangolo](https://github.com/tiangolo).

### 0.2.0

#### Refactors

* ♻️ Separate label header prefix from label text with `label_header_prefix`, this allows re-using the default labels while only changing the header level. PR [#58](https://github.com/tiangolo/latest-changes/pull/58) by [@tiangolo](https://github.com/tiangolo).

### 0.1.1

#### Fixes

* 🐛 Fix handling multiple section headers. PR [#57](https://github.com/tiangolo/latest-changes/pull/57) by [@tiangolo](https://github.com/tiangolo).

#### Upgrades

* ⬆ Update httpx requirement from <0.16.0,>=0.15.5 to >=0.15.5,<0.26.0. PR [#54](https://github.com/tiangolo/latest-changes/pull/54) by [@dependabot[bot]](https://github.com/apps/dependabot).

#### Docs

* ✏️ Fix typo in syntax for using the GitHub Action tag directly (instead of with Docker) in README. PR [#39](https://github.com/tiangolo/latest-changes/pull/39) by [@art049](https://github.com/art049).

#### Internal

* ⬆ Bump docker/setup-buildx-action from 1 to 3. PR [#53](https://github.com/tiangolo/latest-changes/pull/53) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/build-push-action from 2 to 5. PR [#52](https://github.com/tiangolo/latest-changes/pull/52) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/login-action from 1 to 3. PR [#51](https://github.com/tiangolo/latest-changes/pull/51) by [@dependabot[bot]](https://github.com/apps/dependabot).

### 0.1.0

#### Features

* ♻️ Use Docker slim to reduce the time to run in half, from 33s to 16s. PR [#55](https://github.com/tiangolo/latest-changes/pull/55) by [@tiangolo](https://github.com/tiangolo).
* ✨ Add support for labels and section headers (features, fixes, etc.). PR [#48](https://github.com/tiangolo/latest-changes/pull/48) by [@tiangolo](https://github.com/tiangolo).
* 🚀 Publish amd64 and arm64 versions, and publish to GitHub Container Registry, fix git in containers. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

#### Upgrades

* ⬆️ Upgrade GitHub Action checkout and references to it. PR [#49](https://github.com/tiangolo/latest-changes/pull/49) by [@tiangolo](https://github.com/tiangolo).

### Docs

* 📝 Add docs for using latest-changes with protected branches. PR [#43](https://github.com/tiangolo/latest-changes/pull/43) by [@tiangolo](https://github.com/tiangolo).

#### Internal

* 👷 Do not push the slim branch for debugging. PR [#56](https://github.com/tiangolo/latest-changes/pull/56) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update CI, Dependabot, funding. PR [#50](https://github.com/tiangolo/latest-changes/pull/50) by [@tiangolo](https://github.com/tiangolo).
* 🔥 Remove config pushing to custom branch for debugging. PR [#47](https://github.com/tiangolo/latest-changes/pull/47) by [@tiangolo](https://github.com/tiangolo).

#### Internal

* 👷 Update CI, Dependabot, funding. PR [#50](https://github.com/tiangolo/latest-changes/pull/50) by [@tiangolo](https://github.com/tiangolo).

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
