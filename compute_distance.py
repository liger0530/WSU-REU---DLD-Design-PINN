import torch

def compute_distance(x, y, d, n):
    """
    x, y, d, n: tensors of identical shape (e.g. [N] or [N,1]).
    Returns min non-negative distance to the 4 posts.
    """
    tilt = 0.012 / n       

    cx = torch.stack([
        torch.zeros_like(x),
        torch.zeros_like(x),
        torch.full_like(x, 0.012),
        torch.full_like(x, 0.012)
    ], dim=-1)             

    cy = torch.stack([
        torch.zeros_like(x),
        torch.full_like(x, 0.012),
        tilt,
        0.012 + tilt
    ], dim=-1)        

    X = x.unsqueeze(-1)      
    Y = y.unsqueeze(-1)

    r = d / 2.0     

    dist_all = torch.sqrt((X - cx)**2 + (Y - cy)**2) - r.unsqueeze(-1)
    dist_min = torch.min(dist_all, dim=-1).values 
    return dist_min