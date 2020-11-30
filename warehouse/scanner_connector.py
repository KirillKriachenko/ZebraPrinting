import usb.core

dev = usb.core.find(idVendor=0x05F9,idProduct=0x2210)
filebuffer = dev[0].interfaces()[0].endpoints()[0]
interface_number = dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

if dev.is_kernel_driver_active(interface_number):
    dev.detach_kernel_driver(interface_number)

dev.set_configuration()
endpoint_address = filebuffer.bEndpointAddress

reader = dev.read(endpoint_address,1024)

print(len(reader))
print(reader)

dev.attach_kernel_driver(interface_number)