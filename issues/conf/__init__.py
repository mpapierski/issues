import os

from .git import GitConfig


# TODO: Implement other config providers as a fallback

settings = GitConfig(
    # You usually want to call issues from inside your git repository
    os.getcwd())
