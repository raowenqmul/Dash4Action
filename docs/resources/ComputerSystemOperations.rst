Computer System Operations
=====

The way in which a computer system is operated can have a significant impact on its operational carbon emissions.  

Tuning of the system is key here.  While the goal should almost always
be to maximise science output (i.e. minimum runtime), there are
situations in which the tradeoff between increased runtime and reduced
power consumption makes this worth while.  One should consider that
increasing the runtime of a workload will reduce the science output of
the HPC system (for a fully occupied system) over its lifetime, thus
making the CO2 per science ratio worse.  In cases where utilisation of
the system is low (e.g. less than 90%), it may make sense to reduce
power consumption regardless of the effect on runtime, since this will
simply increase the utilisation.

There are many different parameters that can be tuned including:

* CPU frequency control (BIOS or OS) and governor
* Memory frequency
* Use of C-states and downclocking
* GPU frequency
* Node powercaps
* Random BIOS options which may have a small effect
  
Many of these are user-configurable, and thus can be set in batch jobs.

If you have an underutilised system, consider allowing nodes to power
off when not required.  Slurm, and other batch schedulers, have
functionality to enable this.

The user management perspective
========

From a user management perspective, there is much that can be done to compute
responsibly.

Workloads should be optimised, with performance improved via
benchmarking and code improvements, to reduce runtimes and maximise
efficiency.  This can be aided by offering RSE time.

However, it is important to have a "Sufficiency" mindset and avoid the
Rebound Effect: If the codes just run faster, this does not mean that
the user should then just run more jobs to fill up the space.  Rather,
in the long term, it should result in smaller systems being specified
in the future.

Training is available in all of these aspects.  In particular, green
skills training could be considered a prerequisite for system usage.

On systems with low utilisation, green scheduling algorithms can be
considered, i.e. delaying job start time until periods of low grid
carbon intensity.  Of course, purchasing a smaller system in the first
place would have been a better solution due to the high embodied
carbon, and the idle node power consumption.

RSE training can be key to increasing the efficiency of systems.  End
user training and an embedded curriculum will also help.  Digital RTPs
can keep an eye on their systems, identifying nodes that are not well
used, and consolidating these where appropriate.

