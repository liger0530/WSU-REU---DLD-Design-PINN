import torch

def compute_distance(x,y,d,n):
    """Compute the minimum distance of (x, y) from the nearest circular post."""
    tilt = 0.012/n
    centers = [(0, 0), (0, 0.012), (0.012, tilt), (0.012, 0.012+tilt)]
    
    distances = torch.full_like(x, 1)  # Initialize distances with large values

    for cx, cy in centers:
        r = d / 2
        distance_to_post = torch.sqrt((x - cx) ** 2 + (y - cy) ** 2) - r
        distances *= distance_to_post

    return distances