routers = {
    "R1": {
        "device_type": "cisco_ios",
        "host": "192.168.15.140",
        "username": "admin",
        "password": "a",
        "secret": "a",
        "interfaces": {
            "fa0/0": "10.1.12.1 255.255.255.0",
            "fa0/1": "10.1.11.1 255.255.255.0",
            "Loopback0": "10.1.1.1 255.255.255.0"
        },
        "ospf_config": {
            "ospf_process_id": "1",
            "router_id": "1.1.1.1",
            "networks": [
                {"ip": "10.1.1.0", "mask": "0.0.0.255", "area": "1"},
                {"ip": "10.1.12.0", "mask": "0.0.0.255", "area": "0"}
            ]
        },
        "eigrp_config": {
            "as_number": "64512",
            "router_id": "1.1.1.1",
            "networks": [
                {"ip": "10.1.11.0", "mask": "0.0.0.255"}
            ]
        }
    },
    "R2": {
        "device_type": "cisco_ios",
        "host": "192.168.15.141",
        "username": "admin",
        "password": "a",
        "secret": "a",
        "interfaces": {
            "fa0/0": "10.1.12.2 255.255.255.0",
            "fa0/1": "10.1.23.2 255.255.255.0",
            "Loopback0": "10.1.1.1 255.255.255.0",
        },
        "ospf_config": {
            "ospf_process_id": "1",
            "router_id": "2.2.2.2",
            "networks": [
                {"ip": "10.1.12.0", "mask": "0.0.0.255", "area": "0"},
                {"ip": "10.1.23.0", "mask": "0.0.0.255", "area": "0"}
            ]
        }
    },
    "R3": {
        "device_type": "cisco_ios",
        "host": "192.168.15.142",
        "username": "admin",
        "password": "a",
        "secret": "a",
        "interfaces": {
            "fa0/0": "10.1.23.3 255.255.255.0",
            "fa0/1": "10.1.32.3 255.255.255.0",
            "Loopback0": "10.3.3.1 255.255.255.0"
        },
        "ospf_config": {
            "ospf_process_id": "1",
            "router_id": "3.3.3.3",
            "networks": [
                {"ip": "10.3.3.0", "mask": "0.0.0.255", "area": "0"},
                {"ip": "10.1.23.0", "mask": "0.0.0.255", "area": "0"}
            ]
        },
        "bgp_config": {
            "as_number": "64532",
            "router_id": "3.3.3.3",
            "neighbors": [
                {"ip": "10.1.32.2", "remote_as": "64532"}
            ]
        }
    },
    "D1": {
        "device_type": "cisco_ios",
        "host": "192.168.15.143",
        "username": "admin",
        "password": "a",
        "secret": "a",
        "interfaces": {
            "fa2/11": "10.1.11.2 255.255.255.0",
            "Loopback0": "198.51.100.1 255.255.255.128"
        },
        "eigrp_config": {
            "as_number": "64512",
            "router_id": "11.11.11.11",
            "networks": [
                {"ip": "10.1.11.0", "mask": "0.0.0.255"},
                {"ip": "198.51.100.0", "mask": "0.0.0.127"}
            ]
        }
    },
    "D2": {
        "device_type": "cisco_ios",
        "host": "192.168.15.144",
        "username": "admin",
        "password": "a",
        "secret": "a",
        "interfaces": {
            "fa2/11": "10.1.32.2 255.255.255.0",
            "Loopback0": "209.165.201.1 255.255.255.128"
        },
        "bgp_config": {
            "as_number": "64532",
            "router_id": "22.22.22.22",
            "neighbors": [
                {"ip": "10.1.32.3", "remote_as": "64532"}
            ],
            "address_family": {
                "ipv4": [
                    {"network": "209.165.201.0", "mask": "255.255.255.128"}
                ]
            }
        }
    }
}

