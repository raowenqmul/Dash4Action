Computer System Design & Procurement
====================================

Computer System Design
----

Reducing the environmental footprint of Digital Research Infrastructure
(DRI) requires addressing both operational efficiency across the system
lifecycle and the upfront environmental cost of acquiring new hardware.
Decisions made during architecture design and procurement lock in
baseline power draw, cooling demand, and embodied emissions for the
service life of the service or facility.

Before procuring replacement equipment, organisations should consider
whether hardware refresh is necessary. Extending the operational life of
equipment through upgrades, refurbishment or repurposing can often
reduce lifecycle carbon emissions more effectively than replacing
equipment with newer, more efficient alternatives.

Systems designers are already familiar with operating within design
constraints. To address environmental sustainability, designers should
consider carbon cost as an additional design constraint alongside
monetary cost, power, space and performance.

There are a number of aspects to systems design and specification work
that are worthy of consideration. A number of these are explained in the
preamble of the SPARKHub “DRI Sustainability Procurement Questions”
document [1] and some are also considered here.

A common theme across sustainable DRI design is that technologies should
be selected to meet service requirements rather than maximising
performance in isolation. Over-specification can increase both embodied
and operational carbon without delivering meaningful benefit to research
outputs.

Bespoke design principles are key to optimising system designs: the
system should be designed for the research that it is intended to do,
which will lead to optimal workloads and minimal wastage.
Over-specifying a system is not in anyone’s interest, resulting in
wasted compute, idle cycles and unnecessary expense and carbon.

Appropriate Accelerator Choice 
~~~~

As Maslow observed, if all you have is a hammer, everything starts to
look like a nail. The same principle applies to computing: no single
accelerator is optimal for every workload, and selecting the appropriate
technology is essential to achieving the best energy and carbon
efficiency.

Studies such as ENERGETIC [2] have demonstrated that significant
reductions in energy consumption can be achieved through careful
matching of applications to hardware architectures and through
optimisation of software for the target platform. While accelerators
such as GPUs can substantially reduce energy-to-solution for suitable
workloads, they are not universally advantageous. Some problems are
better suited to FPGAs, AI accelerators, or simply CPUs. Memory-bound,
communication-bound, or poorly optimised applications may realise
limited performance benefit on a GPU while still incurring the embodied
and operational costs associated with accelerator infrastructure.

System designers should therefore evaluate architectures using measures
such as energy-to-solution and carbon-to-solution, rather than focusing
solely on peak performance. Consideration should be given to expected
utilisation, software portability, cooling requirements, embodied
carbon, and the characteristics of representative workloads. In many
cases the most sustainable solution is not the most powerful accelerator
available, but the technology that delivers the required scientific
outcome with the lowest overall environmental impact across its
lifetime.

Appropriate Choice of Storage
~~~~

Storage technology can have a significant impact on both operational and
embodied carbon. However, the most sustainable storage solution depends
strongly on workload requirements and data access patterns. Solid State
Drives (SSDs) offer low latency and high input/output performance,
making them suitable where rapid or highly concurrent data access is
required. Hard Disk Drives (HDDs) provide very high storage capacities
at relatively low cost and embodied carbon per TB, making them well
suited to large active data collections where access performance
requirements are less demanding. Magnetic tape offers very low
operational energy consumption for infrequently accessed data and
remains one of the most sustainable options for long-term archival
storage. Consequently, the most sustainable storage architecture will
often combine SSDs, HDDs and tape in a tiered hierarchy matched to the
required performance, capacity and data retention requirements.

SSDs are good for:

- Data requiring low-latency or highly concurrent access.
- Scratch and temporary storage where high I/O performance is required.
- Metadata-intensive workloads involving large numbers of small files.
- Workflows where improved storage performance significantly reduces
  overall time-to-solution.

HDDs are good for:

- Large active datasets where capacity is more important than maximum
  performance.
- Project and group storage with moderate access frequency.
- Data repositories and services with predictable throughput
  requirements.
- Situations where low embodied carbon (~8x lower than SSD per TB) and cost per TB are important
  considerations.

Tape is good for:

- Long-term archival and preservation of research data.
- Backup and disaster recovery copies.
- Compliance, retention, and records-management requirements.
- Data that must be retained but is rarely accessed.

| As with accelerator selection, storage should be selected by matching
  the technology to the data lifecycle. High-performance storage should
  be reserved for datasets that genuinely require it, while inactive or
  rarely accessed data should be migrated to lower-carbon and lower-cost
  storage tiers wherever practical.
| Retaining unnecessary data has environmental costs. Data retention
  policies and periodic review of inactive datasets should therefore
  form part of a sustainable storage strategy.

In short data should be stored on the lowest-performance storage tier
that continues to meet the required service level for access time,
throughput, resilience and retention.

Appropriate Choice of Networking Equipment
~~~~

Network infrastructure contributes to both the embodied and operational
carbon footprint of DRI facilities. High-performance interconnects,
optical networking equipment, routers and switches can consume
significant power throughout their operational lifetime while also
carrying substantial embodied carbon from manufacture.

As with compute and storage infrastructure, the most sustainable
networking solution depends upon workload requirements. High-bandwidth,
low-latency interconnects provide substantial benefits for tightly
coupled parallel applications and distributed storage systems, but may
deliver little practical advantage for workloads dominated by
independent tasks or modest data transfer requirements.

When specifying network infrastructure, consideration should be given
to:

- Required bandwidth and projected traffic volumes.
- Latency sensitivity of applications.
- Oversubscription ratios and anticipated utilisation.
- Power consumption of switches, routers and optical transceivers.
- Embodied carbon associated with network equipment and cabling.
- Expected equipment lifetime and upgrade cycles.

Over-specification of networking infrastructure can increase both
embodied and operational carbon without delivering meaningful scientific
benefit. Conversely, under-specification may result in inefficient
resource utilisation, extended job runtimes and reduced system
effectiveness. Network design should therefore be based on measured or
anticipated workload requirements rather than selecting the
highest-performance option available.

Network infrastructure should be designed to deliver the required
bandwidth, latency and resilience with the minimum practical quantity of
active equipment.

Optimise utilisation and power efficiency
~~~~

Often utilisation and power efficiency can be optimised while a DRI is
operational, through configuration and software optimisation. However it
is still a consideration at systems design time.

Highly utilised systems generally deliver more useful work per unit of
embodied carbon and can therefore reduce the Scope 3 impact attributed
to individual services or users. In the design context this encourages
service consolidation using on-premises cloud and virtualisation
technologies which can help minimise the number of servers required
helping to reduce scope 3 footprint.

In many cases increasing utilisation delivers greater sustainability
benefits than marginal improvements in equipment efficiency.
Under-utilised infrastructure incurs embodied carbon costs regardless of
whether it is actively performing useful work.

Service consolidation using virtualisation, containerisation and cloud
technologies can improve utilisation and reduce the number of physical
systems required.

Some critical infrastructure services may still need to run on dedicated
hardware for reasons of security, resilience or operational simplicity.
In such cases, consideration should be given to appropriately sized
low-power devices, including single board computers, where these can
meet service requirements.

Procurement
----

| Design decisions determine much of a system’s environmental footprint,
  but the procurement process provides the opportunity to gather
  evidence, assess suppliers and formally incorporate sustainability
  objectives into purchasing decisions.
| Essentially by including environmental sustainability criteria to
  tendering assessments we can balance NetZero and other sustainability
  issues against price and performance.

Procurement activity should begin by confirming that replacement is
genuinely required and that options for extending the service life of
existing assets have been fully considered.

Sustainability Requirements
~~~~

Environmental sustainability criteria should be considered alongside
price, performance, functionality, resilience and support requirements
during supplier evaluation. Sustainability considerations can be
incorporated into both mandatory requirements and scored assessment
criteria[1].

Areas that may be considered include:

- Operational energy efficiency and expected power consumption under
  representative workloads.
- Embodied carbon associated with manufacture, transport and end-of-life
  processing.
- Product longevity and expected service life.
- Availability of firmware updates, maintenance contracts and long-term
  vendor support.
- Repairability and availability of spare parts.
- Upgrade paths that allow equipment life extension.
- Packaging reduction and sustainable logistics.
- Vendor take-back, refurbishment and recycling programmes.
- Supplier environmental management systems, sustainability policies and
  Net Zero commitments.


Requesting Carbon Information 
~~~~

Estimating operational energy consumption (Scope 2 emissions) is relatively 
straightforward and, as part of a large procurement, it may be possible to 
obtain access to representative hardware for benchmarking and power measurements 
under realistic workloads.


Assessing Scope 3 carbon footprint is considerably more challenging and 
generally requires vendor engagement. The tendering and procurement process 
therefore provides an important opportunity to request Product Carbon Footprints 
(PCFs), Life Cycle Assessments (LCAs), environmental product declarations and 
other sustainability information from suppliers. This information can then be 
used to compare competing solutions on a more complete lifecycle basis rather 
than considering operational power consumption alone.

Where sustainability data is unavailable, suppliers should be encouraged to 
explain the methodology used to estimate environmental impacts and identify any 
significant assumptions or exclusions.

Procurement Resources
~~~~

A number of university purchasing consortia have adopted the “Sustain
Supply Chain Code of Conduct”. This seems like a sensible minimum
baseline to sustainable procurement [3].

Detailed sustainability procurement questions for DRI and example tender
requirements can be found in the SPARKHub “DRI Sustainability
Procurement Specifications and Questions” document [1].

Additionally London Universities Purchasing Consortium (LUPC) has
developed a Carbon Toolkit [4] which has been adopted across UK
Universities Purchasing Consortia (UKUPC). This addresses PPN 06/21 and
is a useful reference (especially appendix B).



References
----

| [1] “DRI Sustainability Procurement Specifications and Questions.”
  NetDRIVE & SPARKHub. (2026).
  https://sparkhub.eu/wp-content/uploads/2026/04/DRI-Sustainability-Procurement-Specs-Questions-26.03.26.docx
| also linked via https://uknetdrive.org/resources

[2] Final Report of ENergy-aware hEteRoGenEous compuTIng at sCale
project (ENERGETIC) Michael K. Bane et al. (2023).
https://doi.org/10.23634/MMU.00631226

| [3] “Sustain Supply Chain Code of Conduct” AUPC (2025)
| https://www.apuc-scot.ac.uk/wp-content/uploads/2026/04/Updated-SSCCoC-published-Dec-2025-PDF.pdf

| [4] “Carbon Toolkit” LUPC
| https://www.lupc.ac.uk/responsible-procurement/responsible-procurement/carbon-toolkit/
