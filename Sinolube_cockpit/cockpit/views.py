# coding:utf-8
import urllib, urllib2, json

from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.clickjacking import xframe_options_exempt

from cockpit.models import BiCommonPagesu, PagesuDocID


@xframe_options_exempt
def index(request):
    #     username = request.user.first_name + request.user.last_name
    if request.method == 'GET':
        return render_to_response('index.html', locals(), context_instance=RequestContext(request))


def getPageSetting(pageid, mstrid='sinolube'):
    settings = {}

    if pageid != "":
        try:
            pagesu = BiCommonPagesu.objects.get(mstrid=mstrid);
            settings['mstraddr'] = pagesu.mstraddr
            jsonurladdr = json.loads(pagesu.urladdr)
            settings['evt'] = jsonurladdr['evt']
            settings['src'] = jsonurladdr['src']
            # folderID = jsonurladdr['folderID']

            print 'pageid:', pageid
            settings['visMode'] = jsonurladdr['visMode']
            settings['currentViewMedia'] = jsonurladdr['currentViewMedia']

            settings['server'] = jsonurladdr['server']
            settings['Project'] = jsonurladdr['Project']
            settings['port'] = jsonurladdr['port']
            settings['share'] = jsonurladdr['share']
            settings['hiddensections'] = jsonurladdr['hiddensections']
            settings['uid'] = jsonurladdr['uid']
            settings['pwd'] = jsonurladdr['pwd']
            doc = PagesuDocID.objects.get(pageid=pageid)
            settings['documentID'] = doc.docid
            print 'settings:', settings
            # promptAnswerMode = jsonurladdr['promptAnswerMode']
        except Exception as e:
            print e
            print "page ", " dose not exists"
            pass
    print pageid, settings
    return settings


def sub(request):
    #     pageid = request.GET.get('index')
    settings = getPageSetting('1')
    print settings
    return HttpResponse(json.dumps(settings))