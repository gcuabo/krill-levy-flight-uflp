# Krill Heard with Levy Flight Applied to Uncapacitated Facility Location Problem

## Requirements

This requires python `3.11.4`. Requirements are listed in the requirements file,
and can be installed using

```
> pip install -r requirements.txt
```

## Running the algorithm

Once the requirements are installed, run the algorithm with:

```
> python main.py
```

## Changing the clients and facilities

The clients and facilities are listed in `krill_levy_flight/const.py`. A sample client is as follows:

```
Client("A", 2, 1)
```

Where "A" is a unique key to the client, and `2` and `1` are X and Y coordinates respectively.

The same structure goes to the facility:

```
Facility("X", 4, 1)
```

> [!IMPORTANT]  
> Client/Facility keys must be unique.
> e.g. There can be no 2 Clients with the same key 'A'.

## Understanding the returned solution

The algorithm returns the solution in a dictionary format, where the keys are the facilities:

```
{
  Facility(key='X', x=4, y=1): [
    Client(key='A', x=2, y=1),
    Client(key='B', x=3, y=2),
    Client(key='C', x=2, y=3),
    Client(key='D', x=4, y=4)
  ],
  Facility(key='Y', x=8, y=3): [
    Client(key='G', x=8, y=4),
    Client(key='H', x=9, y=5),
    Client(key='I', x=10, y=1)
  ],
  Facility(key='Z', x=3, y=7): [
    Client(key='E', x=3, y=5),
    Client(key='F', x=4, y=6),
    Client(key='J', x=6, y=10)
  ]
}
```

This means that Facility "X" with coordinates x=4, y=4 will serve Clients A, B, C, D.
... and so on
