from django.http import HttpResponseRedirect 
from django.shortcuts import render
import os
from MyPython3 import readffile
def index(request):
    restudy_info = {}
    restudy_info['alt1'] = '进度中alt1'
    restudy_info['alt1_common'] = 'alt1_common'
    restudy_info['alt2'] = '进度中alt2'
    restudy_info['alt2_common'] = 'alt2_common'
    restudy_info['alt3'] = '进度中alt3'
    restudy_info['alt3_common'] = 'alt3_common'
    restudy_info['alt4'] = '进度中alt4'
    restudy_info['alt4_common'] = 'alt4_common'
    restudy_info['plan_endian'] = readffile('plan_endian/everydaytodolist.txt')

    if os.path.exists('new_gs/4web_restudy/已复习') and not os.path.exists('new_gs/4web_restudy/common_info'):
        restudy_info['alt1'] = 'alt1已复习'
        restudy_info['alt1_common'] = ''
    elif not os.path.exists('new_gs/4web_restudy/common_info'):
        restudy_info['alt1'] = 'alt1'
        restudy_info['alt1_common'] = ''

    if os.path.exists('language_voice_diction_korean/4web_restudy/已复习') and not os.path.exists('language_voice_diction_korean/4web_restudy/common_info'):
        restudy_info['alt2'] = 'alt2已复习'
        restudy_info['alt2_common'] = ''
    elif not os.path.exists('language_voice_diction_korean/4web_restudy/common_info'):
        restudy_info['alt2'] = 'alt2'
        restudy_info['alt2_common'] = ''

    if os.path.exists('language_voice_diction_english/4web_restudy/已复习') and not os.path.exists('language_voice_diction_english/4web_restudy/common_info'):
        restudy_info['alt3'] = 'alt3已复习'
        restudy_info['alt3_common'] = ''
    elif not os.path.exists('language_voice_diction_english/4web_restudy/common_info'):
        restudy_info['alt3'] = 'alt3'
        restudy_info['alt3_common'] = ''

    if os.path.exists('language_voice_diction_hebrew/4web_restudy/已复习') and not os.path.exists('language_voice_diction_hebrew/4web_restudy/common_info'):
        restudy_info['alt4'] = 'alt4已复习'
        restudy_info['alt4_common'] = ''
    elif not os.path.exists('language_voice_diction_hebrew/4web_restudy/common_info'):
        restudy_info['alt4'] = 'alt4'
        restudy_info['alt4_common'] = ''
    
    #restudy_info['alt1_common'] = ''
    #restudy_info['alt2_common'] = ''
    #restudy_info['alt3_common'] = ''
    #restudy_info['alt4_common'] = ''
    return render(request, 'index.html', restudy_info)

