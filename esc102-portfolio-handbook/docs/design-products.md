# Personal Engineering Design Products

This page lists the products of my engineering design activities in the past year, since September 2022. As per assignment requirements, I write this page to present what are done to an external audience with no prior knowledge of the projects. While not focusing on the process and takeaways, they will connect with my positions mentioned on the previous page.


## Personal Programming Projects

As mentioned before, I created a lot of personal projects purely out of passion and to demonstrate my skills to myself. Most of them are not stunning products but focused on what I "like" rather than what I "need", and therefore a lot of them are experimental and ongoing. I don't have a particular goal for them, and I feel I'm more free when I don't have to work toward an objective, which can be hard to achieve due to hyperfocus. I also have multiple projects running at the same time and frequently start new projects, since I may become bored at one project, and I can always choose to switch back later. Some noticeable ones in the past year are the Spirula function grapher, the FEM mesh generation experiment, and the 3D matrix visualizer.

### Spirula Function Grapher

The [Spirula function grapher](https://harry7557558.github.io/spirula/) is a web-based tool that instantly renders user-input mathematical functions. The interface is very simple: the user enters a function on the box on the top right, and the tool displays it. It supports explicit, implicit, and parametric equations, as well as functions defined in complex domains.

![](img/spirula.jpg)

I created it out of my passion in computer graphics, my need for fast visualization of 3D implicit surfaces, and the lack of such a tool I can find om the internet. I have been maintaining and constantly updating this tool since April 2022, for my demand for additional features during use and as passion activities: it initially only graphs 3D implicit surfaces, but I implemented complex domain coloring in 2D and 3D in October 2022, updated the parser in January 2022, added support for parametric surfaces in February 2022, added several non-elementary functions in March 2022, and I still have plans for more functionality like automatic differentiation and exporting 3D models. I like how this project has different parts requiring different knowledge and techniques, allowing me to switch between them and reduce mental fatigue.

![](img/spirula-complex.jpg)

<p class="caption" markdown="1">
A function over the complex domain graphed in Spirula
</p>

Other they me enjoying the creation process, the product has benefitted me in unintentional ways. I often use Spirula as a tool to create artworks: since I'm weak in communication and often experience frustration, I use 3D modeling artwork as therapy. I would say it's much more effective than most traditional and digital arts that can take a long time to see the result: Spirula renders it immediately as I update an equation, and there's still rooms for me to tweak the parameters and refine the results. I share the results on social media and received positive feedback, which I think have improved my confidence over my programming strength. While there are numorous thankful emails and feature requests from people who found my works on the internet and benefit from them, and they inspired to create more functionality like animation, I still view this tool as something I created for myself and became proud of my ability.


<img src="../img/spirula-jellyfish.jpg" style="width:46%;display:inline"></img>
<img src="../img/spirula-implicit.jpg" style="width:51%;display:inline"></img>
![](img/spirula-xray.jpg)

<p class="caption" markdown="1">
Some artworks I created using Spirula.
<br/>
*Left*: a jellyfish created through the parametric surface grapher
<br/>
*Right*: the Mandelbulb over toric coordinates through the implicit surface grapher
<br/>
*Bottom*: X-ray mode of the parametric surface grapher based on the [physically-based X-ray model](https://en.wikipedia.org/wiki/Beer%E2%80%93Lambert_law)
</p>


### The Matrix Visualizer

I created the [matrix visualizer](https://harry7557558.github.io/tools/matrixv.html#) in 2019 to visualize matrix transformation when I just started learning linear algebra. The internal algorithm of the tool was heavily updated in November 2022. It visualizes 2D and 3D transformation matrices as well as 4D affine matrices. It has computation of determinant and eigensystem and visualization for eigenvectors. It also allows users to try different models with varying symmetry.

I was researching the QR eigenvalue algorithm for another personal project, and I decided to update this tool as an exercise, and considering it's "grade-school" eigensystem computation was very unstable in practice. The updated algorithm was much more robust over arbitrary user inputs and edge cases, and the addition of the sphere model reduced anisotropy in visualization. According to Google Search Console, the tool received more than 2000 Google search clicks in the past 3 months, confirming the impact of my technical strength.

![](img/matrixv.png)

<p class="caption" markdown="1">
Interface of the matrix visualizer. I implemented link sharing after seeing the popularity of my tool. You can see an example here: [http://harry7557558.github.io/tools/matrixv.html#m=1,1,1;1,1,0;1,0,1&g=isosphere&s=2&tf=0](http://harry7557558.github.io/tools/matrixv.html#m=1,1,1;1,1,0;1,0,1&g=isosphere&s=2&tf=0)
</p>



### FEM Mesh Generation



## Praxis II: The Nurdle Filter
 - Background: AGF
 - Features
 - Passionate about

## Praxis I: Foggy Glasses Solutions
 - 

## CIV102 Bridge Project
 - An entire optimization framework written independently from scratch
 - Paper bridge hold 400N train
 - Where I learned from failure
