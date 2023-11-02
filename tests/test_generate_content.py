import inspect

import pytest

from latest_changes.main import (
    Settings,
    TemplateDataPR,
    TemplateDataUser,
    generate_content,
)


def test_no_sections():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    * 🔥 Remove config. PR [#47](https://github.com/tiangolo/latest-changes/pull/47) by [@tiangolo](https://github.com/tiangolo).
    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    * 📝 Add docs. PR [#43](https://github.com/tiangolo/latest-changes/pull/43) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(content=content, settings=settings, pr=pr, labels=[])
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).
    * 🔥 Remove config. PR [#47](https://github.com/tiangolo/latest-changes/pull/47) by [@tiangolo](https://github.com/tiangolo).
    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    * 📝 Add docs. PR [#43](https://github.com/tiangolo/latest-changes/pull/43) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_before_release():
    raw_content = """
    ## Release Notes

    ### Latest Changes
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(content=content, settings=settings, pr=pr, labels=[])
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).

    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_existing_labels_no_label():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    #### Features

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(content=content, settings=settings, pr=pr, labels=[])
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).

    #### Features

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_existing_labels_same_label():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    #### Features

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(
        content=content, settings=settings, pr=pr, labels=["feature"]
    )
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    #### Features

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).
    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_existing_label_other_label():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    #### Fixes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(
        content=content, settings=settings, pr=pr, labels=["feature"]
    )
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    #### Features

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).

    #### Fixes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_existing_label_secondary_label():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    #### Features

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(
        content=content, settings=settings, pr=pr, labels=["bug"]
    )
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    #### Features

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

    #### Fixes

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_no_existing_label_label():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(
        content=content, settings=settings, pr=pr, labels=["feature"]
    )
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

    #### Features

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_no_existing_label_release_label_label():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    #### Features

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(
        content=content, settings=settings, pr=pr, labels=["feature"]
    )
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

    #### Features

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    #### Features

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_custom_label_label():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    #### Custom

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(
        content=content, settings=settings, pr=pr, labels=["feature"]
    )
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    #### Custom
    
    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

    #### Features

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_sectionless_content_label():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

    #### Fixes

    * 🔥 Remove config. PR [#47](https://github.com/tiangolo/latest-changes/pull/47) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(
        content=content, settings=settings, pr=pr, labels=["feature"]
    )
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

    #### Features

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).

    #### Fixes

    * 🔥 Remove config. PR [#47](https://github.com/tiangolo/latest-changes/pull/47) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_content_above_latest_changes():
    raw_content = """
    ## Release Notes

    Here's some content.

    ## Some Header

    * Here's a list.

    #### Features

    These are not release notes.

    ### Latest Changes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

    #### Fixes

    * 🔥 Remove config. PR [#47](https://github.com/tiangolo/latest-changes/pull/47) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(
        content=content, settings=settings, pr=pr, labels=["feature"]
    )
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    Here's some content.

    ## Some Header

    * Here's a list.

    #### Features

    These are not release notes.

    ### Latest Changes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

    #### Features

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).

    #### Fixes

    * 🔥 Remove config. PR [#47](https://github.com/tiangolo/latest-changes/pull/47) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_multiple_labels():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    #### Fixes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(
        content=content, settings=settings, pr=pr, labels=["bug", "feature"]
    )
    assert new_content == inspect.cleandoc(
        """
    ## Release Notes

    ### Latest Changes

    #### Features

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).

    #### Fixes

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
    )


def test_no_latest_changes_raises():
    raw_content = """
    ## Release Notes

    Here's some content.

    ## Some Header

    * Here's a list.

    #### Features

    These are not release notes.

    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).

    #### Fixes

    * 🔥 Remove config. PR [#47](https://github.com/tiangolo/latest-changes/pull/47) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    with pytest.raises(RuntimeError):
        generate_content(content=content, settings=settings, pr=pr, labels=["feature"])


def test_changes_exist_raises():
    raw_content = """
    ## Release Notes

    ### Latest Changes

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).
    * 🔥 Remove config. PR [#47](https://github.com/tiangolo/latest-changes/pull/47) by [@tiangolo](https://github.com/tiangolo).
    * 🚀 Publish amd64 and arm64 versions. PR [#46](https://github.com/tiangolo/latest-changes/pull/46) by [@tiangolo](https://github.com/tiangolo).
    * 📝 Add docs. PR [#43](https://github.com/tiangolo/latest-changes/pull/43) by [@tiangolo](https://github.com/tiangolo).
    
    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    with pytest.raises(RuntimeError):
        generate_content(content=content, settings=settings, pr=pr, labels=["feature"])
