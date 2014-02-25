Reiis
======

**reify** (_verb_) - make (something abstract) more concrete or real.

Reified redis (reiis) is a python library that allows you to treat data
persisted in redis like their native python equivalents. While currently a work
in progress the goal is to allow simplified interaction with redis using python
objects and to provide a sane set of default behaviors.

## Lists

```python
import reiis

reiis.connection.setup('localhost', 6379)

items = reiis.List([], key='my-items')

items += [1, 2, 3]
items.append(4)
items.remove(3)

items.commit()
```
