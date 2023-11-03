import inspect
from typing import Any, cast

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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
            """
    ## Release Notes

    ### Latest Changes

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).

    ### 0.0.3

    * 🚚 Update Python module name. PR [#37](https://github.com/tiangolo/latest-changes/pull/37) by [@tiangolo](https://github.com/tiangolo).
    * 🐛 Fix default Jinja2 path. PR [#38](https://github.com/tiangolo/latest-changes/pull/38) by [@tiangolo](https://github.com/tiangolo).
    """
        )
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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
    assert (
        new_content
        == inspect.cleandoc(
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
        + "\n"
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


def test_multiple_header_sections():
    raw_content = """
    # Release Notes

    ## Latest Changes

    ### Refactors

    * ✏️ Tweak docstrings format. PR [#50](https://github.com/tiangolo/asyncer/pull/50) by [@realFranco](https://github.com/realFranco).

    ### Docs

    * 👷 Upgrade CI for docs. PR [#78](https://github.com/tiangolo/asyncer/pull/78) by [@tiangolo](https://github.com/tiangolo).
    * 🛠️ Tweak internal CI actions, add `--no-cache-dir` at `Dockfile` files. PR [#52](https://github.com/tiangolo/asyncer/pull/52) by [@realFranco](https://github.com/realFranco).
    * 📝 Update help Asyncer docs. PR [#65](https://github.com/tiangolo/asyncer/pull/65) by [@tiangolo](https://github.com/tiangolo).

    ### Internal

    * 🔨 Update dev scripts. PR [#95](https://github.com/tiangolo/asyncer/pull/95) by [@tiangolo](https://github.com/tiangolo).
    * ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#83](https://github.com/tiangolo/asyncer/pull/83) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
    * ⬆ Bump actions/checkout from 3 to 4. PR [#85](https://github.com/tiangolo/asyncer/pull/85) by [@dependabot[bot]](https://github.com/apps/dependabot).

    ## 0.0.2

    ### Features

    * ✨ Add compatibility with the next (unreleased) version of AnyIO (4.x.x), with `get_asynclib` utility. PR [#48](https://github.com/tiangolo/asyncer/pull/48) by [@tiangolo](https://github.com/tiangolo).

    ### Docs

    * ✏ Fix link to FastAPI and Friends newsletter. PR [#13](https://github.com/tiangolo/asyncer/pull/13) by [@JonasKs](https://github.com/JonasKs).
    * ✏ Fix typo in `docs/tutorial/first-steps.md`, from `asyncio` to `anyio`. PR [#11](https://github.com/tiangolo/asyncer/pull/11) by [@windson](https://github.com/windson).
    * ✏️ Fix broken link in README and index. PR [#9](https://github.com/tiangolo/asyncer/pull/9) by [@vrslev](https://github.com/vrslev).

    ### Internal

    * 🔧 Update mypy config, use `strict = true` instead of manual configs. PR [#38](https://github.com/tiangolo/asyncer/pull/38) by [@michaeloliverx](https://github.com/michaeloliverx).
    * ➕ Add extra dev dependencies for MkDocs Material. PR [#49](https://github.com/tiangolo/asyncer/pull/49) by [@tiangolo](https://github.com/tiangolo).
    * ⬆ Update mypy requirement from ^0.930 to ^0.971. PR [#34](https://github.com/tiangolo/asyncer/pull/34) by [@dependabot[bot]](https://github.com/apps/dependabot).

    ## 0.0.1

    * First release. 🎉

    ### Docs

    * ✏ Fix typo in index and README. PR [#4](https://github.com/tiangolo/asyncer/pull/4) by [@sanders41](https://github.com/sanders41).

    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
        input_latest_changes_header="## Latest Changes",
        input_end_regex="^## ",
        input_labels=cast(
            Any,
            [
                {"label": "breaking", "header": "Breaking Changes"},
                {"label": "security", "header": "Security Fixes"},
                {"label": "feature", "header": "Features"},
                {"label": "bug", "header": "Fixes"},
                {"label": "refactor", "header": "Refactors"},
                {"label": "upgrade", "header": "Upgrades"},
                {"label": "docs", "header": "Docs"},
                {"label": "lang-all", "header": "Translations"},
                {"label": "internal", "header": "Internal"},
            ],
        ),
        input_label_header_prefix="### ",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(content=content, settings=settings, pr=pr, labels=[])
    assert (
        new_content
        == inspect.cleandoc(
            """
    # Release Notes

    ## Latest Changes

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).

    ### Refactors

    * ✏️ Tweak docstrings format. PR [#50](https://github.com/tiangolo/asyncer/pull/50) by [@realFranco](https://github.com/realFranco).

    ### Docs

    * 👷 Upgrade CI for docs. PR [#78](https://github.com/tiangolo/asyncer/pull/78) by [@tiangolo](https://github.com/tiangolo).
    * 🛠️ Tweak internal CI actions, add `--no-cache-dir` at `Dockfile` files. PR [#52](https://github.com/tiangolo/asyncer/pull/52) by [@realFranco](https://github.com/realFranco).
    * 📝 Update help Asyncer docs. PR [#65](https://github.com/tiangolo/asyncer/pull/65) by [@tiangolo](https://github.com/tiangolo).

    ### Internal

    * 🔨 Update dev scripts. PR [#95](https://github.com/tiangolo/asyncer/pull/95) by [@tiangolo](https://github.com/tiangolo).
    * ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#83](https://github.com/tiangolo/asyncer/pull/83) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
    * ⬆ Bump actions/checkout from 3 to 4. PR [#85](https://github.com/tiangolo/asyncer/pull/85) by [@dependabot[bot]](https://github.com/apps/dependabot).

    ## 0.0.2

    ### Features

    * ✨ Add compatibility with the next (unreleased) version of AnyIO (4.x.x), with `get_asynclib` utility. PR [#48](https://github.com/tiangolo/asyncer/pull/48) by [@tiangolo](https://github.com/tiangolo).

    ### Docs

    * ✏ Fix link to FastAPI and Friends newsletter. PR [#13](https://github.com/tiangolo/asyncer/pull/13) by [@JonasKs](https://github.com/JonasKs).
    * ✏ Fix typo in `docs/tutorial/first-steps.md`, from `asyncio` to `anyio`. PR [#11](https://github.com/tiangolo/asyncer/pull/11) by [@windson](https://github.com/windson).
    * ✏️ Fix broken link in README and index. PR [#9](https://github.com/tiangolo/asyncer/pull/9) by [@vrslev](https://github.com/vrslev).

    ### Internal

    * 🔧 Update mypy config, use `strict = true` instead of manual configs. PR [#38](https://github.com/tiangolo/asyncer/pull/38) by [@michaeloliverx](https://github.com/michaeloliverx).
    * ➕ Add extra dev dependencies for MkDocs Material. PR [#49](https://github.com/tiangolo/asyncer/pull/49) by [@tiangolo](https://github.com/tiangolo).
    * ⬆ Update mypy requirement from ^0.930 to ^0.971. PR [#34](https://github.com/tiangolo/asyncer/pull/34) by [@dependabot[bot]](https://github.com/apps/dependabot).

    ## 0.0.1

    * First release. 🎉

    ### Docs

    * ✏ Fix typo in index and README. PR [#4](https://github.com/tiangolo/asyncer/pull/4) by [@sanders41](https://github.com/sanders41).

    """
        )
        + "\n"
    )


def test_multiple_header_sections_label():
    raw_content = """
    # Release Notes

    ## Latest Changes

    ### Refactors

    * ✏️ Tweak docstrings format. PR [#50](https://github.com/tiangolo/asyncer/pull/50) by [@realFranco](https://github.com/realFranco).

    ### Docs

    * 👷 Upgrade CI for docs. PR [#78](https://github.com/tiangolo/asyncer/pull/78) by [@tiangolo](https://github.com/tiangolo).
    * 🛠️ Tweak internal CI actions, add `--no-cache-dir` at `Dockfile` files. PR [#52](https://github.com/tiangolo/asyncer/pull/52) by [@realFranco](https://github.com/realFranco).
    * 📝 Update help Asyncer docs. PR [#65](https://github.com/tiangolo/asyncer/pull/65) by [@tiangolo](https://github.com/tiangolo).

    ### Internal

    * 🔨 Update dev scripts. PR [#95](https://github.com/tiangolo/asyncer/pull/95) by [@tiangolo](https://github.com/tiangolo).
    * ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#83](https://github.com/tiangolo/asyncer/pull/83) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
    * ⬆ Bump actions/checkout from 3 to 4. PR [#85](https://github.com/tiangolo/asyncer/pull/85) by [@dependabot[bot]](https://github.com/apps/dependabot).

    ## 0.0.2

    ### Features

    * ✨ Add compatibility with the next (unreleased) version of AnyIO (4.x.x), with `get_asynclib` utility. PR [#48](https://github.com/tiangolo/asyncer/pull/48) by [@tiangolo](https://github.com/tiangolo).

    ### Docs

    * ✏ Fix link to FastAPI and Friends newsletter. PR [#13](https://github.com/tiangolo/asyncer/pull/13) by [@JonasKs](https://github.com/JonasKs).
    * ✏ Fix typo in `docs/tutorial/first-steps.md`, from `asyncio` to `anyio`. PR [#11](https://github.com/tiangolo/asyncer/pull/11) by [@windson](https://github.com/windson).
    * ✏️ Fix broken link in README and index. PR [#9](https://github.com/tiangolo/asyncer/pull/9) by [@vrslev](https://github.com/vrslev).

    ### Internal

    * 🔧 Update mypy config, use `strict = true` instead of manual configs. PR [#38](https://github.com/tiangolo/asyncer/pull/38) by [@michaeloliverx](https://github.com/michaeloliverx).
    * ➕ Add extra dev dependencies for MkDocs Material. PR [#49](https://github.com/tiangolo/asyncer/pull/49) by [@tiangolo](https://github.com/tiangolo).
    * ⬆ Update mypy requirement from ^0.930 to ^0.971. PR [#34](https://github.com/tiangolo/asyncer/pull/34) by [@dependabot[bot]](https://github.com/apps/dependabot).

    ## 0.0.1

    * First release. 🎉

    ### Docs

    * ✏ Fix typo in index and README. PR [#4](https://github.com/tiangolo/asyncer/pull/4) by [@sanders41](https://github.com/sanders41).

    """

    content = inspect.cleandoc(raw_content)
    settings = Settings(
        github_repository="tiangolo/latest-changes",
        github_event_path="event.json",
        input_token="secret",
        input_latest_changes_header="## Latest Changes",
        input_end_regex="^## ",
        input_labels=cast(
            Any,
            [
                {"label": "breaking", "header": "Breaking Changes"},
                {"label": "security", "header": "Security Fixes"},
                {"label": "feature", "header": "Features"},
                {"label": "bug", "header": "Fixes"},
                {"label": "refactor", "header": "Refactors"},
                {"label": "upgrade", "header": "Upgrades"},
                {"label": "docs", "header": "Docs"},
                {"label": "lang-all", "header": "Translations"},
                {"label": "internal", "header": "Internal"},
            ],
        ),
        input_label_header_prefix="### ",
    )
    pr = TemplateDataPR(
        title="Demo PR",
        number=42,
        html_url="https://example.com/pr/42",
        user=TemplateDataUser(login="tiangolo", html_url="https://github.com/tiangolo"),
    )
    new_content = generate_content(
        content=content, settings=settings, pr=pr, labels=["docs"]
    )
    assert (
        new_content
        == inspect.cleandoc(
            """
    # Release Notes

    ## Latest Changes

    ### Refactors

    * ✏️ Tweak docstrings format. PR [#50](https://github.com/tiangolo/asyncer/pull/50) by [@realFranco](https://github.com/realFranco).

    ### Docs

    * Demo PR. PR [#42](https://example.com/pr/42) by [@tiangolo](https://github.com/tiangolo).
    * 👷 Upgrade CI for docs. PR [#78](https://github.com/tiangolo/asyncer/pull/78) by [@tiangolo](https://github.com/tiangolo).
    * 🛠️ Tweak internal CI actions, add `--no-cache-dir` at `Dockfile` files. PR [#52](https://github.com/tiangolo/asyncer/pull/52) by [@realFranco](https://github.com/realFranco).
    * 📝 Update help Asyncer docs. PR [#65](https://github.com/tiangolo/asyncer/pull/65) by [@tiangolo](https://github.com/tiangolo).

    ### Internal

    * 🔨 Update dev scripts. PR [#95](https://github.com/tiangolo/asyncer/pull/95) by [@tiangolo](https://github.com/tiangolo).
    * ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#83](https://github.com/tiangolo/asyncer/pull/83) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
    * ⬆ Bump actions/checkout from 3 to 4. PR [#85](https://github.com/tiangolo/asyncer/pull/85) by [@dependabot[bot]](https://github.com/apps/dependabot).

    ## 0.0.2

    ### Features

    * ✨ Add compatibility with the next (unreleased) version of AnyIO (4.x.x), with `get_asynclib` utility. PR [#48](https://github.com/tiangolo/asyncer/pull/48) by [@tiangolo](https://github.com/tiangolo).

    ### Docs

    * ✏ Fix link to FastAPI and Friends newsletter. PR [#13](https://github.com/tiangolo/asyncer/pull/13) by [@JonasKs](https://github.com/JonasKs).
    * ✏ Fix typo in `docs/tutorial/first-steps.md`, from `asyncio` to `anyio`. PR [#11](https://github.com/tiangolo/asyncer/pull/11) by [@windson](https://github.com/windson).
    * ✏️ Fix broken link in README and index. PR [#9](https://github.com/tiangolo/asyncer/pull/9) by [@vrslev](https://github.com/vrslev).

    ### Internal

    * 🔧 Update mypy config, use `strict = true` instead of manual configs. PR [#38](https://github.com/tiangolo/asyncer/pull/38) by [@michaeloliverx](https://github.com/michaeloliverx).
    * ➕ Add extra dev dependencies for MkDocs Material. PR [#49](https://github.com/tiangolo/asyncer/pull/49) by [@tiangolo](https://github.com/tiangolo).
    * ⬆ Update mypy requirement from ^0.930 to ^0.971. PR [#34](https://github.com/tiangolo/asyncer/pull/34) by [@dependabot[bot]](https://github.com/apps/dependabot).

    ## 0.0.1

    * First release. 🎉

    ### Docs

    * ✏ Fix typo in index and README. PR [#4](https://github.com/tiangolo/asyncer/pull/4) by [@sanders41](https://github.com/sanders41).

    """
        )
        + "\n"
    )
