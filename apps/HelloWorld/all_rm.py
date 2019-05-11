from tableDefine import * #导入自定义的东西
from django.http import HttpResponseRedirect 

def all_rm(request):
    runsyscmd('rm new_gs/4web_restudy/*')
    runsyscmd('rm language_voice_diction_english/4web_restudy/*')
    runsyscmd('rm language_voice_diction_hebrew/4web_restudy/*')
    runsyscmd('rm language_voice_diction_korean/4web_restudy/*')

    return HttpResponseRedirect('/alt1234')
