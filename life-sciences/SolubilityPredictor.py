import logging
import numpy as np
from typing import Dict, List, Union, Iterable
import pkg_resources 

import deepchem as dc
from rdkit import Chem

logger = logging.getLogger(__name__)

class SolubilityPredictor(object):
    def __init__(self):
        installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]
        logger.info(f"{installed_packages}")
        self.ready = False

    def load(self):
        logger.info("Loading...")
        self._model = dc.models.GraphConvModel(n_tasks=1, mode='regression', dropout=0.2, model_dir="./ckpt-model")
        self._model.restore()
        self.ready = True

    def predict(self, smiles: List, meta: Dict = None) -> Union[np.ndarray, List, str, bytes]:
        try:
            if not self.ready:
                self.load()
            mols = [Chem.MolFromSmiles(s) for s in smiles]
            featurizer = dc.feat.ConvMolFeaturizer()
            x = featurizer.featurize(mols)
            self.predicted_solubility = self._model.predict_on_batch(x)
            return self.predicted_solubility
        
        except Exception as ex:
            logging.exception("Exception during predict!")
            logging.exception(f"{ex}")