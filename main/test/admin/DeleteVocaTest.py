import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from func.admin.VocaManage.DeleteVoca import delete_word

#Test
delete_word("testtest")