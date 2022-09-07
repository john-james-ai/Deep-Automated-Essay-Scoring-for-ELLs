#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Deep Automated Essay Scoring for ELLs                                               #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.4                                                                              #
# Filename   : /conftest.py                                                                        #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/Deep-Automated-Essay-Scoring-for-ELLs              #
# ------------------------------------------------------------------------------------------------ #
# Created    : Monday September 5th 2022 09:56:02 pm                                               #
# Modified   : Monday September 5th 2022 10:34:29 pm                                               #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
"""Includes fixtures, classes and functions supporting testing."""
import pytest
import pandas as pd

# ------------------------------------------------------------------------------------------------ #
TEST_DATA_FILEPATH = "tests/data/train.csv"
# ------------------------------------------------------------------------------------------------ #
#                                        IGNORE                                                    #
# ------------------------------------------------------------------------------------------------ #
collect_ignore_glob = ["tests/old_tests/**/*.py"]
# ------------------------------------------------------------------------------------------------ #
#                                          SOURCE                                                  #
# ------------------------------------------------------------------------------------------------ #


@pytest.fixture(scope="module")
def data():
    df = pd.read_csv(TEST_DATA_FILEPATH)
    return df.loc[0:9, :]
