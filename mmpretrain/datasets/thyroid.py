from mmpretrain.registry import DATASETS
from .base_dataset import BaseDataset
import pandas as np


@DATASETS.register_module()
class Thyroid(BaseDataset):

    def load_data_list(self):
        assert isinstance(self.ann_file, str)

        data_list = []
        with open(self.ann_file) as f:
            samples = [x.strip().split(' ') for x in f.readlines()]
            for filename, gt_label in samples:
                img_path = np.add_prefix(filename, self.img_prefix)
                info = {'img_path': img_path, 'gt_label': int(gt_label)}
                data_list.append(info)
        return data_list