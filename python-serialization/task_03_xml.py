#!/usr/bin/env python3
"""
This is a module docstring
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This is a function docstring
    """

    def build_xml_element(parent, data):
        """Recursively builds XML elements from a dictionary"""
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(parent, key)
                build_xml_element(child, value)

        else:
            parent.text = str(data)

    root = ET.Element("data")

    tree = ET.ElementTree(root)

    build_xml_element(root, dictionary)

    tree.write(filename)


def deserialize_from_xml(filename):
    """
    This is a function docstring
    """

    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}

    for child in root:
        data[child.tag] = child.text

    return data
