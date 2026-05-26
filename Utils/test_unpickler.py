import pickle
import sys, types

class _MockedClass:
    def __init__(self, *args, **kwargs): pass
    def __call__(self, *args, **kwargs): return self
    def __setstate__(self, state): pass
    def __getattr__(self, name): return _MockedClass()

class _DummyUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if 'torch' in module or 'networkx' in module or 'numpy' in module:
            return _MockedClass
        return super().find_class(module, name)

try:
    with open('c:/Users/ASUS/OneDrive/Desktop/BTP/shared_map.pkl', 'rb') as f:
        M = _DummyUnpickler(f).load()
    print("SUCCESS")
    with open('c:/Users/ASUS/OneDrive/Desktop/BTP/real_gan_data.json', 'w') as f:
        import json
        json.dump({'g_hist': M['g_hist'], 'd_hist': M['d_hist']}, f)
    print("Data extracted to real_gan_data.json")
except Exception as e:
    print("FAILED", type(e).__name__, e)
