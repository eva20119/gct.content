# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import gct.content


class GctContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=gct.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'gct.content:default')


GCT_CONTENT_FIXTURE = GctContentLayer()


GCT_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GCT_CONTENT_FIXTURE,),
    name='GctContentLayer:IntegrationTesting',
)


GCT_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GCT_CONTENT_FIXTURE,),
    name='GctContentLayer:FunctionalTesting',
)


GCT_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        GCT_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='GctContentLayer:AcceptanceTesting',
)
