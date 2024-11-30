from treenode import TreeNode

def read_tree():
    f_line = input().split()
    s_line = input().split()
    n, d = int(f_line[0]), int(f_line[1])
    nodes = [TreeNode(value) if value != '-' else None for value in s_line]

    for i in range(n):
        if nodes[i] is not None:
            for j in range(1, d + 1):
                child_index = d * i + j
                if child_index < n and nodes[child_index] is not None:
                    nodes[i].add_child(nodes[child_index])

    return nodes[0] if nodes else None

def main():
    read_tree().print_tree()

if __name__ == "__main__":
    main()
