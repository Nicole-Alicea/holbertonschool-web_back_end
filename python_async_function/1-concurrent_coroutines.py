#!/usr/bin/env python3
'''The following is an async routine'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Async routine that takes in 2 integer arguments and will spawn
    wait_random n times with the specified max_delay. Will return the list
    of all the delays in ascending order without using sort() because of
    concurrency.'''

    all_delays = [asyncio.create_task(wait_random(max_delay))
                  for _ in range(n)]
    
    return [await all_delays for all_delays
            in asyncio.as_completed(all_delays)]
