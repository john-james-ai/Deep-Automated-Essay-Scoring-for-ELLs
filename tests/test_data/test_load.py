#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Deep Automated Essay Scoring for ELLs                                               #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.4                                                                              #
# Filename   : /test_load.py                                                                       #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/Deep-Automated-Essay-Scoring-for-ELLs              #
# ------------------------------------------------------------------------------------------------ #
# Created    : Tuesday September 6th 2022 10:36:17 pm                                              #
# Modified   : Tuesday September 6th 2022 10:43:45 pm                                              #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
import os
import inspect
import pytest
import logging
import logging.config

# Enter imports for modules and classes being tested here
from aes.data.load import LoadEssays

# ------------------------------------------------------------------------------------------------ #
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
# ------------------------------------------------------------------------------------------------ #


@pytest.mark.load_essays
class TestLoadEssays:
    def test_load_essays(self, caplog, data):
        logger.info("\tStarted {} {}".format(self.__class__.__name__, inspect.stack()[0][3]))

        name = "load_essays"
        params = {"destination": "tests/data/extracted/", "force": False}
        load = LoadEssays(name=name, params=params)
        load.execute(data=data)
        assert len(os.listdir(params["destination"])) == 10

        logger.info("\tCompleted {} {}".format(self.__class__.__name__, inspect.stack()[0][3]))

    def test_skip_essays(self, caplog, data):
        logger.info("\tStarted {} {}".format(self.__class__.__name__, inspect.stack()[0][3]))

        name = "load_essays"
        params = {"destination": "tests/data/extracted/", "force": False}
        load = LoadEssays(name=name, params=params)
        load.execute(data=data)
        assert len(os.listdir(params["destination"])) == 10

        logger.info("\tCompleted {} {}".format(self.__class__.__name__, inspect.stack()[0][3]))
