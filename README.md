
---
**This project is an internal research project. I decided not to release code since I am not publishing a paper on this. Presentation slide contains enough explanation, see next section.**

**If you are interested in it, or have any question related to NFV or differential privacy, feel free to email me. If necessary, I can share code.**
---

# DP-messaging-nfv

This is a crypto research project.

We implemente a differential private (DP) messaging system using NFV technique, at George Washington University with Professor [Arkady Yerukhimovich](https://www2.seas.gwu.edu/~arkady/) . It is inspired by existing researches in the field like [Vuvuzela](https://www.freehaven.net/anonbib/cache/vuvuzela:sosp15.pdf), [Stadium](https://eprint.iacr.org/2016/943.pdf), and [Karaoke](https://people.csail.mit.edu/nickolai/papers/lazar-karaoke.pdf).

The testing enviorment is on [CloudLab](https://cloudlab.us/), to which we specially want to say THANK YOU!

## Motivation

As the dead-drop protocol was introduced by Vuvuzela, researches in differential private messaging has been becoming more active and more "private". However, limitations in current systems make them hard to use. The major limitation is high latency and high deployment cost.

To decouple the control panel and data panel of triditional network protocol stack, network function virtualization (NFV) and software-defined network (SDN) is proposed to make network programmable. With the introduction of NFV, such DP-messaging system would be able to have lower latency and cost.

## In-Dev

- [x] Client + Noise generation
- [x] NF architecture
- [x] Shuffling NF
- [x] Dead-drop NF
- [x] Verification using bloom filter
- [x] Research project report and [presentation slide](https://docs.google.com/presentation/d/1D8Y94qmM55OrBm45_cEeT10cFFVEJ8jcuBEv8ibcAZc/edit?usp=sharing).

Another interesting result is we found a mistake in Stadium's implementation, which might lead to failure of achieving their privacy guarantee.

## Todo

- [ ] Meet-in-middle privacy protocol
- [ ] Topology-based privacy protocol
- [ ] TCP-based transmission (low priority)
- [ ] Fault Tolerance (low priority)

Planning to finish one of above directions, then we will publish a paper.
