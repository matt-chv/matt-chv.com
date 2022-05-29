Title: TDC - How to build a LIDAR system with a TDC
Date: 2017-02-01
Category: techart
Tags: sensing
Slug: TDC-for-LiDaR
Summary: How to build a LIDAR system with a time-to-digital converter
cover_image_url: LiDaR.PNG
cover_image_caption: Lidar with TDC
url_ext: http://www.ti.com/lit/an/slyt706/slyt706.pdf

#Introduction

In many applications, it is not possible to measure distance
to the target by establishing a physical contact. Typical
examples include measuring presence of objects on a
conveyor belt in logistic centers, or ensuring safety
distances around moving robot arms. Other possible
options for contactless distance measurement are eddy
currents, ultrasounds and light.
Light distance and ranging (LIDAR) systems use the
time taken by the light to travel back and forth to an
object to measure the distance to this object. A LIDAR
system can be built with either a high-speed ADC or a
time-to-digital converter (TDC). TDCs can be a timer in a
microcontroller/microprocessor (MCU/MPU), dedicated
logic on a field-programmable gate array (FPGA), or more
simply, a dedicated TDC integrated circuit (IC). This
article is an introduction to designing systems based on
TDCs and covers optical and analog front-end considerations, as well as basic signal processing for TDCs.
