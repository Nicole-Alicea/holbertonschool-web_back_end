#!/usr/bin/env python3
'''The following is an asynchronous coroutine'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Asynchronous coroutine that takes in an integer argument and waits
    for a random delay between 0 and max_delay seconds and eventually
    returns it.'''

    random_number = random.uniform(0, max_delay + 1)
    await asyncio.sleep(random_number)

    return random_number
