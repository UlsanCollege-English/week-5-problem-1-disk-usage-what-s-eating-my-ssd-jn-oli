# src/disk_usage.py

def total_size(node):
    """Recursively calculate the total size of all files in the given structure."""
    if not node or not isinstance(node, dict):
        return 0

    node_type = node.get("type")

    # Handle file node
    if node_type == "file":
        return node.get("size", 0)

    # Handle directory node
    if node_type == "dir":
        total = 0
        for child in node.get("children", []):
            total += total_size(child)
        return total

    # Ignore unknown types
    return 0
