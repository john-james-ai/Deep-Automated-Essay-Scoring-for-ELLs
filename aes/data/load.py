#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Deep Automated Essay Scoring for ELLs                                               #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.4                                                                              #
# Filename   : /load.py                                                                            #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/Deep-Automated-Essay-Scoring-for-ELLs              #
# ------------------------------------------------------------------------------------------------ #
# Created    : Monday September 5th 2022 09:25:45 pm                                               #
# Modified   : Tuesday September 6th 2022 06:09:47 pm                                              #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
import os
import shutil
from typing import Any
from atelier.workflow.operators import Operator

# ------------------------------------------------------------------------------------------------ #


class LoadEssays(Operator):
    """Loads essays into staged directory

    Args:
        name (str): The name for the step in the pipeline.
        params (dict): Dictionary containing
            - id_col (str): Column containing the identifier for the essay.
            - text_col (str): Column containing the text of the essay.
            - destination (str): The folder into which essays will be essays
        force (bool): Whether to overwrite existing data. If data already exists
            then force must be True, otherwise the step is not executed.

    """

    def __init__(self, name: str, params: dict = {}) -> None:
        super(LoadEssays, self).__init__(name=name, params=params)
        self._id_col = self._params.get("id_col", "text_id")
        self._text_col = self._params.get("text_col", "full_text")
        self._destination = self._params.get("destination", None)
        self._force = self._params.get("force", None)

    def execute(self, data: Any = None, context: dict = {}) -> None:
        """Decompresses a zipfile from source and stores contents at destination.

        Args:
            data: Not used
            context: not used.
        """

        if self._force or not os.path.exists(self._destination):

            # Remove residual data just in case.
            shutil.rmtree(self._destination, ignore_errors=True)
            os.makedirs(self._destination, exist_ok=True)

            ids = list(data[self._id_col].values)
            essays = list(data[self._text_col].values)
            for id, essay in zip(ids, essays):
                filename = id + ".txt"
                filepath = os.path.join(self._destination, filename)
                with open(filepath, "w") as f:
                    f.writelines(essay)
