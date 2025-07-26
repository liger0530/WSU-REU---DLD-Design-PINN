# Abstract
Deterministic Lateral Displacement (DLD) devices are widely used in microfluidics for particle separation (e.g., DNA isolation and cancer cell detection). However, computational challenges remain in efficiently and accurately simulating trajectories within DLD geometries due to the complexities of the Navier-Stokes equations. To address this issue, recent research has explored surrogate modeling using deep learning. However, prior work has largely overlooked the inclusion of physical constraints on periodic boundaries, which are essential for accurately capturing flow continuity across DLD units. This paper further investigates deep learning solutions by utilizing Physics-Informed Neural Networks (PINNs) to enforce DLD behavior through boundary conditions at inlets, outlets, pillars, and periodic boundaries. These deep learning models typically require large datasets and extensive training epochs to achieve accurate results. To overcome this limitation, this research integrates Navier-Stokes–driven loss functions to enable training without any labeled data. This approach allows the model to be trained on a denser input domain while remaining independent of specific datasets and avoiding overfitting to particular geometries.

# About Repository
Three types of PINN exist in this repository: Original, Periodic, Label_Free. All three models results in three sub-networks (or models) each predicting u,v,and p in that order.

## Original
This model is direct training of DLD trajectory based on CFD simulation datasets. The training is done through PINN_Original.ipynb and model weights are saved in 'models/original'. The predictions, comparisons, and loss histories are saved in 'results/original'.

## Periodic
This model trains same as original but with boundary conditions to set zero velocities at the post and equal u,v,p at periodic boundary pairs. The weights are saved in 'models/periodic' and results are saved in 'results/periodic'.

## Label Free
This model trains with partial differential equation (PDE) derived losses from Navier-Stokes Equations and does not use dataset for training. The weights are saved in 'models/label_free' and results are saved in 'results/label_free'.