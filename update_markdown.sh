#!/bin/bash

# プロジェクトディレクトリのパス
PROJECT_DIR="/Users/shigikasumi/Dropbox/Projects/Projects/01_REXLI/__LINE_Marketing_Research/Statistics/jirei"

# プロジェクトディレクトリに移動
cd "$PROJECT_DIR" || { echo "ディレクトリに移動できませんでした: $PROJECT_DIR"; exit 1; }

# Git操作
git add .
git commit -m "Update Markdown file"
git push origin main
