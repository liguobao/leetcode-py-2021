# Java

## HashMap

- 在 jdk1.7 中，在多线程环境下，扩容时会造成环形链或数据丢失。

- 在 jdk1.8 中，在多线程环境下，会发生数据覆盖的情况。

## ConcurrentHashMap

- 分段锁，JDK1.7 是基于 Segment，多个 HashEntry 做的；JDK1.8 是基于首个 HashEntry，JDK1.8 使用红黑树来优化链表，查询更快
- ConcurrentHashMap 使用 Final 和 volatile，final 保证初始化安全性，不可变对象不需要同步就可以自由访问和被共享；volatile 保证内存对象被修改后在多个线程中即时可见
- ConcurrentHashMap 由于只锁部分 HashEntry，可能会导致“脏读”

## JVM 内存模型

### 内存分类

- 共享内存，分为主程序内存（主存）和工作线程内存。
- 实例域、静态域、数组元素都在堆内存中（所有线程都可以访问，可共享）
- 局部变量，方法定义参数、异常处理参数不会在线程中共享
- 不同线程处理共享内存对象的时候都是拷贝一份到自己的内存中，遇到 volatile 修饰的变量，线程更新后会立即写回主存中

### 重排序

- A =1， B=3， C= A+B 这样的一个代码，A 和 B 互相独立，编译器和处理器对指令调整的时候，改变顺序并不影响结果，这种时候尽可能并行化的操作是被 JMM 允许的

#### 允许的优化

- 编译器的优化顺序，不改变语义的情况下，重新排序语句的执行顺序
- 指令级并行的重排序，不存在数据依赖，处理器可以改变语句对应机器指令的执行顺序
- 内存的重排序，加载和存储操作看起来是乱序执行

### as-if-serial

- 单线程情况下，代码看起来是受到保护的，严格顺序执行的，这是编译器、runtime 和处理器共同保证的

### happens-before 原则

- 程序的顺序性 A =1, B=2 , A = A+1, B = B+A 对于 B =B+A 而言，A 一定是可见的且等于 2

- volatile 一个线程对 volatile 变量的读写，另一个线程读取 volatile 变量是可见的（及时写入主存）

- A happens-before B，B happens-before C, A happens-before C 传递性

```Java
class VolatileExample {
  int x = 0;
  volatile boolean v = false;
  public void writer() {
    x = 42;
    v = true;
  }
  public void reader() {
    if (v == true) {
      // 这里x会是多少呢？
    }
  }
}
// 两个线程分别执行writer()和reader()方法
// 由于v 是被 volatile修饰的，只要v== true, x一定等于42
```

- 管程中的锁 synchronized, A B 线程同时操作，保证 x =20 只被执行一次

```Java
 synchronized (this) { //此处自动加锁
  // x是共享变量,初始值=0
  if (this.x < 20) {
    this.x = 20;
  }
} //此处自动解锁
```

- 线程 Start()规则，在 A 线程中执行 B.Start(), 线程 A 中的所有操作结果对 B 都可见

```java
Thread B = new Thread(()->{
  // 主线程调用B.start()之前
  // 所有对共享变量的修改，此处皆可见
  // 此例中，a==77
});
// 此处对共享变量a修改
a = 77;
// 启动子线程
B.start();
```

- 线程 Join() 规则，A 线程中执行了 B.Join(), B 线程中的操作结果对 A 都可见
