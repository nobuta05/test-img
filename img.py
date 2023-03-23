from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server

with Diagram("LDAP @ Lab", show=False, filename="output/ldap_@_lab"):
    with Cluster("LDAP Clients"):
        ldap_clients = [Server("GPU serv"), Server("CPU serv")]

    ldap_clients >> Server("LDAP Serv, Workstation")

with Diagram(
    "Servers @ Lab", show=False, filename="output/servers_@_lab", direction="TB"
):
    with Cluster("Lab"):
        clients = [
            Server("Workstation\nxx.xx.xx.xx"),
            Server("GPU serv"),
            Server("CPU serv"),
        ]

    Server("所内ルータ") - clients
