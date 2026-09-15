def calculate_ttc(speed_ms: float, obstacle_distance_m: float) -> float:
    """
    Calculate Time to Collision (TTC) in seconds.
    Assumes obstacle is stationary.
    """
    if speed_ms <= 0:
        return float('inf')

    return obstacle_distance_m / speed_ms

def should_trigger_aeb(ttc: float) -> int:
    """
    Determine if AEB should be triggered based on TTC.
    Trigger if TTC < 2.0s.
    """
    if ttc < 2.0:
        return 1
    return 0
