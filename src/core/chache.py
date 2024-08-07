import time
from database.json_manager import JSONManager

json_manager = JSONManager()


def get_cached_data(cache_key, max_age=3600):
    cache = json_manager.read_json("local_cache.json")
    if cache_key in cache and time.time() - cache[cache_key]["timestamp"] < max_age:
        return cache[cache_key]["data"]
    return None


def update_cache(cache_key, data):
    cache = json_manager.read_json("local_cache.json")
    cache[cache_key] = {"data": data, "timestamp": time.time()}
    json_manager.write_json("local_cache.json", cache)
