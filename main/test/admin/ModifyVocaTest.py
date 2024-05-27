import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from func.admin.VocaManage.ModifyVoca import edit_word

edit_word("testtest", "tttt", "테테테", "n")