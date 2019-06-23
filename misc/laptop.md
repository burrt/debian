
# ASUS Zenbook UX303LB

## Specifications

* ASUS Zenbook UX303LB-C4028H
* i7-5500U processor 2.40 GHz 2 cores/4 threads
* 8GB 1600MHz DDR3L-SDRAM
* 802.11a, 802.11g, 802.11n
* 1450 grams
* NVIDIA GeForce 940M
* Intel HD Audio hardware is capable of delivering up to eight channels at 192 kHz/32-bit quality

## Drivers

https://www.asus.com/sa-en/Notebooks/ASUS_ZENBOOK_UX303LB/HelpDesk_Download/

### Windows 10

If you want the SD card reader to operate correctly with Windows 10 v1903+, check that you have installed the Genesys USB3.0 Card Reader v4.5.2 - this may not be available from the ASUS Drivers website.

### Ubuntu

### Touchpad

To enable two finger scroll, you may need to do the following:

```bash
sudo add-apt-repository ppa:hanipouspilot/focaltech-dkms
sudo apt-get update
sudo apt-get install focaltech-dkms

# Then reboot, or reload module
sudo modprobe -r psmouse
sudo modprobe psmouse
```
