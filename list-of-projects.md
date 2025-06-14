# List of My Projects

*Last updated: May 31, 2025*

Here is a document I created to track and showcase my projects. As a [kid from an alien planet](https://en.wikipedia.org/wiki/Asperger_syndrome), I spent a large fraction of my spare time on personal programming projects as a [surrogate activity](https://books.google.ca/books?id=ckfJEAAAQBAJ&pg=PT19&lpg=PT19). Almost all works on my GitHub are done independently. My topics of interest include rendering and visualization, 3D computer vision, deep learning, geometry processing, image and signal processing, and physical simulation and control. I value high performance in my works, but I'm also inclined to solve problems in unconventional ways. I enjoy coding in C++ and Python, but I've also created a number of web applications for their accessibility.

## Currently Working On

Gaussian splatting, half a research project and half a personal project and half for job;

Works in my school's drone racing team, covering wide range of topics including developing a photorealistic drone simulator, gate detection using deep learning, model-based reinforcement learning for control, and simultaneous localization and mapping (SLAM);

Miscellaneous personal projects that I don't get bored in (like those shown below, and those you can find in my public repositories);

~~Necessities like busy undergraduate engineering academics.~~ I'm finally on my CO-OP year!

## Other Platforms

List of my Desmos graphs: https://harry7557558.github.io/desmos/

List of my Shadertoy shaders: https://harry7557558.github.io/shadertoy/


# Rendering and Visual Art

## Spirulae Online Function Grapher (March 2022, August 2022 - October 2024)

https://spirulae.github.io/ ([gallery of unfiltered renderings](https://spirulae.github.io/gallery))

![](./list-of-projects-src/d2bc53ed23f3f9273be6d360d9d37139.jpg)

I was inspired by raymarching demos on Shadertoy to create a WebGL online graphing calculator for 3D implicit surfaces, and I have been working on it constantly. Currently, spirulae has a 3D implicit surface grapher, a 3D parametric surface grapher, a path tracer, 2D and 3D complex function graphers, mesh generators, a vector field grapher, and robust equation parsing with support for custom variables and functions.

## “Man of La Mancha” Media Project (May 2022)

https://harry7557558.github.io/art/molm/

![](./list-of-projects-src/3630cfacf81862b858cf72c9af805c1d.jpg)

I made this artwork for a high school English course. I procedurally modeled several objects and rendered them using Monte Carlo path tracing in WebGL. I implemented the Cook-Torrance reflectance model, refractive materials, and emissive materials.

## AVI4M Independent Study Project (November 2021 - January 2022)

https://harry7557558.github.io/AVI4M-ISP/

![](./list-of-projects-src/9fa6c63aadf0696ea84c497072a2ae17.jpg)

I created this project for a high school art course. I developed an SDF visualization tool using volume rendering techniques and used it in CSG modeling. I implemented octree-based adaptive marching cubes for surface reconstruction and developed disambiguation techniques. I initially wrote path tracing rendering code from scratch. I later rendered the models in Blender to save time and meet the deadline.

## Volume Rendering Demo (October 2021)

https://harry7557558.github.io/Graphics/raytracing/webgl_volume/

![](./list-of-projects-src/b3e9e1c320d6ba508d0d1ddd4c1d2c77.jpg)

I played with volume rendering of medical imaging datasets in WebGL 2. I processed several popular CT and MRI scanning datasets into raw bytes using NumPy. I implemented volume rendering modes like MIP, X-ray, isosurface, volumetric integration, gradient-dependent transfer function, etc.

## IdentiEgg (July 2021)

https://harry7557558.github.io/art/dyed-egg/

I was inspired by WordPress identicon to generate identicon eggs. To make the shapes of the eggs match real-world eggs, I traced real-world eggs, fitted them to a linear least squares model, and plotted the parameter points in R³. I noticed the parameters are within an ellipsoid, so I applied principal component analysis to find the equation of the ellipsoid and derived an equation to generate uniformly distributed points in it without rejection sampling. I wrote code to minimize the height of the center of mass of eggs so they can be physically rested on a plane.

## “In Your Eyes” Art Project (December 2020)

https://harry7557558.github.io/Graphics/UI/Homework/AVI3M/

![](./list-of-projects-src/bd1e9c662fd8ad5eab61985ac9ae3ff4.jpg)

I generated 3D renderings of an eye model for a high school art project. The model was an implicit surface triangulated by the marching cube method, and I merged vertices that are too close with the help of the disjoint set data structure. I implemented Monte Carlo path tracing for rendering and played with specular, refractive, and glossy materials. I received a perfect score on this project.

## “The Glass” (May 2019)

https://github.com/harry7557558/Ray-Tracing

I created an animation for a high school art project and rendered it using ray tracing. I learned about matrix and vector algebra and object-oriented programming in C++. I also interpolated motion captured values using Fourier series.


# 3D Reconstruction and View Synthesis

## Gaussian Splatting (May 2024 - Present)

https://github.com/harry7557558/spirulae-splat

![](./list-of-projects-src/8e0e56eff52b929981a4ba59c57b36ef.jpg)

As prompted by a research project I did in my university, I gave a try to Gaussian splatting to digitalize real-world objects and scenes. Initially forked from the splatfacto method in nerfstudio, I experimented with various additions like 2DGS, polynomial kernels, per-pixel sorting, batching, exposure correction, exact camera distortion, UV-dependent color, direction-dependent background, depth supervision, segmentation, etc.

I ran my custom method on benchmark datasets, places around my school, and small objects. I made viewers running in browser, in Unity, and as a robot simulator that integrates with ROS. I tried effects like fisheye distortion, lighting effects, motion/defocus blur, and underwater. I also got good results by using it to generate synthetic data to train machine learning models.

## 3D Structure from Motion (April 2024 - July 2024)

https://github.com/harry7557558/Graphics/tree/master/mapping

![](./list-of-projects-src/9d8a7499ed86d92cafe30556112694a3.jpg)

Experimented with structure from motion (SfM) with videos captured with mobile cameras. Wrote Python/OpenCV script that select video frames based on amount of movement and motion blur, and incrementally add frames to a reconstructed scene. Experiemnted with techniques like feature detection and matching, optical flow, epipolar geometry, PnP, bundle adjustment, loop closure, etc. Each scene in the above image took 1-3 minutes to process. Demonstrated using recovered camera intrinsics, poses, and point cloud to train high-fidelity NeRF and Gaussian Splatting models.


# Geometry Processing

## 2D to 3D Converter (April 2023, November 2023 - January 2024)

https://harry7557558.github.io/img23d/ ([medium article](https://medium.com/@harry7557558/img23d-web-based-tool-that-turns-2d-images-into-3d-models-15c0d7382a08))

![](./list-of-projects-src/0de32173bf9f644efc3ae0c29504c12b.jpg)

• Trying to make a tool to inflate 2D images into 3D models after reading [Baran & Lehtinen's “Notes on inflating curves”](https://www.alecjacobson.com/weblog/?p=4613)  
• C++ code with mesh generation and numerically solving the Poisson equation, with command line and web interfaces

## Mesh Decimation for Marching Cubes (October 2023)

https://spirulae.github.io/meshgen3

![](./list-of-projects-src/d661d251f6677c0974f945b67ffde433.jpg)

• Intended to export [spirulae](https://spirulae.github.io) graphs into 3D models compatible with 3D modeling and animation software  
• Techniques: octree-based marching cubes; error quadrics, face and edge costs, valence balance; segment tree  
• Features: real-time dense marching cubes mesh, adaptive mesh with accurate Euler characteristics

## Implicit Mesh Smoothing Experiment (February 2022)

https://github.com/harry7557558/Graphics/tree/master/simulation/heatequ

Laplacian and Taubin smoothing; Finite difference method; Implicit method with conjugate gradient solver;

## Adaptive Parametric Surface Triangulation (December 2020)

https://github.com/harry7557558/Graphics/blob/master/triangulate/parametric_surface_adaptive_dist.h

Quadtree; Orthogonal approximation error; Tested on [artistic models](https://github.com/harry7557558/Graphics/blob/master/modeling/parametric/surfaces.h);


# Physics (static)

## Finite Element Analysis (December 2022 - February 2023)

https://github.com/harry7557558/Graphics/tree/master/simulation/fem/statics_le

![](./list-of-projects-src/7065d7e990c4e327aa6370b58188417f.jpg)

I experimented with solving 3D trusses using the stiffness method after learning about trusses in university, and I soon moved to write C++ code from scratch to analyze stress and deflection in solids. I researched strain and stress formulations, experimented with linear and quadratic tetrahedral elements of various shapes, different preconditioners for the conjugate gradient method, and mesh generation from implicit objects. I also implemented an OpenGL GUI to visualize results.

## Rigid Body Balancing (November 2020)

https://github.com/harry7557558/Graphics/tree/master/simulation/balance

I tried to find ways to place a rigid body on a plane to minimize the height of its center of mass. I did that for 2D shapes by finding the convex hull of Bézier splines. For 3D meshes, I extended the Nelder-Mead optimization algorithm to a unit sphere and used it to find a local optimal orientation.


# Physical Simulation

## Stable Fluids (September 2022)

https://harry7557558.github.io/Graphics/simulation/fluid_grid/jacobi_pressure/

![](./list-of-projects-src/777475f9d08a829ca51e8a04f2e52bb7.jpg)

I implemented a web-based fluid simulation demo after reading Jamie Wong’s blog post. I attempted a multigrid pressure solver and vorticity confinement.

## XPBD Cloth Simulation (August 2022)

https://github.com/harry7557558/Graphics/tree/master/simulation/mass_spring/xpbd_cloth

I implemented the Extended Position Based Dynamics (XPBD) method and applied it to simulating mass-spring models and cloth models. I researched solid elasticity and implemented the energy function and its analytical gradient. I compared XPBD results with the results of a conventional semi-implicit Euler solver.

## SPH Fluid Simulation (June 2021)

https://github.com/harry7557558/Graphics/tree/master/simulation/fluid

I tried the Smoothed Particle Hydrodynamics (SPH) method for simulating 2D and 3D liquids. I implemented a particle system, a grid for fast neighbor lookup, the semi-implicit Euler solver with splitting, and iterative solvers.


# Deep Learning

## Gate detection for Autonomous Drone Racing (November 2024 - April 2025)

![](./list-of-projects-src/9bd4835c1eaea726ac9d63e14a5e8214.jpg)

For my school design team, I developed a deep learning model that detects gates for autonomous drone racing. The model has YOLO-like outputs, involves CNN and attention in its architecture, and is trained on curated loss functions. Powered by large volume of synthetic data generated from Gaussian splatting, it can detect gates, assign ID to each detected gate, output corner points and depths with covariance, and directly output 6-DOF 3D pose between camera and gate with centimeter accuracy, across a range of camera intrinsics. With custom augmentation, the model works well in the presence of heavy shot noise, motion blur, and rolling shutter artifacts. For 1280x720 RGB images, model inference takes around 6.5ms on on a NVIDIA Jetson Orin 16GB.

## Path Tracing Denoise (September 2023 - April 2024)

https://spirulae.github.io/utmist-denoising/

![](./list-of-projects-src/7f05e1a0049186e16757c32adc9f746f.jpg)

My first professional collaborated project – Improving my [WebGL path tracer](https://spirulae.github.io/implicit3-rt) by incorporating deep learning denoising. We trained an U-Net model and wrote inference in WebGL, as well as adding more features to the path tracer to showcase our model's high generalizability to unseen cases. Our rendering and denoising run in real-time, achiving over 40 fps at 1024×768 resolution, completely inside a web browser.

## Face Generator (July 2022, November 2023)

https://harry7557558.github.io/Graphics/fitting/dcgan/ffhq_convtrans_vae_2/webgl/

![](./list-of-projects-src/4d14eb9fd4bc6d591034639121f1a77b.jpg)

I implemented a GAN neural network in PyTorch with a variational autoencoder and trained it on the FFHQ face database. I created a webpage that renders animated face transitions in real time, which inferences the model by loading binary weights into WebGL. I derived a mapping function that results in a uniform distribution when applied to linearly interpolated noise and used it to keep the diversity of faces in animation.

## Neural Network Written from Scratch (April 2022)

https://github.com/harry7557558/Graphics/tree/master/fitting

![](./list-of-projects-src/a8f8926baabc26c95540d802725bb889.jpg)

I tried to implement neural networks in C++ from scratch to see if they can overperform machine learning frameworks. I implemented dense, convolutional, and RBF layers, and SGD, Adam, and BFGS optimizers. I generated a grid of SDF values from a polygon mesh using breast-first search and fitted it to a SIREN neural model. I improved the algorithm by using quasi-random sampled data points in mini-batch training. I did several tests with different random number seeds and found that compared to TensorFlow, my code achieved half of the loss in a quarter of the time on average.


# Image and Signal Processing

## SVG to Desmos (March 2022)

https://github.com/harry7557558/svg-to-desmos

![](./list-of-projects-src/f7e39854080d192e7a394a665bddffa3.jpg)

After seeing other people’s projects exporting SVG images to the Desmos graphing calculator, I was intrigued to write my own but focus on size optimization. I wrote a Python script that parses SVG paths into Bézier splines, and applied arc-length parameterized discretization using Gaussian quadrature and the secant method. I compressed the paths using FFT and merged shapes with the same colors using an R-tree and a greedy algorithm. I was able to fit the entire Twemoji list (4000+ emojis, 7MB SVG) into a single Desmos graph with a size of less than 3 MB.

## Symbolic Procedural Noise Analysis (August 2021)

https://github.com/harry7557558/Graphics/tree/master/modeling/procedural/noise_stat

I tried to normalize noises used in procedural modeling to a fixed mean and variance on values and gradients. To simplify work and overcome the speed issue with SymPy, I implemented a Python class for the product of polynomials and trigonometric series that supports symbolic summation, multiplication, differentiation, and integration. I used it to compute the analytical variance of several noises and their gradients and validated my results using quasi-Monte Carlo simulation in C++.


# Numerical Optimization

## Model Predictive Contouring Control (May 2023 - August 2023)

For my school's design team, I implemented the quadrotor controller described in the paper [Model Predictive Contouring Control for Time-Optimal Quadrotor Flight](https://ieeexplore.ieee.org/document/9802523). The optimal controller is formulated as a constrained nonlinear optimization problem. I used Acados solver with CasADi for automatic differentiation. Miscellenous programming include arc-length parameterization of splines and integration with Gazebo simulator. I also proposed an original constraint to faciliate successful gate traversal.

## Color Function Fitting (May 2021)

https://github.com/harry7557558/Graphics/tree/master/UI/color_functions

![](./list-of-projects-src/3b9660aa366a96c384ded3d8ba1ea300.jpg)

I tried to fit Wolfram colormap functions and export them to personal projects. I implemented linear least squares for polynomial and trigonometric series models with varying numbers of terms. I also fit them to a frequency-dependent trigonometric model by setting the frequency to a numerical optimization parameter.

## Fitting Bézier Curves to Parametric Curves (October 2020)

https://github.com/harry7557558/Graphics/tree/master/fitting/parametric2bezier

I tried to fit Bézier splines to mathematical parametric curves without too many pieces. I researched, implemented, and compared techniques for finding the distance from a point to a cubic Bézier spline. I initially fit the curve with Gaussian quadrature and linear least squares. I later wrote code to discretize the parametric curve with the handling for different types of singularities, while minimizing the number of curve samples.


# Applications

## Desmos to 3D Model (January 2024)

https://github.com/harry7557558/desmos-to-3d-model

![](./list-of-projects-src/015152b712fef0e6fce022c8a9635de0.jpg)

Export graphs created in Desmos 3D Graphing Calculator to 3D models in formats like GLTF, OBJ, and STL that can be used for animation (eg. in Blender) and 3D printing.

## 3D Matrix Visualizer (July 2019, October 2022)

https://harry7557558.github.io/tools/matrixv.html

![](./list-of-projects-src/5ee9f338723d6c95e30029d5658f8596.jpg)

I wrote an online tool to visualize transformation matrices in computer graphics on an HTML5 canvas, which has several built-in 3D models and visualization of eigenpairs. It was updated in October 2022 to use the shifted QR algorithm for more accurate and stable eigenpair calculation. Currently, this tool has more than 600 Google search clicks per month according to Google Search Console.

## STL and PLY viewer (May 2020 - September 2021)

https://github.com/harry7557558/Graphics/blob/master/UI/ply_viewer.cpp

![](./list-of-projects-src/d1e025743dc363336d7dcbbd62ce70eb.jpg)

I created a Windows 3D model viewer for personal use and maintained it for more than one year. It is based on Win32 GUI with software rasterization. It implements different shading modes, restoring the connectivity of STL models using disjoint set data structure, and calculating physical quantities like the center of mass and inertia tensor using the divergence theorem.

## Chemical Equation Balancer (November 2019)

https://harry7557558.github.io/tools/chemequ.html

![](./list-of-projects-src/3f108e82013ec1a6d5706deb1260271a.jpg)

I learned the solution to homogeneous linear systems and applied it to balancing chemical equations. I implemented a chemical equation parser in JavaScript, a rational number class, and a Gaussian elimination solver. I applied integer congruence properties to find multiple rational solutions for linear systems with a nonzero solution space rank.


# Non-Programming Projects

TODO &ndash; 
Yes, I do have a list, must be something related to my [favorite colors and animals](https://github.com/harry7557558#user-profile-frame). Coming (probably) soon.


# Academic Publications

Not listed on this page – considering I've realized I'm not a fan of choosing a research topic and working on stuff only to make reviewers happy. But I'm pretty sure you can find my Google Scholar profile if you stalk me hard enough.
