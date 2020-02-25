import os

name = input()
os.system('VBoxManage modifyvm {} --cpuidset 00000001 000106e5 00100800 0098e3fd bfebfbff'.format(name))

os.system('VBoxManage setextradata {} "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "iMac11,3"'.format(name))

os.system('VBoxManage setextradata {} "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"'.format(name))

os.system('VBoxManage setextradata {} "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Iloveapple"'.format(name))

os.system('VBoxManage setextradata {} "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"'.format(name))

os.system('VBoxManage setextradata {} "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1'.format(name))
