import torch
import numpy as np
from PIL import Image
from torchvision import transforms 

totensor = transforms.ToTensor()

def read_image(path:str) -> torch.Tensor:
    """ Read an image from given path 
    
    Args:
        path (str) : The given path 
    
    Returns:
        result Tensor 
    """
    
    image = Image.open(path)
    return totensor(image)


