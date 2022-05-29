Title: What can we learn for IIoT from the man who invented the Web?
Date: 2016-01-12
Category: Blog
Tags: blog, business, fiction
cover_image_url: web_3.0_iiot.jpg
url_ext: https://e2e.ti.com/blogs_/b/industrial_strength/posts/what-can-we-learn-for-iiot-from-the-man-who-invented-the-web
cover_image_caption: What can we learn for IIoT from the man who invented the Web. The What, Where and How.
Slug: learning-from-web-for-iiot

# What can we learn for IIoT from the man who invented the Web

> originally posted [here](https://e2e.ti.com/blogs_/b/industrial_strength/posts/what-can-we-learn-for-iiot-from-the-man-who-invented-the-web)

These days, not a day goes by without news related to the benefits of process automation or factory automation brought by the Industrial Internet of Things (IIoT). When we talk to industry stakeholders, challenges about integration from sensor to data warehouse and cybersecurity are among the most critical aspects that might delay rollout of IIoT.

To understand the challenge of integration from sensor to data warehouse that IIoT faces and identify ways to overcome those challenges, let’s go back to what made the Internet and World Wide Web so successful. While the Web first appeared in the 1950s, its development was extremely slow and kept to the niches of university research and defense. But that all changed when Tim Berners-Lee defined the three principles that made the Internet possible:

* What you get: HTML.
* Where to get the desired content from: URI.
* How to get the information: HTTP.

This innovative way of thinking gave rise to the first two waves of the Internet, referred to Web 1.0 and Web 2.0. As seen in figure 2, Web 3.0, the third wave where data can be generated and consumed by machines, is basically the IIoT, when machines become capable of acting and reacting based on web content.

 
![][https://e2e.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-09-70/0624.1.jpg]
Figure 2: The three ages of the Internet

To help our customers roll out solutions for IIoT, we decided to look at what Tim Berners-Lee did to enable Web 1.0 and realized that we actually just needed to bring the three elements and show case an example of integration from sensor to the data warehouse.

More specifically, we reused the architecture from web 1.0: 

* What you get: industrial-grade data collection.
    * To make these industrial grade measures available, we decided to bring to market designs with the industry’s highest levels of accuracy, resolution, power consumption and cost structure.
* Where do you get this: wireless sensor nodes.
    * To make those wireless sensor nodes available, we decided to attach the sensors to highly versatile wireless links.
* Howto get it: gateway.
    * To make this gateway available, we decided to make this data easily available via gateways that are highly flexible and easily connected to existing network infrastructure or via one of our cloud partners.

![][https://e2e.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-09-70/TI_5F00_WirelessSensorNode_5F00_Blog_5F00_revised.jpg]

At TI, we had those three elements, but they were not tied together. We decided to bind this together and release the wireless pH sensor transmitter (TIDA-00561) reference design and showcase it with a Bluetooth® Smart gateway. This was demoed in our booth at SPS 2015.

The design has a pH front-end with a standard connection for a pH probe and lab-tested performance data in the 0-14 pH input range with an overall accuracy of +/- 0.01pH, ensuring compatibility with process instrumentation needs. The reference design’s form factor and electrical connections are compatible with the TI SimpleLink™ multi-standard CC2650 SensorTag ecosystem, allowing you to create a wireless sensor node. A simple firmware update is enough to select the wireless connectivity technology: Bluetooth® Smart, ZigBee® or 6LoWPAN.

Once you have selected the wireless connectivity technology, you can use the appropriate gateway to either run analysis of the system which can be transported by Ethernet or wireless local area networks (WLAN) for cloud analysis with one of our cloud partners.

By creating and connecting wireless sensor nodes like TIDA-00561 or the Wireless Thermocouple Sensor Transmitter DevPack for SensorTag Reference Design, you can easily setup a network and leverage the Bluetooth ecosystem for development. At a later point, the switch to a different radio protocol can be done more easily since both TI gateways and TI SensorTag support other networks, leaving the rest of the datalink untouched, therefore accelerating the work leading to the rollout of IIoT.
