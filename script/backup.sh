#!/usr/bin/env zsh

# 添加所有修改到暂存区
git add .

# 提交暂存区的修改，并添加提交信息
git commit -m "add new"

# 推送代码到远程仓库的 main 分支
git push origin main