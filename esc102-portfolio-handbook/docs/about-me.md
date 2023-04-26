# About Me
--------

This is where you can find an overview of my position: my belief and bias, my unique understanding of engineering design process, my values and skills, as well as my weaknesses and how I overcome them. I tried to support most of these with arguments and evidences, but I found they can be sometimes easier to follow and understand if I just state them, so I decided to leave supporting evidence to later parts of this document.

If you are a member of the ESC102 teaching team, you may have already be familiar with me through various ways including but not limited to my submitted assignments and tutorial activites, and I hope this can help you see a process of how I struggled to understand myself and engineering design. If you are just a visitor from the internet who scrolled to this page, I just want to show you that I'm not a "normal" human to be treated "normally", as well as present some of my unique understandings.

![functional-conch](img/functional-conch.jpg)

<p class="caption" markdown="1">
A [digital rendering of a conch](https://www.shadertoy.com/view/Nt2yW3) I created in mid-2022. I enjoy programming, and I have a special fascination with beaches, spirals, and seashells.
</p>

<br/>

# Overview

While I scoped out all information regarding my mental condition and difficulties I've faced in this document, I characterize myself as a highly individualized and reflective person. I engage little in popular entertainment activities, but spend most of my spare time on personal programming projects and experiments. I frequently reflect on activites I engaged in, connecting the results and processes, trying to find out the cause of my failure and what's wrong with me. I pay attention to a lot of details and often believe things have meanings.

I'm extremely passionate about certain areas of STEM, mostly computer programming, with specific areas like numerical algorithms, geometry processing, and interactive visualization, which I explored in my programming activities. It's possibly that I do programming because I don't have access to tools other than a laptop, and I may find other passions when I get better conditions, but at least programming is what I will answer as my hobby when being asked about. I feel I'm sometimes too passinate that I connect everything with programming, which may not always be the most suitable way.

Communication and teamwork is where I found myself difficult in. If I need to use one word to describe my situation on these, the word would be "cursed." I could say when I was in high school teams, there were only three outcomes: either I did everything, or other teammates did everything and I did nothing, or our team messed up. In university courses where we were required to work as an integrated team, the outcome is a combination of the three: we divided our tasks and work on our own, and at the end there was lots of discrepancies in our team. I reflected on observations of our communication and came out with lots of potential causes and fixes, but I just kept messing up, and I seem to be the person bringing curse into every team that I'm in.

Based on my individualized background, I personally view engineering design as a fun activity where I find challenge, and I found enjoyment working on them for passion and possibly kill time, but I don't have much expectation for it to be practical or beneficial. I often feel the need to isolate myself from society so I can enjoy my own design activities, without bringing curse to any group who does engineering design for a "conventional" purpose.

![sunnyside-beach](img/sunnyside-beach.jpg)

<p class="caption" markdown="1">
Sunnyside beach. During the Praxis II design activity, I visited the beach 4 times (3 times independently) to collect information and test prototypes. My final design has an outstanding performance, but our showcase presentation was poorly organized, and there were lots of discrepancy among team members.
</p>

<br/>



# Engineering Design: An Optimization Problem

Combining what I learned in the Praxis courses and my experience in personal programming activities, I present my understanding of engineering design as an optimization problem. I couldn't find a description of a similar analogy elsewhere so I consider this as my unique understanding.

In applied mathematics and science, a common problem is finding the extremum of a mathematical function. For example, in aerospace, one would try to maximize a function that takes the amount of fuel in each layer of a rocket and outputs the height traveled; In finance, one would try to maximize a function that takes the price of a product and outputs the net profit; In CAD modeling and graphics design, a program would try to minimize the error between a smooth spline and a hand-sketched path. Some optimization problems have constraints, like the amount of fuels in each layer must be non-negative, and the spline must start and end at specific points.

Given a function where you want to minimize (or maximize, but here I use minimize by convention), one way to solve the optimization problem is [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent): if you know the direction the function goes down, just keep going in that direction and keep going down until you can't go down anymore, and you arrive at the minimum.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Gradient_descent.svg/800px-Gradient_descent.svg.png" style="width:25%;display:inline"></img>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Goldstein_Price_function.pdf/page1-1200px-Goldstein_Price_function.pdf.jpg" style="width:35%;display:inline"></img>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Ackley%27s_function.pdf/page1-1200px-Ackley%27s_function.pdf.jpg" style="width:35%;display:inline"></img>

<p class="caption" markdown="1">
*Left*: how gradient descent arrives at the minimum.
<br/>
*Middle*: a function where the global minimum can be arrived at through gradient descent.
<br/>
*Right*: a function with many local minima, gradient descent would find a poor local minimum instead of the "best" global minima.
</p>

However, 

 - Mathematical optimization: find a global minimum
 - Can be quantized through framing, but not required
 - Go fast -> not optimal
 - FDCR: genetic algorithm
 - Iterative design: gradient descent
 - Judgement before testing to save effort

<br/>

# Values and Skills

I consider myself to have several strong areas that have committed to my success in individual work. Here I describe my strong intuition, strong motivation, and self-reflection.

**Strong intuition.** I was born with a strong intuition and common sense for the physical world and technical areas. This made me understand how things work easily, both theoretically and empirically; and after I understand how things work, I can easily tell potential benefits and issues of a technique or approach and how to reduce issues. This intuition has contributed significantly to my independent projects and problem-solving activities. My intuition also made me learn new things fast and easily become comfortable with a tool someone else created, even if there is little documentation, which made me quickly learn tools ranging from hand tool to household appliances to CAD software to programming interfaces.

**Strong motivation.** I am enthuasiastic in numerous areas of STEM. I like trying and testing the result of techniques by my own hand, but I don't reject theoretical understanding and divergent thinking activities. While my activity is mostly limited to software due to material restriction, previous experiences have shown I enjoy activites related to mechatronics and chemistry when I get better conditions. My enthuasiasm not only made me spend most of my spare time exploring STEM (like mentioned previously), but also made me maintain my interest throughout a number of school projects.

**Self reflection.** I consider myself a reflective person. When I feel I need a break from STEM activities, I often start reflecting on myself without intention. I often come out with unique understanding of things and insights into my previous failure experiences, which can be helpful applying suitable techniques and avoiding similar failures from happening again. One example of a result of my reflection is the understanding of engineering design as an optimization problem.

 - Strong intuition: understanding, learning, analyzing, using things
 - Reflective: identify the causes of failure and success
 - Concentration without distraction

<br/>

# Weaknesses

My numerous noticed weaknesses are related to my values and skills, as well as communication and managing conflicts. Attempts have been made to overcome these conflicts and maintain my optimism for the outcome of engineering design activities and personal development.

**Hyperfocus.** I consider hyperfocus to be my strongest weakness in completing projects, including but not limited to engineering design activities. According to a research published in 2019, "‘Hyperfocus’ is a phenomenon that reflects one’s complete absorption in a task, to a point where a person appears to completely ignore or ‘tune out’ everything else.", which was the case for my numerous school assignments and projects and a large number of personal projects. This is closely related to my enthuasiasm: when I'm extremely enthuasiastic about something, I focus on the part I'm enthuasiastic about and overlook other important aspects, like how I often do an assignment without carefully reading the instruction, and start prototyping and testing in a personal project without going through much secondary research and analysis. I consider that my strong intuition to be worsening this, because it made me not approaching concepts and tasks rigorously and systematically, and therefore I spend more time trying to figure out the less important parts.

And considering my reflective nature, when I think 

**Communication and conflict management.**



 - Enthuasiasm -> overlook important things, hand on without through research, can lead to depression instead; follow plan, set timer
 - Reflective -> excessive pride and inferiority, daydreaming
 - Difficult to let go
 - Communication: just cursed, lack of empathy; isolation is a solution?
 - Strong intuition -> not rigorously and systematically

<br/>

# Position Statement


<br/>

## References

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7851038/

https://en.wikipedia.org/wiki/Hyperfocus

https://en.wikipedia.org/wiki/Flow_(psychology)

Objective
 - Represent a personal position on engineering design that enables you to effectively manage your engineering design activities and teams.
