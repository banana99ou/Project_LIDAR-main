from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

for i, scan in enumerate(lidar.iter_scans()):
    print(scan)
    if i > 10:
        break

lidar.stop()
lidar.stop_motor()
lidar.disconnect4()