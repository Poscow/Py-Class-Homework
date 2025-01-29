average_speed = int(80)
speed_limit = int(60)
distance_traveled = int(100)
speeding_time = distance_traveled / average_speed
speed_limit_time = distance_traveled / speed_limit 
speed_limit_total_time = int(speed_limit_time * 60)
speeding_total_time = int(speeding_time * 60)
print(f"While traveling, {average_speed} miles per hour with the speed limit of {speed_limit}. You saved {speed_limit_total_time - speeding_total_time} minutes traveling {distance_traveled} miles.")

