import torch

def compute_distance(x, y, d, n, ds=0.4):
    """
    x, y, d, n: tensors of identical shape (e.g. [N] or [N,1]).
    Returns min non-negative distance to the 4 posts.
    """
    tilt = ds / n       

    cx = torch.stack([
        torch.zeros_like(x),
        torch.zeros_like(x),
        torch.full_like(x, ds),
        torch.full_like(x, ds)
    ], dim=-1)             

    cy = torch.stack([
        torch.zeros_like(x),
        torch.full_like(x, ds),
        tilt,
        ds + tilt
    ], dim=-1)        

    X = x.unsqueeze(-1)      
    Y = y.unsqueeze(-1)

    r = d / 2.0

    beta = 1000

    dist_all = torch.sqrt((X - cx)**2 + (Y - cy)**2) - r.unsqueeze(-1)
    dist_min = -torch.logsumexp(-beta * dist_all, dim=-1) / beta
    
    return torch.clamp(dist_min, min=0)