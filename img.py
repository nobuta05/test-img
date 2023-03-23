from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server

with Diagram("Servers @ Lab", show=False, filename="./outputs/servers_@_lab"):
    with Cluster("LDAP Clients"):
        ldap_clients = [Server("GPU serv"), Server("CPU serv")]

    ldap_clients >> Server("LDAP Serv, Workstation")
