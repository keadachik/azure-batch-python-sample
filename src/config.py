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

_BATCH_ACCOUNT_NAME = 'keadachibatch'  # Your batch account name
_BATCH_ACCOUNT_KEY = '0jxBRH7R+hvYCA6Dm16ipSvzzLxXwvHf+VE5QC47ssri65NIk9V2pfzUHZWN5Mn9VBvZbdzcFV1hi9jT1+lEdQ=='  # Your batch account key
_BATCH_ACCOUNT_URL = 'https://keadachibatch.japaneast.batch.azure.com'  # Your batch account URL
_STORAGE_ACCOUNT_NAME = 'keadachibatchdata'  # Your storage account name
_STORAGE_ACCOUNT_KEY = 'dsam4ZdKOUcmBTB+vhRJBSEDwOz/9xmAGKuiceHH/BWWS0OJMBdToOxX1GuhflZIm9Dw0wMk9bRpnG3tAJVhyA=='  # Your storage account key
_POOL_ID = 'AzureBatchSamplePool2'  # Your Pool ID
_POOL_NODE_COUNT = 2  # Pool node count
_POOL_VM_SIZE = 'STANDARD_D2_v2'  # VM Type/Size
_NOW = datetime.datetime.now()
_JOB_ID = 'PythonQuickstartJob-' + _NOW.strftime("%Y%m%d%H%M%S")  # Job ID
_STANDARD_OUT_FILE_NAME = 'stdout.txt'  # Standard Output file
_SIMPLE_TASK_NAME = 'sample_simple_task.py'
_SIMPLE_TASK_PATH = os.path.join(sys.path[0], 'sample_simple_task.py')
_DUMMY_FILE = 'readme.txt'
_DUMMY_FILE_PATH = os.path.join(sys.path[0], 'readme.txt')