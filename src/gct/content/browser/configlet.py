# -*- coding: utf-8 -*-
from gct.content import _
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from zope import schema
from plone.z3cform import layout
from z3c.form import form
from plone.directives import form as Form


class IDict(Form.Schema):

    dict = schema.Text(
        title=_(u'store category and subject'),
        required=False,
    )


class CategoriesControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IDict

CustomControlPanelView = layout.wrap_form(CategoriesControlPanelForm, ControlPanelFormWrapper)
CustomControlPanelView.label = _(u"Custom Related Setting")
