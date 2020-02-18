#!/bin/bash

# リポジトリ追加
apt update && apt -y install software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa

# python3.7　インストール
apt -y install python3.7
ln -sfn /usr/bin/python3.7 /usr/bin/python
