# -------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "python_quickstart_client.py "
import datetime
import os
import sys

# ポータルから設定値を入手して記入
_BATCH_ACCOUNT_NAME = ''  # Your batch account name
_BATCH_ACCOUNT_KEY = ''  # Your batch account key
_BATCH_ACCOUNT_URL = ''  # Your batch account URL

_STORAGE_ACCOUNT_NAME = ''  # Your storage account name
_STORAGE_ACCOUNT_KEY = ''  # Your storage account key

_POOL_ID = 'AzureBatchSamplePool'  # Your Pool ID

# プログラムからpoolを作成する場合のパラメータ
_POOL_NODE_COUNT = 0  # Pool node count
_LOW_PRIORITY_POOL_NODE_COUNT = 4
_POOL_VM_SIZE = 'STANDARD_D2_v2'  # VM Type/Size

# タスクのイン、アウトのファイル名
_NOW = datetime.datetime.now()
_JOB_ID = 'EchoFileJob-' + _NOW.strftime("%Y%m%d%H%M%S")  # Job ID
_STANDARD_OUT_FILE_NAME = 'stdout.txt'  # Standard Output file
_SIMPLE_TASK_NAME = 'sample_simple_task.py'
_SIMPLE_TASK_PATH = os.path.join(sys.path[0], 'sample_simple_task.py')
_DUMMY_FILE = 'readme.txt'
_DUMMY_FILE_PATH = os.path.join(sys.path[0], 'readme.txt')