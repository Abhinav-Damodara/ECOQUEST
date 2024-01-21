import matplotlib.pyplot as plt
def display_tasks(category, score):
    short_term_tasks = []
    long_term_tasks = []

    if category == "Electronic Waste":
        if score == 1:
            short_term_tasks = ["Device Power-Off Routine", "Screen Time Limits", "Unplug Unused Chargers", "Digital Breaks"]
            long_term_tasks = ["Energy-Efficient Upgrades", "Green Energy Source", "Educational Outreach", "Community Electronics Recycling Event"]
        elif score == 2:
            short_term_tasks = ["Digital Breaks", "Unplug Unused Chargers", "Screen Time Limits", "Device Power-Off Routine"]
            long_term_tasks = ["Energy-Efficient Upgrades", "Green Energy Source", "Educational Outreach", "Community Electronics Recycling Event"]
        elif score == 3:
            short_term_tasks = ["Screen Time Tracker", "Tech-Free Zones", "Scheduled Digital Breaks", "Device Consolidation"]
            long_term_tasks = ["Digital Detox Weekend", "Smart Home Automation", "Green Energy Source Transition", "Educate Others Online"]
        elif score == 4:
            short_term_tasks = ["Tech-Free Zones", "Scheduled Digital Breaks", "Screen Time Tracker", "Digital Detox Day"]
            long_term_tasks = ["Scheduled Digital Sabbaticals", "Device Consolidation", "Tech-Free Zones in Home", "Recycle Old Devices"]
        else:
            short_term_tasks = ["Scheduled Digital Sabbaticals", "Device Consolidation", "Tech-Free Zones in Home", "Recycle Old Devices"]
            long_term_tasks = ["Advocacy for Responsible Tech Use", "Organize E-Waste Collection Drives", "Green Technology Adoption", "Educate Community"]

    elif category == "Fuel Consumption":
        if score == 1:
            short_term_tasks = ["Try Public Transport for a Day", "Plan Carpooling with Friends", "Practice Eco-Friendly Driving Habits", "Walk or Bike Short Distances"]
            long_term_tasks = ["Increase Public Transport Usage", "Join Car-Sharing Program", "Upgrade to Hybrid/Electric Vehicle", "Advocate for Sustainable Transportation"]
        elif score == 2:
            short_term_tasks = ["Plan Carpooling with Friends", "Try Public Transport for a Day", "Walk or Bike Short Distances", "Practice Eco-Friendly Driving Habits"]
            long_term_tasks = ["Increase Carpooling Frequency", "Explore Car-Sharing Programs", "Upgrade to Hybrid/Electric Vehicle", "Advocate for Sustainable Transportation"]
        elif score == 3:
            short_term_tasks = ["Practice Eco-Friendly Driving Habits", "Plan Carpooling with Friends", "Try Public Transport for a Day", "Walk or Bike Short Distances"]
            long_term_tasks = ["Upgrade to Hybrid/Electric Vehicle", "Participate in Carpooling Initiatives", "Advocate for Sustainable Transportation", "Explore Public Transport Options"]
        elif score == 4:
            short_term_tasks = ["Walk or Bike Short Distances", "Try Public Transport for a Day", "Plan Carpooling with Friends", "Practice Eco-Friendly Driving Habits"]
            long_term_tasks = ["Explore Public Transport Options", "Join Carpooling Initiatives", "Advocate for Sustainable Transportation", "Consider Eco-Friendly Vehicle Upgrade"]
        else:
            short_term_tasks = ["Walk or Bike Short Distances", "Try Public Transport for a Day", "Plan Carpooling with Friends", "Practice Eco-Friendly Driving Habits"]
            long_term_tasks = ["Upgrade to Eco-Friendly Vehicle", "Explore Car-Sharing Programs", "Advocate for Sustainable Transportation", "Participate in Public Transport Advocacy"]

    elif category == "Water Usage":
        if score == 1:
            short_term_tasks = ["Fix Leaks", "Shorter Shower Time", "Collect Rainwater", "Turn Off Tap"]
            long_term_tasks = ["Install Water-Efficient Appliances", "Opt for Native Plants in Garden", "Implement Greywater System", "Community Water Conservation Initiative"]
        elif score == 2:
            short_term_tasks = ["Shorter Shower Time", "Turn Off Tap", "Fix Leaks", "Collect Rainwater"]
            long_term_tasks = ["Opt for Native Plants in Garden", "Implement Greywater System", "Community Water Conservation Initiative", "Install Water-Efficient Appliances"]
        elif score == 3:
            short_term_tasks = ["Turn Off Tap", "Fix Leaks", "Shorter Shower Time", "Collect Rainwater"]
            long_term_tasks = ["Implement Greywater System", "Community Water Conservation Initiative", "Install Water-Efficient Appliances", "Opt for Native Plants in Garden"]
        elif score == 4:
            short_term_tasks = ["Fix Leaks", "Shorter Shower Time", "Turn Off Tap", "Collect Rainwater"]
            long_term_tasks = ["Community Water Conservation Initiative", "Install Water-Efficient Appliances", "Opt for Native Plants in Garden", "Implement Greywater System"]
        elif score == 5:
            short_term_tasks = ["Shorter Shower Time", "Turn Off Tap", "Fix Leaks", "Collect Rainwater"]
            long_term_tasks = ["Opt for Native Plants in Garden", "Implement Greywater System", "Community Water Conservation Initiative", "Install Water-Efficient Appliances"]
        else:
            short_term_tasks = ["Shorter Shower Time", "Turn Off Tap", "Fix Leaks", "Collect Rainwater"]
            long_term_tasks = ["Implement Greywater System", "Community Water Conservation Initiative", "Install Water-Efficient Appliances", "Opt for Native Plants in Garden"]

    elif category == "Plastic Usage":
        if score == 5:
            short_term_tasks = ["Always Carry Reusable Bag", "Refuse Single-Use Plastics", "Bring Your Own Water Bottle and Coffee Cup", "Avoid Plastic Packaging"]
            long_term_tasks = ["Transition to a Zero-Waste Lifestyle", "Make DIY Alternatives", "Advocate for Plastic-Free Practices", "Participate in Beach or Park Cleanup"]
        elif score == 4:
            short_term_tasks = ["Refuse Single-Use Plastics", "Bring Your Own Water Bottle and Coffee Cup", "Always Carry Reusable Bag", "Avoid Plastic Packaging"]
            long_term_tasks = ["Make DIY Alternatives", "Advocate for Plastic-Free Practices", "Participate in Beach or Park Cleanup", "Transition to a Zero-Waste Lifestyle"]
        elif score == 3:
            short_term_tasks = ["Bring Your Own Water Bottle and Coffee Cup", "Always Carry Reusable Bag", "Refuse Single-Use Plastics", "Avoid Plastic Packaging"]
            long_term_tasks = ["Advocate for Plastic-Free Practices", "Participate in Beach or Park Cleanup", "Transition to a Zero-Waste Lifestyle", "Make DIY Alternatives"]
        elif score == 2:
            short_term_tasks = ["Avoid Plastic Packaging", "Refuse Single-Use Plastics", "Bring Your Own Water Bottle and Coffee Cup", "Always Carry Reusable Bag"]
            long_term_tasks = ["Participate in Beach or Park Cleanup", "Transition to a Zero-Waste Lifestyle", "Make DIY Alternatives", "Advocate for Plastic-Free Practices"]
        else:
            short_term_tasks = ["Avoid Plastic Packaging", "Refuse Single-Use Plastics", "Bring Your Own Water Bottle and Coffee Cup", "Always Carry Reusable Bag"]
            long_term_tasks = ["Make DIY Alternatives", "Advocate for Plastic-Free Practices", "Participate in Beach or Park Cleanup", "Transition to a Zero-Waste Lifestyle"]

    else:
        print("Invalid category")

    return short_term_tasks[:2], long_term_tasks[:2]


def get_user_score(category):
    while True:
        try:
            score = int(input(f"Enter your score for {category} (1 to 5): "))
            if 1 <= score <= 5:
                return score
            else:
                print("Please enter a score between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer score between 1 and 5.")

def create_graph(categories, user_scores):
    plt.figure(figsize=(12, 6))

    # Calculate the Sustainability Rating as the average of scores for the four categories
    sustainability_rating = sum(user_scores.values()) / len(categories)
    categories.append("Sustainability Rating")
    user_scores["Sustainability Rating"] = sustainability_rating

    # Coordinates for the base dotted line
    base_line_coords = list(zip(categories, [2.336, 2.73, 2.73, 3.38, sustainability_rating]))

    # Plot the base dotted line
    base_line_x, base_line_y = zip(*base_line_coords)
    plt.plot(base_line_x, base_line_y, 'k--', label='Base Line')

    for category in categories:
        plt.scatter(category, user_scores[category], label=f'{category} (Score: {user_scores[category]})', s=100)

    # Draw lines connecting the dots
    for i in range(len(categories) - 1):
        plt.plot([categories[i], categories[i + 1]], [user_scores[categories[i]], user_scores[categories[i + 1]]], 'k-')

    plt.title('Sustainability Factors and Rating')
    plt.xlabel('Factors')
    plt.ylabel('User Score (1 to 5)')
    plt.yticks([1, 2, 3, 4, 5])
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    categories = ["Electronic Waste", "Fuel Consumption", "Water Usage", "Plastic Usage"]
    user_scores = {}

    for category in categories:
        user_scores[category] = get_user_score(category)

    # Sort categories based on scores and get top 2
    sorted_categories = sorted(user_scores, key=user_scores.get, reverse=True)[:2]

    for category in sorted_categories:
        short_term, long_term = display_tasks(category, user_scores[category])
        print(f"\nFor {category} (Score: {user_scores[category]}):")
        print("Short-Term Tasks:")
        for task in short_term:
            print(f"  - {task}")
        print("\nLong-Term Tasks:")
        for task in long_term:
            print(f"  - {task}")
        print("\n" + "=" * 40)

    # Create and display the graph
    create_graph(categories, user_scores)

if __name__ == "__main__":
    main()
