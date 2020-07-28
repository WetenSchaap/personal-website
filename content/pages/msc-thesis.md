
title: MSc Thesis
date: 2020-07-28
modified: 2020-07-28

I performed my MSc thesis in 2016-2017 under supervision of [Ilse van Hees](https://orcid.org/0000-0001-7261-3699) and [Marleen Kamperman](https://orcid.org/0000-0002-0520-4534) (currently full professor at the University of Groningen) in the [Physical Chemistry and Soft Matter group](https://www.wur.nl/en/Research-Results/Chair-groups/Agrotechnology-and-Food-Sciences/Physical-Chemistry-and-Soft-Matter.htm) at Wageningen University. 

In this project, I explored the coacervation behaviour of temperature responsive polyelectrolytes. Of course, I wrote a report on this thesis, which is available upon request, if you really want it. However, a [paper](https://doi.org/10.1039/c9py00250b) was published about this work (and even a bit more!) so I suggest you go read that. It is probably written better, misses all the uninteresting technical details, and is also about 50 pages shorter.

If you want a short(-ish) readable, understandable version of my work, keep reading! Before we go any deeper, it is probably best to give you some background on [polyelectrolytes](https://en.wikipedia.org/wiki/Polyelectrolyte) (fancy name for polymers with charged monomers) and coacervation. If you know this, you may want to skip the following section.
# Polyelectrolytes, Coacervation, and Salts
It may be somewhat unsurprising, but when you take a positively charged polyelectrolyte (dissolved in water), and mix it with an negatively charged polyelectrolyte, the polymers tend to attract each other, form a complex, demix from the solvent, and fall out of the original solution. The new concentrated phase consists of both types of electrolytes and a lot of water (up to 80% water in fact, somewhat surprising considering I just called this the 'concentrated' phase). This process is what we call "[complex coacervation](https://en.wikipedia.org/wiki/Coacervate)", and the concentrated phase it produces is called a "complex coacervate". Why such an uninteresting name? No idea. The complex coacervate is typically a gooey, slimy substance, with a very low interfacial tension with water. I should add a picture here!

As mentioned, this complex coacervation typically takes place between 2 oppositely charged polyelectrolytes, and is not caused by electrostatic effects (as you may expect), but due to the entropic gain of the displacement of counter-ions on the polyelectrolytes. This means that the amount and type of salt can strongly influence how strongly the polyelectrolytes bond each other.

# Coacervate as a glue?
Now, as I mentioned, a complex coacervate is a somewhat slimy substance, not unlike unset glue. This gives us an idea. Maybe we can use it to make glue? 

To make glue (or formally, an [adhesive](https://en.wikipedia.org/wiki/Adhesive)), we want a material with 3 properties:
 1. Glue must be a cohesive liquid, meaning it should sort of stay together, e.g. it must be sort of slimy
 2. Glue can be applied to a surface, and spread over the surface covering any roughness or cracks.
 3. Glue must be able to cure - it must go from its 'spread over cracks and connect to surfaces'-mode to a strong, hard material that is strongly bonded to the surface somehow. Typically this curing occurs through crosslinking of polymers in the glue, after an external trigger, like heat, radiation, or the addition of a second component.

So the very nice property of our glue is that it is indeed a cohesive liquid, which can be applied to a surface, even underwater! Most glues do not work, or hardly work, when in a wet environment. This is a very nice property, because many people try to make glue for medical purposes: it would be nice to glue an organ back together after surgery, instead of using stitches (for a variety of reasons, but most easy to imagine is the fact that a stitch inherently requires you to poke even more holes in already damaged person). 

So the component we are missing right now is something to cure our glue. How can we make our coacervate grow hard due to a trigger we provide? Here we find our inspiration in nature. It turns out that a so-called [sandcastle worm](https://en.wikipedia.org/wiki/Phragmatopoma_californica) already makes coacervate-based adhesives. It uses it to build a small house from sand (hence the name). To cure its coacervates, it uses a pH trigger. (Of course, this is why we started looking into this in the first place, but that would make for a confusing introduction.)

We prefer not to work with pH but with an easier to control variable: temperature. To make our coacervate glue set, we are going to build a two step mechanism: first we have the two polyelectrolytes come together and form a coacervate. This coacervate can be applied to the surface we are trying to glue. Then, we increase the temperature, and another component causes the coacervate to harden out, and things are glued together.

So, how do we go about this, how do we get a temperature controlled hardening? Our solution is [PNIPAM](https://en.wikipedia.org/wiki/Poly%28N-isopropylacrylamide%29), a polymer that is pretty boring and water-soluable at room temperature, but changes it behaviour when it is heated above ~32 degrees C: it demixes from water and starts sticking to itself (this is the so called [LCST](https://en.wikipedia.org/wiki/Lower_critical_solution_temperature)) . Why this happens exactly is at the moment not super relevant, but it is all quite interesting, and worthy of study in its own right. Important to mention here is that if you add salt to the PNIPAM solution, you decrease this LCST, you can go even to below the freezing point if you just keep adding salt!

The solution we have now constructed is, in theory pretty simple: we make 2 types of special polymers, each made of two parts (so called [block-copolymers](https://en.wikipedia.org/wiki/Copolymer)). The first part of the polymer is a charged bit, either positive or negative, and the second part of the polymer is PNIPAM. In theory, this could react the way we want to, creating a glue that I have described but in practice, life is almost always more complicated.
# What actually happened
Well in fact, things sort of worked the way we expect, only, more is happening then we expected! We get an entire phase diagram of behaviours. It turns out that depending on the salt concentration and the temperature of the samples, you get wildly different behaviours from the polymer mixture. I will guide you trough it quickly.

At very high salt concentrations, the coacervate does not want to form, because the driving force (releasing salt into the solution) is basically gone. But, as you have added a lot of salt, the PNIPAM LCST is below room temperature, and thus all the PNIPAM tries to stick together. This causes the formation of so called PNIPAM cored [micelles](https://en.wikipedia.org/wiki/Micelle), basically, you have little balls with a core of PNIPAM from several polymers stuck together, and several strands of charged polymer standing out from that, in such a way no more PNIPAM can be added to this ball.

At lower salt concentration (but still room temperature), we get so called coacervate cored micelles, the opposite situation of earlier. Now, because the salt concentration is lower, the polyelectrolytes try to stick together to form a coacervate, but the PNIPAM wants to be dissolved in water, because we are below its LCST! This leads to again, balls, now with a core of coacervate, and a bunch of PNIPAM polymers standing out, making sure not more coacervate can join the ball in the center.

Now, if we start at this situation and increase the temperature, we cross the LCST of PNIPAM, and it no longer wants to dissolve in water, and tries to find other PNIPAM to stick to. This is what we originally wanted, and indeed what happens is that everything starts to stick together, leading to a though solid coacervate falling out of the solution.

Now of course, since this is the stuff we were looking for, we want to do all kinds of tests to see how sticky it is, how strong it is, etc., etc., but, unfortunatly for me, my time was up, my thesis had to be handed in, and thus I did not have time to do any more work. I left it up to my supervisors to finish up, and luckily for me, they did.

There are some more things to say about what phases form and how they behave, but then we must go a bit deeper. I think at that point you are better of just reading the paper about this work if you want to know more, so I won't go any further here.

