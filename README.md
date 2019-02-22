# DP-messaging-nfv

This is a crypto research project.

We implemente a differential private (DP) messaging system using NFV technique, at George Washington University with Professor [Arkady Yerukhimovich](https://www2.seas.gwu.edu/~arkady/) . It is inspired by existing researches in the field like [Vuvuzela](https://www.freehaven.net/anonbib/cache/vuvuzela:sosp15.pdf), [Stadium](https://eprint.iacr.org/2016/943.pdf), and [Karaoke](https://people.csail.mit.edu/nickolai/papers/lazar-karaoke.pdf).

## Motivation

As the dead-drop protocol was introduced by Vuvuzela, researches in differential private messaging has been becoming more active and more "private". However, limitations in current systems make them hard to use. The major limitation is high latency and high deployment cost.

To decouple the control panel and data panel of triditional network protocol stack, network function virtualization (NFV) and software-defined network (SDN) is proposed to make network programmable. With the introduction of NFV, such DP-messaging system would be able to have lower latency and cost.

## In-Dev

- Noise generation
- Shuffling net using NFV
- Dead-drop
- Verification using bloom filter

## Todo (Under change)

- [ ] Meet in middle protocol
- [ ] Protection protocol
- [ ] Potential topology protocol
- [ ] TCP-based transmission
- [ ] Fault Tolerance

---
The testing enviorment is on [CloudLab](https://cloudlab.us/), to which we specially want to say THANK YOU!
