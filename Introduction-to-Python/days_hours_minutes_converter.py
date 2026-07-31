"""
Days / Hours / Minutes Converter
===================================
Demonstrates: Floor division operator (//) and Modulus operator (%)

Converts a total number of minutes into a human-readable breakdown of
days, hours, and remaining minutes.

Key idea:
- // (floor division) gives the whole number of units that fit
- %  (modulus) gives what's left over after removing those whole units
"""


def convert_minutes(total_minutes):
    """
    Break down total minutes into days, hours, and minutes.

    Uses // to find whole days/hours, and % to find the remainder
    that carries over to the next smaller unit.
    """
    minutes_per_day = 24 * 60

    days = total_minutes // minutes_per_day          # whole days
    remaining_minutes = total_minutes % minutes_per_day  # leftover minutes after removing full days

    hours = remaining_minutes // 60                  # whole hours from what's left
    minutes = remaining_minutes % 60                 # final leftover minutes

    return days, hours, minutes


def main():
    print("=== Days / Hours / Minutes Converter ===")

    try:
        total_minutes = int(input("Enter total minutes to convert: "))

        if total_minutes < 0:
            print("Please enter a non-negative number of minutes.")
            return

        days, hours, minutes = convert_minutes(total_minutes)

        print(f"\n{total_minutes} minutes = {days} day(s), {hours} hour(s), {minutes} minute(s)")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
