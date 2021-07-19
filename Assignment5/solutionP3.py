import sys

class Node:
    def __init__(self, nodeValue):
        self.left= self.right= None
        self.nodeValue = nodeValue

# This function prints the tree in Inorder manner (left node-> root ->right node)
def printTree(root):
    if root is None:
        return
    printTree(root.left)
    print(root.nodeValue)
    printTree(root.right)


# Return the node with minimum key value found in that tree.
def findMinValueNode(node):
    tmpNode = node
    #As this is a binary tree go thru the leftmost node to find the minimum value
    while (tmpNode.left is not None):
        tmpNode = tmpNode.left
    return tmpNode

# Function to delete the required value and return the new root after re-ordering
def deleteNode(node, value):
    # If given root is empty
    if node is None:
        return node

    # As this is a binary tree, if the node to be deleted is < root then it lies in left subtree so
    # call this method recursively in left subtree until it matches the node that needs to be deleted
    if value < node.nodeValue:
        #print("value < nodevalue", value,node.nodeValue)
        node.left = deleteNode(node.left, value)

    # If the node to be deleted is > root then it lies in right subtree so call this method
    # recursively in right subtree until it matches the node that needs to be deleted
    elif (value > node.nodeValue):
        #print("value > nodevalue", value,node.nodeValue)
        node.right = deleteNode(node.right, value)

    # If the node to be deleted matches the node then this node needs to be deleted
    elif (value == node.nodeValue):
        #print("value == nodevalue", value,node.nodeValue)
        # If left child is None return the right child or return None if node has no children
        if node.left is None:
            temp = node.right
            root = None
            return temp
        # If right child is None return the left child
        elif node.right is None:
            temp = node.left
            root = None
            return temp

        # In case node that needs to be deleted has two children we need to find the smallest
        # child in the right subtree for replacement
        tmp = findMinValueNode(node.right)

        # Copy the Child's value to this node
        node.nodeValue = tmp.nodeValue

        # Once data copied delete the required node
        node.right = deleteNode(node.right, tmp.nodeValue)

    #return the new root in all cases even when the desired node is not found in the tree.
    return node

def mergeTrees(tree1, tree2):
    if (not tree1):
        return tree2
    if (not tree2):
        return tree1
    # Apply Merge sum
    tree1.nodeValue += tree2.nodeValue

    # Invoke Merging trees method recursively to sum their left nodes
    tree1.left = mergeTrees(tree1.left, tree2.left)

    # Invoke Merging trees method recursively to sum their right nodes
    tree1.right = mergeTrees(tree1.right, tree2.right)
    return tree1

# Function to store the traversal of a tree in Left->Node->Right order
def storeTreeValues(root, arr):
    # If given root is empty
    if root is None:
        return
    # Traverse thru the left subtree recursively and store the values in an array
    storeTreeValues(root.left, arr)
    # Append the root's value
    arr.append(root.nodeValue)
    # Traverse thru the right subtree recursively and store the values in an array
    storeTreeValues(root.right, arr)

# Function to copy contents of sorted array into a Binary search tree
def convertArrToBinSearchTree(arr, root):
    # If the given tree is empty
    if root is None:
        return
    # First update the left subtree
    convertArrToBinSearchTree(arr, root.left)

    # After updating root's data delete that value from array
    root.nodeValue = arr[0]
    arr.pop(0)

    # Update the right subtree
    convertArrToBinSearchTree(arr, root.right)

# This function converts a binary tree to Binary search Tree
def binaryTreeToBST(tree):
    # If given Tree is empty
    if tree is None:
        return

    # Create the temp array to store the value of Binary tree
    arr = []
    storeTreeValues(tree, arr)
    # Sort the array
    arr.sort()
    # copy array elements back to binary tree
    convertArrToBinSearchTree(arr, tree)


if __name__== '__main__':
    try:
        # Let us create a Binary Tree
        #    1
        #   / \
        #  2   3
        # / \   \
        #4   5   6
        tree1 = Node(1)
        tree1.left = Node(2)
        tree1.right = Node(3)
        tree1.left.left = Node(4)
        tree1.left.right = Node(5)
        tree1.right.right = Node(6)
        print("Tree 1 is ===>")
        printTree(tree1)

        # Now create second Binary Tree
        #     4
        #    / \
        #  1    7
        # /    / \
        #3    2   6

        tree2 = Node(4)
        tree2.left = Node(1)
        tree2.right = Node(7)
        tree2.left.left = Node(3)
        tree2.right.left = Node(2)
        tree2.right.right = Node(6)

        print("Tree 2 is ===>")
        printTree(tree2)

        root3 = mergeTrees(tree1, tree2)
        # Output -> Merged Binary Tree
        #     5
        #    / \
        #  3    10
        # / \   / \
        #7   5 2   12
        print("Merged Binary Tree is ===>")
        printTree(root3)

        # Convert binary tree to BST
        binaryTreeToBST(root3)
        # Output -> Binary Search Tree
        #     5
        #    / \
        #  3    10
        # / \   / \
        #2   5 7   12
        print("Converted Binary Search Tree is ===>")
        printTree(root3)
        # Output -> Binary Search Tree after deleting node with value 10
        #     5
        #    / \
        #  3    7
        # / \    \
        # 2   5   12
        print("Deleted Binary Search Tree is ===>")
        deleteNode(root3,10)
        printTree(root3)

    except NameError:
        print("\nName error occured. Error message: ",sys.exc_info()[1])
    except TypeError:
        print("\nType mismatch occured. Error message: ",sys.exc_info()[1])
    except ValueError:
        print("\nValue error occurred. Error message: ",sys.exc_info()[1])
    except IndexError:
        print("\nIndex error occurred. Error message: ",sys.exc_info()[1])
    except SyntaxError:
        print("\nSyntax error ocurred. Error message: ",sys.exc_info()[1])
    except AttributeError:
        print("\nAttribute error occured. Error message: ",sys.exc_info()[1])
    except Exception:
        print("Error encountered : ", sys.exc_info()[0])
        print("Try again...")