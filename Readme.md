# Readme

Para ver la configuración actual del MAC

```bash
ifconfig
```

Para modificarlo:

```bash
ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55
ifconfig eth0 up
ifconfig
```