from torch import *
from torch_geometric.data import InMemoryDataset, Data
from torch.nn import Linear
from torch.optim.lr_scheduler import MultiStepLR
import torch.nn.functional
import torch_geometric.nn
from torch_geometric.nn import TopKPooling, global_mean_pool
from torch_geometric.nn import global_mean_pool as gap, global_max_pool as gmp
from torch_geometric.data import DataLoader
import torch.backends.cudnn as cudnn

import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
class GCN(torch.nn.Module):
    def __init__(self,X_train):
        super(GCN, self).__init__()
        self.CC1 = torch_geometric.nn.ChebConv(X_train.shape[1], 16,K = 3)
        self.PL1 = torch_geometric.nn.max_pool()
        self.BN1 = torch.nn.BatchNorm1d(16)

        self.CC2 = torch_geometric.nn.ChebConv(X_train.shape[1], 32, K=3)
        self.PL2 = torch_geometric.nn.max_pool()
        self.BN2 = torch.nn.BatchNorm1d(32)

        self.CC3 = torch_geometric.nn.ChebConv(X_train.shape[1], 64, K=3)
        self.PL3 = torch_geometric.nn.max_pool()
        self.BN3 = torch.nn.BatchNorm1d(64)

        self.CC4 = torch_geometric.nn.ChebConv(X_train.shape[1], 128, K=3)
        self.PL4 = torch_geometric.nn.max_pool()
        self.BN4 = torch.nn.BatchNorm1d(128)

        self.CC5 = torch_geometric.nn.ChebConv(X_train.shape[1], 256, K=3)
        self.PL5 = torch_geometric.nn.max_pool()

        self.dense = Linear(128 * 2, 4)

    def forward(self, x, edge_index, batch_index, edge_weight):
        hidden = self.CC1(x, edge_index, edge_weight)
        hidden = self.PL1(hidden)
        hidden = torch.nn.functional .softplus(hidden)
        hidden = self.BN1(hidden)

        hidden = self.CC2(hidden, edge_index, edge_weight)
        hidden = self.PL2(hidden)
        hidden = torch.nn.functional.softplus(hidden)
        hidden = self.BN2(hidden)

        hidden = self.CC3(hidden, edge_index, edge_weight)
        hidden = self.PL3(hidden)
        hidden = torch.nn.functional.softplus(hidden)
        hidden = self.BN3(hidden)

        hidden = self.CC4(hidden, edge_index, edge_weight)
        hidden = self.PL4(hidden)
        hidden = torch.nn.functional.softplus(hidden)
        hidden = self.BN4(hidden)

        hidden = self.CC5(hidden, edge_index, edge_weight)
        hidden = self.PL5(hidden)

        hidden = torch.cat([gmp(hidden, batch_index),
                            gap(hidden, batch_index)], dim=1)

        hidden = self.dense(hidden)

        return torch.nn.functional.log_softmax(hidden, dim=4)