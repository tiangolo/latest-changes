import logging
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

from github import Github
from jinja2 import Template
from pydantic import BaseModel, BaseSettings, SecretStr


class Settings(BaseSettings):
    github_repository: str
    github_event_path: Path
    github_event_name: Optional[str] = None
    input_token: SecretStr
    input_latest_changes_file: Path = Path("README.md")
    input_latest_changes_header: str = "### Latest Changes\n\n"
    input_template_file: Path = Path(__file__).parent / "latest-changes.jinja2"
    input_debug_logs: Optional[bool] = False


class PartialGitHubEventInputs(BaseModel):
    number: int


class PartialGitHubEvent(BaseModel):
    number: Optional[int] = None
    inputs: Optional[PartialGitHubEventInputs] = None


logging.basicConfig(level=logging.INFO)
# Ref: https://github.com/actions/runner/issues/2033
logging.info("GitHub Actions workaround for git in containers, ref: https://github.com/actions/runner/issues/2033")
safe_directory_config_content = "[safe]\n\tdirectory = /github/workspace"
dotgitconfig_path = Path.home() / ".gitconfig"
dotgitconfig_path.write_text(safe_directory_config_content)
settings = Settings()
if settings.input_debug_logs:
    logging.info(f"Using config: {settings.json()}")
g = Github(settings.input_token.get_secret_value())
repo = g.get_repo(settings.github_repository)
if not settings.github_event_path.is_file():
    logging.error(f"No event file was found at: {settings.github_event_path}")
    sys.exit(1)
contents = settings.github_event_path.read_text()
event = PartialGitHubEvent.parse_raw(contents)
if event.number is not None:
    number = event.number
elif event.inputs and event.inputs.number:
    number = event.inputs.number
else:
    logging.error(
        f"No PR number was found (PR number or workflow input) in the event file at: {settings.github_event_path}"
    )
    sys.exit(1)
pr = repo.get_pull(number)
if not pr.merged:
    logging.info("The PR was not merged, nothing else to do.")
    sys.exit(0)
if not settings.input_latest_changes_file.is_file():
    logging.error(
        f"The latest changes files doesn't seem to exist: {settings.input_latest_changes_file}"
    )
    sys.exit(1)
logging.info("Setting up GitHub Actions git user")
subprocess.run(["git", "config", "user.name", "github-actions"], check=True)
subprocess.run(["git", "config", "user.email", "github-actions@github.com"], check=True)
logging.info("Pulling the latest changes, including the latest merged PR (this one)")
subprocess.run(["git", "pull"], check=True)
content = settings.input_latest_changes_file.read_text()
match = re.search(settings.input_latest_changes_header, content)
if not match:
    logging.error(
        f"The latest changes file at: {settings.input_latest_changes_file} doesn't seem to contain the header RegEx: {settings.input_latest_changes_header}"
    )
    sys.exit(1)
template_content = settings.input_template_file.read_text("utf-8")
template = Template(template_content)
message = template.render(pr=pr)
if message in content:
    logging.error(f"It seems these PR's latest changes were already added: {number}")
    sys.exit(1)
pre_content = content[: match.end()]
post_content = content[match.end() :]
new_content = pre_content + message + post_content
settings.input_latest_changes_file.write_text(new_content)
logging.info(f"Committing changes to: {settings.input_latest_changes_file}")
subprocess.run(["git", "add", str(settings.input_latest_changes_file)], check=True)
subprocess.run(["git", "commit", "-m", "📝 Update release notes"], check=True)
logging.info(f"Pushing changes: {settings.input_latest_changes_file}")
subprocess.run(["git", "push"], check=True)
logging.info("Finished")
