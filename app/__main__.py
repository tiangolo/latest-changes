import logging
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

from devtools import debug
from github import Github
from github.NamedUser import NamedUser
from pydantic import BaseSettings, SecretStr
from pydantic.main import BaseModel
from jinja2 import Template


from app.model import Organization, PullRequest, Repository


class Settings(BaseSettings):
    github_repository: str
    github_event_path: Path
    github_event_name: Optional[str] = None
    input_token: SecretStr
    input_number: Optional[int] = None
    input_latest_changes_file: Path = Path("README.md")
    input_latest_changes_header: str = "### Latest Changes\n\n"
    input_template_file: Path = Path(__file__).parent / "latest-changes.jinja2"
    input_debug_logs: Optional[bool] = False


class GitHubEventPullRequest(BaseModel):
    action: str
    number: int
    changes: Optional[dict] = None
    pull_request: PullRequest
    repository: Repository
    organization: Optional[Organization] = None
    installation: Optional[dict] = None
    sender: Optional[dict] = None


logging.basicConfig(level=logging.INFO)
settings = Settings()
if settings.input_debug_logs:
    logging.info(f"Using config: {settings.json()}")
g = Github(settings.input_token.get_secret_value())
repo = g.get_repo(settings.github_repository)
event: Optional[GitHubEventPullRequest] = None
number: Optional[int] = settings.input_number
if settings.input_number is None and settings.github_event_path.is_file():
    contents = settings.github_event_path.read_text()
    event = GitHubEventPullRequest.parse_raw(contents)
    number = event.pull_request.number
if number is None:
    logging.error("This GitHub action must be triggered by a merged PR or with a PR number")
    sys.exit(1)
assert number is not None, "The PR number should exist by now"
pr = repo.get_pull(number)
if settings.input_debug_logs:
    logging.info("PR object:")
    debug(pr)
if not pr.merged:
    logging.error(
        "The PR was not merged but this action was run, add a step to your GitHub Action with:"
    )
    logging.error("if: github.event.pull_request.merged == true")
    sys.exit(1)
if not settings.input_latest_changes_file.is_file():
    logging.error(
        f"The latest changes files doesn't seem to exist: {settings.input_latest_changes_file}"
    )
    sys.exit(1)
logging.info("Setting up GitHub Actions git user")
subprocess.run(["git", "config", "user.name", "github-actions"], check=True)
subprocess.run(
    ["git", "config", "user.email", "github-actions@github.com"], check=True
)
logging.info(
    "Pulling the latest changes, including the latest merged PR (this one)"
)
subprocess.run(["git", "pull"], check=True)
content = settings.input_latest_changes_file.read_text()
match = re.search(settings.input_latest_changes_header, content)
if not match:
    logging.error(
        f"The latest changes file at: {settings.input_latest_changes_file} doesn't seem to contain the header RegEx: {settings.input_latest_changes_header}"
    )
    sys.exit(1)
pre_content = content[: match.end()]
post_content = content[match.end() :]
template_content = settings.input_template_file.read_text("utf-8")
template = Template(template_content)
message = template.render(pr=pr)
new_content = pre_content + message + post_content
settings.input_latest_changes_file.write_text(new_content)
logging.info(f"Committing changes to: {settings.input_latest_changes_file}")
subprocess.run(["git", "add", str(settings.input_latest_changes_file)], check=True)
subprocess.run(["git", "commit", "-m", "📝 Update release notes"], check=True)
logging.info(f"Pushing changes: {settings.input_latest_changes_file}")
subprocess.run(["git", "push"], check=True)
logging.info("Finished")
