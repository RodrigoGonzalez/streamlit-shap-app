#!/bin/sh
# make executable with
# chmod +x scripts/commit.sh

current_branch=$(git symbolic-ref --short HEAD)

if [ "$current_branch" = "main" ] || [ "$current_branch" = "master" ]; then
  echo "Error: You are on the main or master branch."
  echo "Switch to a different branch before committing."
  exit 1
else
  poetry run cz commit
  # if adding commit to remote branch -u is redundant,
	# however it is needed for the first commit and doesn't
	# have any effects on subsequent commits
  git push -u origin HEAD
fi
