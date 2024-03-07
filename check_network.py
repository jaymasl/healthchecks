#!/usr/bin/env python3
import socket

def check_network():
    """Returns True and prints Success if it succeeds in resolving Google's URL"""
    try:
        socket.gethostbyname("www.google.com")
        print("Success")
        return True
    except:
        print("Fail")
        return False

check_network()