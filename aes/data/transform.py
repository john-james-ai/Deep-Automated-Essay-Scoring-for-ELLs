#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Deep Automated Essay Scoring for ELLs                                               #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.4                                                                              #
# Filename   : /transform.py                                                                       #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/Deep-Automated-Essay-Scoring-for-ELLs              #
# ------------------------------------------------------------------------------------------------ #
# Created    : Tuesday September 6th 2022 05:38:49 pm                                              #
# Modified   : Tuesday September 6th 2022 09:16:55 pm                                              #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
import os
import pandas as pd
import spacy
from spacy.tokens import Doc
from typing import Any
from atelier.workflow.operators import Operator
from atelier.data.io import YamlIO, PickleIO

# ------------------------------------------------------------------------------------------------ #


class TransformEssays(Operator):
    """Transforms essays into tokens, with POS-tagging and dependency parsing.

    Args:
        name (str): The name for the step in the pipeline.
        params (dict): Dictionary containing:
            'destination': filepath for the transformed essay documents
            'components': the list of pipeline components to execute.
        force (bool): Whether to overwrite existing data. If data already exists
            then force must be True, otherwise the step is not executed.

    """

    __spacy_configfile = "config/spacy.yml"

    def __init__(self, name: str, params: dict = {}) -> None:
        super(TransformEssays, self).__init__(name=name, params=params)

        # Obtain spacy configuration
        io = YamlIO()
        self._spacy_config = io.read(TransformEssays.__spacy_configfile)

        # Force parameter
        self._force = self._params.get("force", None)

    def execute(self, data: Any = None, context: dict = {}) -> None:
        """Executes an NLP Pipeline and returns a spaCy document object.

        Args:
            data: Data to be processed through the pipeline
            context: not used.
        """

        if self._force or not os.path.exists(self._destination):

            docs = self._execute_pipeline(data=data)
            self._save_documents(docs)

            return docs

    def _execute_pipeline(self, data: pd.DataFrame) -> list:
        """Executes the pipeline and returns the documents object.

        Args:
            data: (pd.DataFrame) The data to be transformed

        Returns:
            list of document objects.
        """

        if not Doc.has_extension("text_id"):
            Doc.set_extension("text_id", default=None)

        # Convert the data to a list of tuples to preserve the text_id
        df = data[["full_text", "text_id"]]
        tt = [
            ((row["full_text"], {"text_id": row["text_id"]})) for row in df.to_records(index=False)
        ]

        # Get pipeline components to disable
        disabled_components = self._get_disabled_components()

        # Load the NLP model and run the pipeline which returns tuples
        nlp = spacy.load(self._spacy_config["model"])
        dt = nlp.pipe(tt, as_tuples=True, disable=disabled_components)

        # Convert the tuples to a list
        docs = []
        for doc, context in dt:
            doc._.text_id = context["text_id"]
            docs.append(doc)

        return docs

    def _get_disabled_components(self):
        """Extract the components to disable from the pipeline."""

        disabled_components = []

        all_components = self._spacy_config["components"]
        requested_components = self._params.get("components", None)

        for component in all_components:
            if component not in requested_components:
                disabled_components.append(component)

        return disabled_components

    def _save_documents(self, docs: list) -> None:
        """Saves the document in Pickle format.

        Args:
            docs (list): List of Document objects.
        """
        io = PickleIO()
        io.write(docs, self._params["destination"])
