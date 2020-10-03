import logging
import subprocess
from pathlib import Path
from typing import Optional

from devtools import debug
from github import Github
from github.NamedUser import NamedUser
from pydantic import BaseSettings, SecretStr
from pydantic.main import BaseModel

from app.model import Organization, PullRequest, Repository


class Settings(BaseSettings):
    github_repository: str
    input_token: SecretStr
    github_event_path: Path
    github_event_name: Optional[str] = None
    input_latest_changes_file: Path = Path("README.md")
    input_latest_changes_header: str = "### Latest Changes\n\n"


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
logging.info(f"Using config: {settings.json()}")
# g = Github(settings.input_token.get_secret_value())
# repo = g.get_repo(settings.github_repository)
# owner: NamedUser = repo.owner
# github_event: Optional[GitHubEventPullRequest] = None
if settings.github_event_path.is_file():
    contents = settings.github_event_path.read_text()
    github_event = GitHubEventPullRequest.parse_raw(contents)
    debug(github_event)
    logging.info(github_event.json(indent=2))
    logging.info(f"Current dir: {Path.cwd()}")
    logging.info(f"Current dir list: {list(Path.cwd().iterdir())}")
    subprocess.run(["git", "config", "user.name", "github-actions"], check=True)
    subprocess.run(["git", "config", "user.email", "github-actions@github.com"], check=True)
    subprocess.run(["git", "pull"], check=True)
    content = settings.input_latest_changes_file.read_text()
    header_break_point = content.index(settings.input_latest_changes_header) + len(
        settings.input_latest_changes_header
    )
    pre_content = content[:header_break_point]
    post_content = content[header_break_point:]
    message = f"* {github_event.pull_request.title}. PR [#{github_event.pull_request.number}]({github_event.pull_request.html_url}) by [@{github_event.pull_request.user.login}]({github_event.pull_request.user.html_url}).\n"
    new_content = pre_content + message + post_content
    settings.input_latest_changes_file.write_text(new_content)
    subprocess.run(["git", "add", str(settings.input_latest_changes_file)], check=True)
    subprocess.run(["git", "commit", "-m", "📝 Update release notes"], check=True)
    subprocess.run(["git", "push"], check=True)
logging.info("Finished")
