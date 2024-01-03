# -*- coding: utf-8 -*-


#
# IMPORTS
#


from .settings import GeneralSettings

#
#
# TYPES
#


class InitSettings(GeneralSettings):
    pass


#
# INITIALIZATION
#


settings = InitSettings()

__version__ = settings.version
