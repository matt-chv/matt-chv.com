Title: The Bear and the Sloth - the secret of energy harvesting
Date: 2015-09-29
Category: blog
Tags: energy_harvesting
Slug: bear-and-sloth.md
cover_image_url: BearAndTheSloth.png
cover_image_caption: The bear and the sloth
cover_art_url: BearAndTheSloth.png
Summary: The Bear and the Slot - the secret of energy harvesting

# The secrets of energy harvesting: The sloth and the bear

> originally posted [here](https://e2e.ti.com/blogs_/b/industrial_strength/posts/the-secrets-of-energy-harvesting-the-sloth-and-the-bear)

Industry 4.0 is a term that describes the vision that cyberphysical systems will revolutionize factories. In a recent German-language article on the concept, I discussed how industrial revolutions have so far been a combination of new data management and the mastery of a new energy source— and that energy harvesting is the “fuel” for Industry 4.0. Since the limited sharing of best practices for successful energy harvesting limits the success rate for those designs, I will share some of those best practices in this blog.

I’m often asked for tips and tricks on how to best design an energy harvesting system. In this post, I’ll discuss the importance of being a “bear” rather than a “sloth” when it comes to energy harvesting systems. 

The secret for energy harvesting is to be like a bear, who:
* Knows when winter is coming and has the ability to adapt.
* Is fast enough to catch fish in anticipation of winter.
* Is capable of a huge reduction in metabolism when the environment requires it (hibernation).
* Is able to wake up extremely quickly from hibernation when external conditions stimulate its senses. 

The most frequent mistake for energy harvesting is to be like a sloth, who:
* Is not capable of adapting to a changing environment (as his limited natural habitat shows).
* Is barely capable of accelerating even when its survival is at stake.
* Does not adapt its energy spending to the situation, but always keeps it at a minimum.

But how do sloths and bears translate to embedded electronics systems? While a complete answer may require a whole second blog post, most designers should already know that a solar cell can produce energy anywhere in a range between 0 (no light), 2-5µW (poorly lit ) and up to 10mW (full sunlight) for the same square centimeter of active area. A bear-like system would be able to harvest all of this energy, while a sloth-like one would be optimized for the worst-case supply, say 1µW. By nature, the sloth approach limits the opportunity to harvest ambient energy and fails to adapt to new environmental conditions, thereby limiting the benefits that they system could provide to end customers.

You may ask how you can actually design a system that behaves like a bear? One place to start is with the Generic Energy Harvesting Adapter Module for Thermoelectric Generators (TEG) TI Designs reference design. In its lowest power mode, this design runs with 60nA and can harvest energy from 40µW to a few hundred milliwatts with more than 80% efficiency. Also, when the system is in hibernation mode, it can wake up at any time to react to environmental changes.

This performance is possible because of a unique combination of TI devices for ultra-low power and energy harvesting: the TPL5100 programmable timer and bq25570 power management integrated circuit (IC), plus the industry’s lowest power microcontroller unit (MCU), the MSP430FR5969 MCU, and lowest power comparator, the TLV3691.

The TPL5100 generates the “heart beat” of this reference design. This timer’s best feature is its ability to run at 30nA and wake the MSP430™ MCU periodically for housekeeping. When I helped define this IC, I wanted to be able to either generate an interrupt to an ultra-low-power MCU such as MSP430FR5969 MCU or disconnect the load. In this TI Design reference design, I am showing how to use it in this first manner.

For harvesting the ambient energy, I selected the bq25570, a DC/DC boost converter that can convert 90 percent of its input energy source from as low as 100µW, while running dynamic maximum power-point tracking (MPPT), which can also be powered down and then only takes 1nW.

The brain of the system is the MSP430FR5969 MCU. This MCU, in its lowest power mode (LPM4.5), takes only 20nA while keeping its general-purpose input/output (GPIO) remain active for either asynchronous interrupts or to power directly low-power functions of the system.

The “senses” that wake our bear from hibernation come from the TLV3691, a comparator that is operational with only 75nA and designed to monitor the input voltage. Given its low power consumption, the GPIO of the MSP430FR5969 MCU can power this comparator, and turn it on and off depending on the need.

![](https://e2e.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-09-70/scheme.jpg)

Figure 2: Block diagram of the reference design, in a BoosterPack form factor for rapid prototyping

If you are looking to design an extremely low-power or energy harvesting-based system, have a look at the schematics, layout and test data from this reference design. Feel free to share success stories or challenges you faced from previous designs in the comments.

And do be bearish and make your energy harvesting so adaptable and so compelling it take over the entire ecosystem!

Additional resources
Download the schematic, test data, design files and bill of materials for the Generic Energy Harvesting Adapter Module for Thermoelectric Generators (TEG) TI Designs reference design.
Learn why Industry 4.0 will be fueled by energy harvesting in this German-language article.
If your energy harvesting system needs to be isolated from the main system, download the schematic from this TI Designs reference design (TIDA-00349).
