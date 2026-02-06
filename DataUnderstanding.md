# Data Understanding & Analysis Instructions

## Context: Valorant & Esports

### About Valorant
Valorant is a tactical 5v5 first-person shooter developed by Riot Games. Key gameplay elements:

- **Agents**: Characters with unique abilities (Duelists, Initiators, Controllers, Sentinels)
- **Maps**: Competitive maps include Ascent, Bind, Haven, Split, Icebox, Breeze, Fracture, Pearl, Lotus, Sunset
- **Economy System**: Players earn credits to buy weapons/abilities each round
- **Round Structure**: Best of 24 rounds (first to 13 wins), with attackers/defenders switching at half
- **Abilities**: Each agent has 4 abilities (2 purchasable, 1 signature free ability, 1 ultimate)

### Valorant Champions Tour (VCT)
The VCT is the premier global esports circuit featuring:
- **International Events**: Masters tournaments and Champions (world championship)
- **Regional Leagues**: Americas, EMEA, Pacific, China
- **Tier Structure**: VCT International → VCT Challengers → Game Changers
- **Patches**: Game balance changes regularly affect agent/weapon meta

### Critical Esports Metrics
- **ACS (Average Combat Score)**: Overall performance metric (damage + kills + assists + utility)
- **K/D Ratio**: Kills to deaths ratio
- **ADR (Average Damage per Round)**: Damage consistency
- **KAST**: Percentage of rounds with Kill/Assist/Survival/Traded
- **First Bloods**: Opening kills that shift round advantage
- **Clutch %**: Win rate in 1vX situations
- **Economy Rating**: Efficiency of credit usage
- **Ultimate Usage**: Timing and effectiveness of ultimate abilities

---

## Your Mission: Comprehensive Data Analysis

You are tasked with conducting a **deep, professional-grade analysis** of the Valorant Champions Tour dataset (2021-2025). This analysis will inform the creation of a world-class analytics dashboard.

## Phase 1: Initial Data Discovery

### 1.1 File Structure Analysis
For each CSV file in the working directory:

```
- List all CSV files found
- For each file, provide:
  * File name and size
  * Number of rows and columns
  * Column names and data types
  * First 5 rows (sample data)
  * Last 5 rows (check for consistency)
```

### 1.2 Schema Understanding
Create a detailed data dictionary:

```
For each table/file:
- Table purpose and entity it represents
- Primary key(s)
- Foreign key relationships (how tables connect)
- Column descriptions (what each field means in Valorant context)
- Data type recommendations (int, float, string, datetime, categorical)
```

### 1.3 Relationship Mapping
```
- Draw an entity-relationship diagram (in text/ASCII)
- Identify fact tables vs dimension tables
- Suggest optimal join keys between tables
- Recommend star schema or snowflake schema design
```

## Phase 2: Data Quality Assessment

### 2.1 Completeness Check
```
For each column:
- Calculate % of missing values
- Identify patterns in missing data
- Assess if missing data is MCAR (random) or MAR (systematic)
- Recommend handling strategy (impute, drop, flag)
```

### 2.2 Consistency Validation
```
- Check for duplicate records (what defines a duplicate?)
- Verify foreign key integrity
- Identify inconsistent naming (team name variations, player aliases)
- Check date ranges (are 2021-2025 all represented?)
- Validate categorical values (agent names, map names, regions)
```

### 2.3 Data Anomalies
```
- Outlier detection for numeric fields (KDA > 10, ACS > 500, etc.)
- Logical inconsistencies (deaths > rounds played, negative values)
- Temporal anomalies (future dates, impossible timestamps)
- Domain-specific validation (agents that didn't exist in certain patches)
```

## Phase 3: Exploratory Data Analysis (EDA)

### 3.1 Tournament Coverage
```
- How many unique tournaments?
- Tournament types distribution (Masters, Champions, Regional)
- Timeline coverage (gaps in data?)
- Regional representation (EMEA, Americas, Pacific, China, etc.)
```

### 3.2 Player Analytics
```
- Total unique players in dataset
- Player statistics distribution:
  * ACS (mean, median, std dev, percentiles)
  * K/D ratios across all players
  * First blood percentages
  * Clutch success rates
- Most represented players (highest match counts)
- Career longevity analysis (players across multiple years)
```

### 3.3 Team Dynamics
```
- Total unique teams
- Team performance metrics aggregation
- Roster stability (how often do team compositions change?)
- Regional dominance (which regions perform best?)
- Team lifespan (teams active across multiple years vs single year)
```

### 3.4 Agent Meta Evolution
```
- Agent pick rates by:
  * Year/Season
  * Tournament tier
  * Map
  * Region
- Agent role distribution (Duelist, Controller, Initiator, Sentinel)
- Meta shifts (which agents rose/fell in popularity?)
- Agent win rates vs pick rates (overperforming/underperforming agents)
```

### 3.5 Map Analytics
```
- Map pool changes over time
- Win rates: Attacker vs Defender sides
- Map-specific agent preferences
- Average round counts per map
- Most competitive maps (closest win rates)
```

### 3.6 Temporal Patterns
```
- Performance trends over years (is competition getting tighter?)
- Seasonal patterns (tournament frequency)
- Patch impact analysis (if patch data available)
- Event chronology and major milestones
```

## Phase 4: Advanced Analytical Insights

### 4.1 Feature Engineering Opportunities
Suggest calculated metrics that don't exist but would be valuable:

```
Examples:
- Economy efficiency = (Rounds won while eco) / (Total eco rounds)
- Clutch factor = (Clutch wins) / (Clutch opportunities)
- First half vs second half performance differential
- Pistol round win impact on match outcome
- Ultimate usage timing (early/mid/late round usage %)
- Multi-kill frequency (2k, 3k, 4k, ace percentages)
- Trading effectiveness = (Deaths traded) / (Total deaths)
```

### 4.2 Correlation Analysis
```
- Which individual stats correlate most with match wins?
- Agent synergy patterns (which agents are picked together?)
- Map preferences by team/region
- Performance correlation with tournament tier
- Does first blood % correlate with round win %?
```

### 4.3 Predictive Potential
```
- What data could predict match outcomes?
- Can you identify "clutch players" vs "consistent performers"?
- Early warning signs of team decline
- Meta prediction based on patch notes (if available)
```

### 4.4 Benchmarking Standards
```
Establish performance tiers:
- What ACS defines "elite" vs "average" vs "below average"?
- K/D benchmarks by agent role
- Expected first blood % by agent type
- Tournament-tier performance differences
```

## Phase 5: Dashboard Data Preparation Recommendations

### 5.1 Aggregation Tables
Suggest pre-computed aggregations for dashboard performance:

```
- Player career statistics (lifetime totals)
- Team season summaries
- Monthly/quarterly agent pick rates
- Map-specific leaderboards
- Tournament-level summaries
```

### 5.2 Data Modeling for BI
```
Recommend:
- Fact tables (what should be measured?)
- Dimension tables (how should we slice data?)
- Bridge tables (for many-to-many relationships)
- Slowly changing dimensions (player team changes)
```

### 5.3 Filtering Requirements
```
Essential filters for dashboard:
- Date range / Season / Year
- Tournament tier (International, Regional, Challengers)
- Region (Americas, EMEA, Pacific, China)
- Agent / Agent role
- Map
- Team
- Player
- Patch version (if available)
```

## Phase 6: Specific Data Questions to Answer

As you analyze, explicitly answer these questions:

### Gameplay Questions
1. What is the average round count per match?
2. Which side (Attack/Defense) has advantage on each map?
3. What's the most picked agent overall? By role? By map?
4. What's the average ACS for professional players?
5. What percentage of rounds end with a clutch situation?

### Competitive Questions
1. Which region has the most tournament wins?
2. Which teams have the longest winning streaks?
3. Who are the top 10 players by ACS? By K/D? By first bloods?
4. What's the tournament prize pool distribution (if available)?
5. Which agents have the highest win rates despite low pick rates?

### Meta Questions
1. How has agent diversity changed from 2021 to 2025?
2. Have any maps become significantly more attacker/defender sided?
3. Which agents fell out of meta? Which emerged?
4. Are there regional meta differences?
5. Do international teams perform better on certain maps?

### Player/Team Questions
1. Which players have competed the longest (2021-2025)?
2. What's the average career length of a pro Valorant player?
3. Which teams have the most roster stability?
4. Do player transfers improve individual performance?
5. Which rookie players have the highest impact?

## Deliverable Format

Please provide your analysis as a structured report with:

### Executive Summary
- Dataset overview (size, scope, quality score)
- Key findings (3-5 bullet points)
- Recommended dashboard focus areas

### Detailed Findings
- All Phase 1-5 analyses with tables, statistics, and insights
- Data quality report card (% complete, % accurate, issues found)
- Visualizations (in text form: describe what charts would show)

### Data Dictionary
- Complete schema documentation
- Table relationships diagram
- Column-level metadata

### Dashboard Recommendations
- Which data should drive which dashboard pages
- Suggested KPIs and their calculation formulas
- Performance optimization tips (indexing, aggregation)
- Data refresh strategy (real-time, daily, weekly?)

### Known Limitations & Caveats
- Data gaps or quality issues
- Metrics that can't be calculated from available data
- Assumptions you had to make
- Recommendations for data enrichment

---

## Important Notes

- **Be thorough but practical**: Focus on insights that will drive dashboard decisions
- **Think like an analyst**: Don't just describe data, interpret what it means
- **Consider the end user**: Esports fans, team coaches, and tournament organizers will use this dashboard
- **Valorant domain knowledge**: Apply your understanding of the game to interpret patterns
- **Be honest about limitations**: If data is missing or unclear, say so

Begin your analysis now. Take your time and be comprehensive.