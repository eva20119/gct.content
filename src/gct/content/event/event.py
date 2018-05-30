from plone import api
from zope.globalrequest import getRequest

def move_to_top(item, event):
    request = getRequest()
    item.moveObjectsToTop(item.id)
    abs_url = api.portal.get().absolute_url()
    request.response.redirect('%s/folder_contents' %abs_url)
