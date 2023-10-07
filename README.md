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
> Client/Facility keys must be unique. e.g. There can be no 2 Clients with the same key 'A'.

** Client/Facility keys must be unique. There can be no 2 Clients with the same key 'A' ***
