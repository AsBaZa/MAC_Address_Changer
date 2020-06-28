# Readme

Para ver la configuración actual del MAC

```bash
ifconfig
```

Para modificarlo:

```bash
ifconfig INTERFACE down
ifconfig INTERFACE hw ether NEW_MAC
ifconfig INTERFACE up
ifconfig
```