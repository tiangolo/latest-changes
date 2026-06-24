# Release Notes

## Latest Changes

* 👷 Update Dependabot. PR [#92](https://github.com/tiangolo/latest-changes/pull/92) by [@tiangolo](https://github.com/tiangolo).

### Features

* ✨ Add support for skip labels, useful for making a PR with the actual release. PR [#96](https://github.com/tiangolo/latest-changes/pull/96) by [@tiangolo](https://github.com/tiangolo).

### Docs

* 📝 Add docs explaining skip labels. PR [#99](https://github.com/tiangolo/latest-changes/pull/99) by [@tiangolo](https://github.com/tiangolo).

### Internal

* ♻️ Migrate from plain pip to uv. PR [#110](https://github.com/tiangolo/latest-changes/pull/110) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update issue-manager to 0.7.1. PR [#109](https://github.com/tiangolo/latest-changes/pull/109) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Update issue-manager to 0.7.0. PR [#108](https://github.com/tiangolo/latest-changes/pull/108) by [@tiangolo](https://github.com/tiangolo).
* 🔒️ Add zizmor workflow security checks. PR [#106](https://github.com/tiangolo/latest-changes/pull/106) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Group Dependabot updates. PR [#105](https://github.com/tiangolo/latest-changes/pull/105) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Update Dependabot ecosystem coverage. PR [#102](https://github.com/tiangolo/latest-changes/pull/102) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump docker/login-action from 4.1.0 to 4.2.0 in the github-actions group across 1 directory. PR [#101](https://github.com/tiangolo/latest-changes/pull/101) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Add workflow dispatch to publish the Docker image. PR [#97](https://github.com/tiangolo/latest-changes/pull/97) by [@tiangolo](https://github.com/tiangolo).
* 🔥 Remove config files now in central GitHub repo. PR [#95](https://github.com/tiangolo/latest-changes/pull/95) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump the python-packages group across 1 directory with 2 updates. PR [#94](https://github.com/tiangolo/latest-changes/pull/94) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump the github-actions group across 1 directory with 6 updates. PR [#93](https://github.com/tiangolo/latest-changes/pull/93) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Tweak permissions for latest-changes action. PR [#98](https://github.com/tiangolo/latest-changes/pull/98) by [@tiangolo](https://github.com/tiangolo).

## 0.5.0

### Features

* ✨ Add support for skipping release PRs with `skip_labels`, with `release` skipped by default.

### Refactors

* 🔥 Remove unused `models.py` file. PR [#90](https://github.com/tiangolo/latest-changes/pull/90) by [@tiangolo](https://github.com/tiangolo).

### Docs

* 📝 Add permissions needed for private repos. PR [#89](https://github.com/tiangolo/latest-changes/pull/89) by [@tiangolo](https://github.com/tiangolo).

## 0.4.1

### Fixes

* 🐛 Fix error out when running out of trials. PR [#86](https://github.com/tiangolo/latest-changes/pull/86) by [@tiangolo](https://github.com/tiangolo).

### Docs

* 📝 Tweak docs with new label infra. PR [#80](https://github.com/tiangolo/latest-changes/pull/80) by [@tiangolo](https://github.com/tiangolo).

### Internal

* ⬆ Bump actions/setup-python from 5 to 6. PR [#82](https://github.com/tiangolo/latest-changes/pull/82) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/upload-artifact from 4 to 5. PR [#84](https://github.com/tiangolo/latest-changes/pull/84) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/issue-manager from 0.5.1 to 0.6.0. PR [#83](https://github.com/tiangolo/latest-changes/pull/83) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/checkout from 4 to 5. PR [#81](https://github.com/tiangolo/latest-changes/pull/81) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.4.0

### Features

* ✨ Add new default `infra` label. PR [#79](https://github.com/tiangolo/latest-changes/pull/79) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Update GitHub Actions bot user configuration. PR [#78](https://github.com/tiangolo/latest-changes/pull/78) by [@malvex](https://github.com/malvex).

### Upgrades

* ⬆ Update httpx requirement from <0.28.0,>=0.15.5 to >=0.15.5,<0.29.0. PR [#77](https://github.com/tiangolo/latest-changes/pull/77) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.3.2

### Features

* ✨ Prevent CI workflows from running on a latest changes commit, add `[skip ci]` to commit message. PR [#76](https://github.com/tiangolo/latest-changes/pull/76) by [@patrick91](https://github.com/patrick91).

### Refactors

* ♻️ Refactor usage of internal `number_of_trials` variable, it was not being used, fix typo. PR [#75](https://github.com/tiangolo/latest-changes/pull/75) by [@nghiahsgs](https://github.com/nghiahsgs).

### Docs

* 📝 Tweak and fix tag to use. PR [#71](https://github.com/tiangolo/latest-changes/pull/71) by [@tiangolo](https://github.com/tiangolo).

### Internal

* ⬆ Bump tiangolo/issue-manager from 0.5.0 to 0.5.1. PR [#74](https://github.com/tiangolo/latest-changes/pull/74) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/build-push-action from 5 to 6. PR [#72](https://github.com/tiangolo/latest-changes/pull/72) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update `issue-manager.yml`. PR [#73](https://github.com/tiangolo/latest-changes/pull/73) by [@tiangolo](https://github.com/tiangolo).

## 0.3.1

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

### Fixes

* 🐛 Fix race condition with retries, when more than one latest-changes is running. PR [#69](https://github.com/tiangolo/latest-changes/pull/69) by [@tiangolo](https://github.com/tiangolo).

### Refactors

* ♻️ Make using the native GitHub Action re-use the existing Docker image instead of building from scratch. PR [#70](https://github.com/tiangolo/latest-changes/pull/70) by [@tiangolo](https://github.com/tiangolo).

### Docs

* 📝 Update README docs for token permissions. PR [#68](https://github.com/tiangolo/latest-changes/pull/68) by [@tiangolo](https://github.com/tiangolo).

### Internal

* ⬆ Update httpx requirement from <0.26.0,>=0.15.5 to >=0.15.5,<0.28.0. PR [#65](https://github.com/tiangolo/latest-changes/pull/65) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/cache from 3 to 4. PR [#64](https://github.com/tiangolo/latest-changes/pull/64) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/upload-artifact from 3 to 4. PR [#61](https://github.com/tiangolo/latest-changes/pull/61) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/setup-python from 4 to 5. PR [#60](https://github.com/tiangolo/latest-changes/pull/60) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Add GitHub templates for discussions and issues, and security policy. PR [#67](https://github.com/tiangolo/latest-changes/pull/67) by [@alejsdev](https://github.com/alejsdev).

## 0.3.0

### Features

* ✨ Add retries to handle race conditions. PR [#63](https://github.com/tiangolo/latest-changes/pull/63) by [@tiangolo](https://github.com/tiangolo).

## 0.2.1

### Fixes

* 🐛 Detect if there's a second level header after the release content, to support the first change in a README with a last section for a license. PR [#59](https://github.com/tiangolo/latest-changes/pull/59) by [@tiangolo](https://github.com/tiangolo).

## 0.2.0

### Refactors

* ♻️ Separate label header prefix from label text with `label_header_prefix`, this allows re-using the default labels while only changing the header level. PR [#58](https://github.com/tiangolo/latest-changes/pull/58) by [@tiangolo](https://github.com/tiangolo).

## 0.1.1

### Fixes

* 🐛 Fix handling multiple section headers. PR [#57](https://github.com/tiangolo/latest-changes/pull/57) by [@tiangolo](https://github.com/tiangolo).

### Upgrades

* ⬆ Update httpx requirement from <0.16.0,>=0.15.5 to >=0.15.5,<0.26.0. PR [#54](https://github.com/tiangolo/latest-changes/pull/54) by [@dependabot[bot]](https://github.com/apps/dependabot).

### Docs

* ✏️ Fix typo in syntax for using the GitHub Action tag directly (instead of with Docker) in README. PR [#39](https://github.com/tiangolo/latest-changes/pull/39) by [@art049](https://github.com/art049).

### Internal

* ⬆ Bump docker/setup-buildx-action from 1 to 3. PR [#53](https://github.com/tiangolo/latest-changes/pull/53) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/build-push-action from 2 to 5. PR [#52](https://github.com/tiangolo/latest-changes/pull/52) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/login-action from 1 to 3. PR [#51](https://github.com/tiangolo/latest-changes/pull/51) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.1.0

### Features

* ♻️ Use Docker slim to reduce the time to run in half, from 33s to 16s. PR [#55](https://github.com/tiangolo/latest-changes/pull/55) by [@tiangolo](https://github.com/tiangolo).
* ✨ Add support for labels and section headers (features, fixes, etc.). PR [#48](https://github.com/tiangolo/latest-changes/pull/48) by [@tiangolo](https://github.com/tiangolo).
* 🚀 Publish amd64 and arm64 versions, and publish to GitHub Container Registry, fix git in containers. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

### Upgrades

* ⬆️ Upgrade GitHub Action checkout and references to it. PR [#49](https://github.com/tiangolo/latest-changes/pull/49) by [@tiangolo](https://github.com/tiangolo).

## Docs

* 📝 Add docs for using latest-changes with protected branches. PR [#43](https://github.com/tiangolo/latest-changes/pull/43) by [@tiangolo](https://github.com/tiangolo).

### Internal

* 👷 Do not push the slim branch for debugging. PR [#56](https://github.com/tiangolo/latest-changes/pull/56) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update CI, Dependabot, funding. PR [#50](https://github.com/tiangolo/latest-changes/pull/50) by [@tiangolo](https://github.com/tiangolo).
* 🔥 Remove config pushing to custom branch for debugging. PR [#47](https://github.com/tiangolo/latest-changes/pull/47) by [@tiangolo](https://github.com/tiangolo).

### Internal

* 👷 Update CI, Dependabot, funding. PR [#50](https://github.com/tiangolo/latest-changes/pull/50) by [@tiangolo](https://github.com/tiangolo).

## 0.0.3

* 🚚 Update Python module name to latest_changes to avoid conflicts with any repo directory "app". PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
* 🐛 Fix default Jinja2 path in Action yaml. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).

## 0.0.2

* ✨ Check if the latest changes message was already added before adding it. PR [#35](https://github.com/tiangolo/latest-changes/pull/35) by [@tiangolo](https://github.com/tiangolo).
* 📝 Add docs for running manually, with a workflow dispatch. PR [#34](https://github.com/tiangolo/latest-changes/pull/34) by [@tiangolo](https://github.com/tiangolo).
* ✨ Refactor and add support for triggering with workflow dispatch events. PR [#32](https://github.com/tiangolo/latest-changes/pull/32) by [@tiangolo](https://github.com/tiangolo).
* 🐛 Fix basic example in README, include checkout step. PR [#31](https://github.com/tiangolo/latest-changes/pull/31) by [@tiangolo](https://github.com/tiangolo).

## 0.0.1

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
