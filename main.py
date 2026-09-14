import sys
from csv_handler import read_csv, write_csv
from aeb_logic import calculate_ttc, should_trigger_aeb
from config import DB_FILE, OUTPUT_FILE

def main():
    try:
        data = read_csv(DB_FILE)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    if not data:
        print("No data found in the CSV.")
        sys.exit(0)

    fieldnames = list(data[0].keys())
    if "emergency_brake" not in fieldnames:
        fieldnames.append("emergency_brake")

    aeb_events = 0
    closest_obstacle = float('inf')

    processed_data = []

    for row in data:
        try:
            # Parse speed and distance
            speed = float(row.get('speed', 0))
            distance = float(row.get('obstacle_distance', 0))
        except (ValueError, TypeError):
            # Skip invalid rows as recommended
            continue

        # Calculate Time to Collision
        ttc = calculate_ttc(speed, distance)

        # Check if AEB should trigger
        trigger = should_trigger_aeb(ttc)
        row['emergency_brake'] = trigger

        processed_data.append(row)

        # Update metrics
        if trigger == 1:
            aeb_events += 1

        if distance < closest_obstacle:
            closest_obstacle = distance

    # Write processed data back to output CSV
    write_csv(OUTPUT_FILE, processed_data, fieldnames)

    # Print report
    print(f"Total AEB events: {aeb_events}")
    if closest_obstacle != float('inf'):
        print(f"Closest obstacle detected: {closest_obstacle:.2f} meters")
    else:
        print("No valid obstacles detected.")

if __name__ == "__main__":
    main()
