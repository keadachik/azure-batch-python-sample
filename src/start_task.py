import azure.batch.models as batchmodels

task_commands = [
        # リポジトリ追加
        'apt update && apt -y install software-properties-common',
        'add-apt-repository -y ppa:deadsnakes/ppa',
        # python3.7　インストール
        'apt -y install python3.7',
        'ln -sfn /usr/bin/python3.7 /usr/bin/python',
    ]

user = batchmodels.AutoUserSpecification(
        scope=batchmodels.AutoUserScope.pool,
        elevation_level=batchmodels.ElevationLevel.admin)