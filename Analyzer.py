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
    print("=== BASKETBALL COMBO GUARD STATS ===")
    eff, b_rating = analyze_basketball_game(points=18, assists=7, rebounds=5, turnovers=2)
    print(f"Efficiency Score: {eff} | Rating: {b_rating}\n")

    print("=== ESPORTS COMPETITIVE MATCH STATS ===")
    kda, impact, e_tier = analyze_esports_match(kills=19, deaths=11, assists=8, objective_score=45)
    print(f"KDA Ratio: {kda} | Impact Score: {impact} | Tier: {e_tier}")
