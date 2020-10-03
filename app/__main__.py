import logging
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
g = Github(settings.input_token.get_secret_value())
repo = g.get_repo(settings.github_repository)
owner: NamedUser = repo.owner
github_event: Optional[GitHubEventPullRequest] = None
if settings.github_event_path.is_file():
    contents = settings.github_event_path.read_text()
    github_event = GitHubEventPullRequest.parse_raw(contents)
    debug(github_event)
    logging.info(github_event.json(indent=2))
logging.info("Finished")
