# MySQL 事务

## 事务是什么？

- 一步或者几步数据库操作序列组成的执行单元，要不全部完成，要不全部放弃执行。

## 事务的四个特性

ACID

- Atomicity Atomicity(原子性) 最小单位，不可分割。
- Consistency Consistency(一致性) 事务执行结果是确定的，必须使得数据库从一个状态，变成另一个状态。或者说：无论事务提交还是回滚，不会破坏数据的完整性。（A 给 B 转账 100 的一个事务，事务提交成功，A-100，B+100；事务提交失败，A 不变 B 不变。）
- Isolation Isolation(隔离性) 并发执行事务的时候，事务和事务之间互相隔离，互不影响。
- Durability Durability(持久性) 已提交的事务对数据库的修改应该永久保存到数据库中。

## Atomicity 原子性

- 事务中的多个操作不可分割，要不全部执行成功，要不全部执行失败。

### 实现原理

MySQL 的原子性操作是使用 undo log 实现的。具体原理：将所有对数据的“增改删”操作都写入日志。

undo log 是逻辑日志，可以理解：记录和事务相反的 SQL 语句，事务执行 insert 语句，undo log 则记录 delete 语句。

它以追加写的方式添加日志，不会覆盖之前的日志。

除此之外，undo log 还用于实现数据库多版本控制 Multiversion Concurrency Control，简称 MVCC）。

如果事务部分执行成功，但另一部分由于种种奇怪的问题（断电、系统崩溃、软硬件鼓故障）而无法成功执行，

则通过回溯日志，将已执行的操作撤销，从而达到所有的操作执行失败的目的。

## Durability 持久性

一个事务对数据的所有修改，都会永久保存在数据库中。

MySQL 事务的持久性是通过 redo log 实现的。

具体实现机制：

当发生数据修改（增、删、改）的时候，InnoDB 引擎会先将记录接到 redo log 中，并更新内存，此时更新算已经完成了。

同时 InnoDB 引擎会选择合适的时机将 redo log 写入磁盘。

redo log 日志是物理日志，记录哪个数据页做了什么样的修改，而不是 SQL 语句的形式。

它有固定的大小，是以循环写入的形式记录日志，空间用完之后会覆盖之前的日志。

## undo log 和 redo log 落盘方式

先到 log buffer，再到 OS buffer，最后落盘。因此中途是有可能因为断点、硬件故障等原因导致日志丢失。

因此 MySQL 提供了三种持久化方式，提供 innodb_flush_log_at_trx_commit 参数供我们使用。

innodb_flush_log_at_trx_commit： 控制 InnoDB 讲 log buffer 的数据写入 OS Buffer，并刷到磁盘的时间点，取值分别是 0，1，2，默认是 1

- 0 每秒将 log buffer 写入 OS Buffer，调用 fsync()将数据写入磁盘
- 1 每次提交写入 OS Buffer，调用 fsync()将数据写入磁盘
- 2 每次提交写入 OS Buffer，每秒调用 fsync()将数据写入磁盘

![innodb_flush_log_at_trx_commit](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48b6380e3400472b86d2f1d0fdca156b~tplv-k3u1fbpfcp-zoom-1.image)

### 数据库崩溃怎么处理？使用 crash_recovery

- 首先读取 redo log，将成功提交没有落磁盘的数据写入磁盘，保证持久性。
- 然后读取 undo log，将还没有成功提交的事务进行回滚，保证了原子性。
- crash_recovery 完成之后，数据库恢复到一致状态，可以继续被使用。

## 数据库事务隔离性

多个事务同时执行时，一个事务的执行不影响其他事务的的执行。

### 事务没有隔离会产生的问题

#### 第一类丢失更新

一个事务在撤销的时候，覆盖了另一个事务更新的数据。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ac56dbb7d7046c68b04368a3a9a8b36~tplv-k3u1fbpfcp-zoom-1.image)

#### 脏读

一个事务读到了另一个事务尚未提交的数据。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5496ab494ef47a5a1d0d24cf2ab3e19~tplv-k3u1fbpfcp-zoom-1.image)

#### 幻读

一个事务读到了另一个事务已提交的新增数据。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb34e4e39f5d402899408af95d3c1cf7~tplv-k3u1fbpfcp-zoom-1.image)

事务 B 在同一个事务中执行两次统计操作之间，另一事务 A insert 了一条记录，导致得到的结果不一样，好像发生了幻觉。

还有一种情况是事务 B 更新了表中所有记录的某一字段，之后事务 A 又插入了一条记录，事务 B 再去查询发现有一条记录没有被更新，这也是幻读。

#### 不可重复读

一个事务读到了另一个事务已提交的更新数据。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be0b896fe7fe4be0acaf5cad5b228dbc~tplv-k3u1fbpfcp-zoom-1.image)

事务 B 在 T2 和 T5 阶段都执行了查询余额的操作，但是每次得到的结果都不一样，

这在开发中是不允许的，同一个事务中同样的多次查询，每次返回不一样的结果，让人不免会对数据库的可靠性产生怀疑。

#### 第二类丢失更新

一个事务提交的时候，覆盖了另一个事务已提交的更新数据。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9205251a5664ed5a6a6c4f287652418~tplv-k3u1fbpfcp-zoom-1.image)

当事务 A 提交之后，账户余额已经发生了变动，然后事务 B 还是基于原始金额（即 1000）的基础上扣除取款金额的，

事务 B 一提交，就是把事务 A 的提交给完全覆盖了。此为第二类丢失更新。

### MySQL 四种隔离级别

- Serializable 可串行化。事务之间串行执行，安全性高，性能差。
- Repeatable 可重复读。默认隔离级别，同一个事务在相同查询会看到同样的数据行（基本 MVCC 多版本并发控制），安全性好，性能较好。
- Read Commited 读已提交。一个事务可以读到已提交的事务数据。
- Read Uncommited 读未提交。一个事务可以读到未提交的事务数据。

| 隔离级别        | 是否出现第一类丢失更新 | 是否出现脏读 | 是否出现虚读 | 是否出现不可重复读 | 是否出现第一类丢失更新 | 是否出现第二类丢失更新 |
| --------------- | ---------------------- | ------------ | ------------ | ------------------ | ---------------------- | ---------------------- |
| Serializable    | 否                     | 否           | 否           | 否                 | 否                     | 否                     |
| Repeatable Read | 否                     | 否           | 是           | 否                 | 否                     | 否                     |
| Read Commited   | 否                     | 否           | 是           | 是                 | 是                     | 是                     |
| Read Uncommited | 否                     | 是           | 是           | 是                 | 是                     | 是                     |

## Repeatable Read

### 快照读解决方案

| 时间 | 事务 A                 | 事务 B                                            |
| ---- | ---------------------- | ------------------------------------------------- |
| T1   | SELECT \* FROM student | -                                                 |
| T2   | -                      | INSERT INTO student VALUES (2, 230160310, ‘Kata’) |
| T3   | -                      | commit                                            |
| T4   | SELECT \* FROM student | -                                                 |

这种情况下，事务 A 中前后拿到的数量都是 1，实现了“重复读”。

#### 解决方案

MySQL 在 Repeatable Read 隔离级别下，用 MVCC（Multiversion Concurrency Control，多版本并发控制）解决了 select 普通查询的幻读现象。

具体的实现方式就是事务开始时，第一条 select 语句查询结果集会生成一个快照（snapshot），

并且这个事务结束前，同样的 select 语句返回的都是这个快照的结果，而不是最新的查询结果，

这就是 MySQL 在 Repeatable Read 隔离级别对普通 select 语句使用的快照读（snapshot read）。

MVCC 是多版本并发控制，快照就是其中的一个版本。

所以可以说 MVCC 实现了快照读，具体的实现方式涉及到 MySQL 的隐藏列。MySQL 会给每个表自动创建三个隐藏列:

- DB_TRX_ID：事务 ID，记录操作（增、删、改）该数据事务的事务 ID
- DB_ROLL_PTR：回滚指针，记录上一个版本的数据在 undo log 中的位置
- DB_ROW_ID：隐藏 ID ，创建表没有合适的索引作为聚簇索引时，会用该隐藏 ID 创建聚簇索引

由于 undo log 中记录了各个版本的数据，并且通过 DB_ROLL_PTR 可以找到各个历史版本，并且由 DB_TRX_ID 决定使用哪个版本（快照）。所以相当于 undo log 实现了 MVCC，MVCC 实现了快照读。

如此看来，MySQL 的 Repeatable Read 隔离级别利用快照读，已经解决了幻读的问题。

然而并没有。

| 时间 | 事务 A                                                     | 事务 B                                           |
| ---- | ---------------------------------------------------------- | ------------------------------------------------ |
| T1   | SELECT \* FROM student                                     | -                                                |
| T2   | -                                                          | INSERT INTO student VALUES (3, 230160312, Luffy) |
| T3   | -                                                          | commit                                           |
| T4   | UPDATE student SET name = ‘Katakuri’ WHERE name = ‘Luffy’; | -                                                |
| T5   | SELECT \* FROM student                                     | -                                                |

这个时候，事务 A 在 T5 阶段能看到所有的数据，且把事务 B 中新增的数据修改掉了。

这其实是 MySQL 对 insert、update 和 delete 语句所使用的当前读（current read）。

因为涉及到数据的修改，所以 MySQL 必须拿到最新的数据才能修改，所以涉及到数据的修改肯定不能使用快照读（snapshot read）。

由于事务 A 读到了事务 B 已提交的新增数据，所以就产生了前文所说的幻读。

### 间隙锁

是通过间隙锁（Gap Lock）来解决的。我们都知道 InnoDB 支持行锁，并且行锁是锁住索引。

而间隙锁用来锁定索引记录间隙，确保索引记录的间隙不变。间隙锁是针对事务隔离级别为 Repeatable Read 或以上级别而设的，间隙锁和行锁一起组成了 Next-Key Lock。当 InnoDB 扫描索引记录的时候，会首先对索引记录加上行锁，再对索引记录两边的间隙加上间隙锁（Gap Lock）。加上间隙锁之后，其他事务就不能在这个间隙插入记录。这样就有效的防止了幻读的发生。

默认情况下，InnoDB 工作在 Repeatable Read 的隔离级别下，并且以 Next-Key Lock 的方式对索引行进行加锁。当查询的索引具有唯一性（主键、唯一索引）时，Innodb 存储引擎会对 Next-Key Lock 进行优化，将其降为行锁，仅仅锁住索引本身，而不是范围（除非锁定不存在的值）。若是普通索引，则会使用 Next-Key Lock 将记录和间隙一起锁定。

### Locking Reads

If you query data and then insert or update related data within the same transaction, the regular SELECT statement does not give enough protection. Other transactions can update or delete the same rows you just queried. InnoDB supports two types of locking reads that offer extra safety:

#### SELECT ... LOCK IN SHARE MODE

Sets a shared mode lock on any rows that are read. Other sessions can read the rows, but cannot modify them until your transaction commits. If any of these rows were changed by another transaction that has not yet committed, your query waits until that transaction ends and then uses the latest values.

#### SELECT ... FOR UPDATE

For index records the search encounters, locks the rows and any associated index entries, the same as if you issued an UPDATE statement for those rows. Other transactions are blocked from updating those rows, from doing SELECT ... LOCK IN SHARE MODE, or from reading the data in certain transaction isolation levels. Consistent reads ignore any locks set on the records that exist in the read view. (Old versions of a record cannot be locked; they are reconstructed by applying undo logs on an in-memory copy of the record.)

## 结束语

全文基本引用于:[深入理解 MySQL 中的事务【超详细配图版】](https://juejin.cn/post/6945713828470620191)


### 扩展阅读
- [【享学MySQL】系列：MySQL中的锁机制](https://juejin.cn/post/6944573028156063751)
- [深入理解 MySQL 的 MVCC 机制](https://cloud.tencent.com/developer/article/1876227)
- [MySQL深度分页的问题及优化方案：千万级数据量如何快速分页](https://juejin.cn/post/6945392074988617764)
