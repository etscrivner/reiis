Reiis
======

**reify** (_verb_) - make (something abstract) more concrete or real.

Reified redis (reiis) is a python library that allows you to treat data 
persisted in redis like native python objects. While currently a work in
progress the goal is to allow simplified interaction with redis using python
and sane default behavior.

## Lists

You can treat reiis lists just like python lists, however, they will

```python
import reiis

reiis.connection.setup(['localhost:9160'])

items = reiis.list([], key='my-items')
items += [1, 2, 3]
items.append(4)
items.remove(3)

items.commit()

```
