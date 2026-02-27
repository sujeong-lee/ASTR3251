


def angle_degrees_formatter(tick_value, tick_position):
    """
    Custom matplotlib formatter for depicting graph axes with
    modular units that wrap to 0 at 360 degrees

    Parameters
    ----------
    tick_value : float
        The tick label as an angle.

    tick_position: float
        The tick position (unused)

    Returns
    -------
    float
        Reformatted tick as an angle between 0 and 360 degrees
    """
    
    if tick_value < 0:
        return f"{tick_value + 360:.0f}"
    else:
        return f"{tick_value:.0f}"