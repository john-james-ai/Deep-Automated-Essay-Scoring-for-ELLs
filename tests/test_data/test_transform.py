#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Deep Automated Essay Scoring for ELLs                                               #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.4                                                                              #
# Filename   : /test_transform.py                                                                  #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/Deep-Automated-Essay-Scoring-for-ELLs              #
# ------------------------------------------------------------------------------------------------ #
# Created    : Tuesday September 6th 2022 09:02:46 pm                                              #
# Modified   : Tuesday September 6th 2022 09:12:48 pm                                              #
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
from aes.data.transform import TransformEssays

# ------------------------------------------------------------------------------------------------ #
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
# ------------------------------------------------------------------------------------------------ #


@pytest.mark.xform
class TestXForm:
    def test_xform(self, caplog, data):
        logger.info("\tStarted {} {}".format(self.__class__.__name__, inspect.stack()[0][3]))

        name = "transform_essays"
        params = {
            "destination": "tests/data/train.pkl",
            "components": ["tokenizer", "tagger", "parser", "senter"],
            "force": True,
        }

        xform = TransformEssays(name=name, params=params)
        docs = xform.execute(data)

        assert os.path.exists(params["destination"])
        assert isinstance(docs, list)

        logger.info("\tCompleted {} {}".format(self.__class__.__name__, inspect.stack()[0][3]))
