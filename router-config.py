from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from variables import routers

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Define the templates
interface_template = env.get_template('interface_template.j2')
ospf_template = env.get_template('ospf_template.j2')
eigrp_template = env.get_template('eigrp_template.j2')
bgp_template = env.get_template('bgp_template.j2')

# Function to deploy configuration to a router
def deploy_config(router_info, interface_config, ospf_config, eigrp_template, bgp_template):
    connection_params = {
        "device_type": router_info['device_type'],
        "host": router_info['host'],
        "username": router_info['username'],
        "password": router_info['password'],
        "secret": router_info.get('secret', ''),
        "timeout": 100,
    }

    # Connect to the router and send configuration commands
    with ConnectHandler(**connection_params) as conn:
        conn.enable()

        # Send interface configuration
        output = conn.send_config_set(interface_config.split('\n'))
        print(f"Interface Configuration output for {router_info['host']}:\n{output}")

        # Send OSPF configuration if 'ospf_config' is present
        if 'ospf_config' in router_info:
            ospf_commands = ospf_config.split('\n')
            output = conn.send_config_set(ospf_commands)
            print(f"OSPF Configuration output for {router_info['host']}:\n{output}")

        # Send EIGRP configuration if 'eigrp_config' is present
        if 'eigrp_config' in router_info:
            eigrp_config = eigrp_template.render(eigrp_config=router_info['eigrp_config'])
            output = conn.send_config_set([eigrp_config])
            print(f"EIGRP Configuration output for {router_info['host']}:\n{output}")

        # Send BGP configuration if 'bgp_config' is present
        if 'bgp_config' in router_info:
            print(f"Rendering BGP configuration for {router_info['host']}:\n{router_info['bgp_config']}")
            bgp_config = bgp_template.render(bgp_config=router_info['bgp_config'])
            output = conn.send_config_set([bgp_config])
            print(f"BGP Configuration output for {router_info['host']}:\n{output}")

# Iterate over each router and configure interfaces, OSPF, EIGRP, and BGP
for router_name, router_info in routers.items():
    print(f"Configuring {router_name}...")

    # Generate interface configuration commands from the template
    interface_config = interface_template.render(interfaces=router_info['interfaces'])

    # Generate OSPF configuration commands from the template if 'ospf_config' is present
    ospf_config = ospf_template.render(ospf_config=router_info.get('ospf_config', ''))

    # Deploy the configuration
    deploy_config(router_info, interface_config, ospf_config, eigrp_template, bgp_template)

print("Configuration completed.")
