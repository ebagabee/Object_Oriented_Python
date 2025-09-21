def destroy_walls(wall_health):
    health_walls = []
    for wall in wall_health:
        if wall > 0:
            health_walls.append(wall)
    return health_walls
