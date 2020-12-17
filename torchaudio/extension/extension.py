import os
import warnings
import importlib
from collections import namedtuple

import torch
from torchaudio._internal import module_utils as _mod_utils


def _init_extension():
    ext = 'torchaudio._torchaudio'
    if _mod_utils.is_module_available(ext):
        _init_script_module(ext)
    else:
        warnings.warn('torchaudio C++ extension is not available.')


def _init_transducer_extension():
    ext = '_warp_transducer'
    if _mod_utils.is_module_available(ext):
        _init_script_module(ext)
        # path = importlib.util.find_spec(ext).origin
        # torch.ops.load_library(path)
    else:
        warnings.warn('warp-transducer extension is not available.')


def _init_script_module(module):
    path = importlib.util.find_spec(module).origin
    warnings.warn(f"module path: {path}, {os.path.realpath(path)} {os.path.expandvars(path)}")
    torch.classes.load_library(path)
    torch.ops.load_library(path)
