# Basketball & Esports Performance Analyzer
# Built by Alvitrix

def analyze_basketball_game(points, assists, rebounds, turnovers):
    efficiency = (points + rebounds + assists) - turnovers
    if efficiency >= 25:
        rating = "MVP Performance"
    elif efficiency >= 15:
        rating = "Strong All-Around Game"
    else:
        rating = "Solid Effort - Keep Grinding"
    return efficiency, rating


def analyze_esports_match(kills, deaths, assists, objective_score):
    safe_deaths = max(deaths, 1)
    kda = round((kills + (assists * 0.5)) / safe_deaths, 2)
    impact_score = round((kda * 10) + (objective_score * 0.2), 1)
    if impact_score >= 30:
        tier = "Carry / Clutch Impact"
    elif impact_score >= 18:
        tier = "Consistent Team Contributor"
    else:
        tier = "Needs Positioning Adjustment"
    return kda, impact_score, tier


if __name__ == "__main__":
    print("=== ALVITRIX SPORTS & ESPORTS ANALYZER ===")
    choice = input("Choose mode (1 = Basketball, 2 = Esports): ").strip()

    if choice == "1":
        pts = int(input("Enter Points: "))
        ast = int(input("Enter Assists: "))
        reb = int(input("Enter Rebounds: "))
        tov = int(input("Enter Turnovers: "))
        eff, b_rating = analyze_basketball_game(pts, ast, reb, tov)
        print(f"\nEfficiency Score: {eff} | Rating: {b_rating}")

    elif choice == "2":
        k = int(input("Enter Kills: "))
        d = int(input("Enter Deaths: "))
        a = int(input("Enter Assists: "))
        obj = int(input("Enter Objective Score (0-100): "))
        kda, impact, e_tier = analyze_esports_match(k, d, a, obj)
        print(f"\nKDA Ratio: {kda} | Impact Score: {impact} | Tier: {e_tier}")

    else:
        print("Invalid choice. Please run again and enter 1 or 2.")
