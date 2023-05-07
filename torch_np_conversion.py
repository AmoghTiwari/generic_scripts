import torch
import numpy as np

def torch_to_numpy(tensor_):
    if len(tensor_.shape) == 4:
        if tensor_.shape[0] == 1:
            tensor_ = tensor_.squeeze(0)
        else:
            print(f"More than one tensors packed into a single tensor (shape: {tensor_.shape}). Can't convert to numpy. Exitting from function")
            exit(0)
    return 255 * (np.transpose(tensor_.detach().cpu().numpy(), (1, 2, 0)) * 0.5 + 0.5)[:, :, ::-1]

def numpy_to_torch(arr):
    return torch.from_numpy(np.transpose(((arr / 255)[:,:,::-1] - 0.5 ) / 0.5, (2,0,1))).unsqueeze(0)

breakpoint()