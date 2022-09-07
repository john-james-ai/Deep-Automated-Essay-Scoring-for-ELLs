#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Deep Automated Essay Scoring for ELLs                                               #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.4                                                                              #
# Filename   : /test_etl_extract.py                                                                #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/Deep-Automated-Essay-Scoring-for-ELLs              #
# ------------------------------------------------------------------------------------------------ #
# Created    : Monday September 5th 2022 09:54:29 pm                                               #
# Modified   : Tuesday September 6th 2022 05:41:05 pm                                              #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
import os
import inspect
import pytest
import shutil
import logging
import logging.config

# Enter imports for modules and classes being tested here
from aes.data.load import LoadEssays

# ------------------------------------------------------------------------------------------------ #
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
# ------------------------------------------------------------------------------------------------ #


@pytest.mark.extract
class TestLoadEssays:
    def test_extract(self, caplog, data):
        logger.info("\tStarted {} {}".format(self.__class__.__name__, inspect.stack()[0][3]))

        params = {
            "id_col": "text_id",
            "text_col": "full_text",
            "destination": "tests/data/extract/output",
            "force": True,
        }

        shutil.rmtree(params["destination"], ignore_errors=True)

        extract = LoadEssays(name="extract_text", params=params)
        extract.execute(data)

        assert len(os.listdir(params["destination"])) == 10

        logger.info("\tCompleted {} {}".format(self.__class__.__name__, inspect.stack()[0][3]))

    def test_extract_exists(self, caplog, data):
        logger.info("\tStarted {} {}".format(self.__class__.__name__, inspect.stack()[0][3]))

        params = {
            "id_col": "text_id",
            "text_col": "full_text",
            "destination": "tests/data/extract/output",
            "force": False,
        }

        shutil.rmtree(params["destination"], ignore_errors=True)

        extract = LoadEssays(name="extract_text", params=params)
        extract.execute(data)

        assert len(os.listdir(params["destination"])) == 10

        logger.info("\tCompleted {} {}".format(self.__class__.__name__, inspect.stack()[0][3]))
