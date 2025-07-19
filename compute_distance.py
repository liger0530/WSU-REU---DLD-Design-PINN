import torch

def compute_distance(x, y, d, n):
    """
    x, y, d, n: tensors of identical shape (e.g. [N] or [N,1]).
    Returns min non-negative distance to the 4 posts.
    """
    tilt = 0.012 / n          # same shape as x

    # Build center coordinate tensors with per-point tilt
    cx = torch.stack([
        torch.zeros_like(x),
        torch.zeros_like(x),
        torch.full_like(x, 0.012),
        torch.full_like(x, 0.012)
    ], dim=-1)                # shape [...,4]

    cy = torch.stack([
        torch.zeros_like(x),
        torch.full_like(x, 0.012),
        tilt,
        0.012 + tilt
    ], dim=-1)                # shape [...,4]

    X = x.unsqueeze(-1)       # shape [...,1]
    Y = y.unsqueeze(-1)

    r = d / 2.0               # broadcasts (same shape as x or scalar)

    dist_all = torch.sqrt((X - cx)**2 + (Y - cy)**2) - r.unsqueeze(-1)
    dist_min = torch.min(dist_all, dim=-1).values  # shape [...,4]
    return dist_min