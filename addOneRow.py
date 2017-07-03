def addOneRow(root,v,d):
    if d==1:
        res = TreeNode(v)
        res.left = root
        return res
    queue = [root]
    count = 1
    while count<d-1:
        n = len(queue)
        for i in range(n):
            if queue[i].left:
                queue.append(queue[i].left)
            if queue[i].right:
                queue.append(queue[i].right)
        queue = queue[n:]
        count += 1
    for i in queue:
        l = i.left
        r = i.right
        i.left = TreeNode(v)
        i.left.left = l
        i.right = TreeNode(v)
        i.right.right = r
    return root
