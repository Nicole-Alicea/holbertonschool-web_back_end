#!/usr/bin/env python3
'''The following is an asynchronous coroutine'''

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measures the total execution time of an async function'''

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
