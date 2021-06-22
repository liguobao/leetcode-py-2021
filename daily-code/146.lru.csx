
public class ListNode
{
    public int key { get; set; }
    public int val { get; set; }

    public ListNode prev { get; set; }

    public ListNode next { get; set; }

    public ListNode(int key = 0, int val = 0)
    {
        this.key = key;
        this.val = val;
    }
}

public class LRUCache
{

    public int capacity { get; set; }

    public ListNode head { get; set; }

    public ListNode tail { get; set; }

    public Dictionary<int, ListNode> nodeDictionary { get; set; }

    public LRUCache(int capacity)
    {
        this.capacity = capacity;
        this.nodeDictionary = new Dictionary<int, ListNode>();
        this.head = new ListNode();
        this.tail = new ListNode();
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    private void moveNodeToTail(int key, int? val = null)
    {
        var keyNode = this.nodeDictionary[key];
        if (val.HasValue)
        {
            keyNode.val = val.Value;
        }
        // 把当前节点抽离出来
        keyNode.prev.next = keyNode.next;
        keyNode.next.prev = keyNode.prev;

        // 把当前节点，挪到最后
        keyNode.prev = this.tail.prev;
        keyNode.next = this.tail;
        this.tail.prev.next = keyNode;
        this.tail.prev = keyNode;
    }

    public int Get(int key)
    {
        if (!this.nodeDictionary.ContainsKey(key))
        {
            return -1;
        }
        this.moveNodeToTail(key);
        return this.nodeDictionary[key].val;
    }

    public void Put(int key, int value)
    {
        if (this.nodeDictionary.ContainsKey(key))
        {
            this.moveNodeToTail(key, value);
            return;
        }
        if (this.nodeDictionary.Count > this.capacity)
        {
            var removeKey = this.head.next.key;
            this.nodeDictionary.Remove(removeKey);
            this.head.next = this.head.next.next;
            this.head.next.prev = this.head;
        }
        var nowNode = new ListNode(key, value);
        // 把当前节点，挪到最后
        nowNode.prev = this.tail.prev;
        nowNode.next = this.tail;
        this.tail.prev.next = nowNode;
        this.tail.prev = nowNode;
        this.nodeDictionary.Add(key, nowNode);
    }
}




var lruCache = new LRUCache(2);
lruCache.Put(1, 1);
lruCache.Put(2, 2);
Console.WriteLine(lruCache.Get(1));
lruCache.Put(3, 3);
Console.WriteLine(lruCache.Get(2));
lruCache.Put(4, 4);
Console.WriteLine(lruCache.Get(1));