# VCT Data Analysis Report (2021-2025)

## 1. Executive Summary

This report analyzes the Valorant Champions Tour dataset spanning 2021-2025. The dataset provides a comprehensive view of professional Valorant, covering match outcomes, player statistics, agent meta, and economic data.

**Key Findings:**
*   **Scale**: The dataset contains over **1.1 million** player-map performance records and covers 5 years of competitive play.
*   **Meta Evolution**: The "Jett/Sova" dominance of 2021 shifted to a "Chamber" meta in 2022, followed by a rise in "Killjoy" usage in 2023. By 2024-2025, **Omen** has solidified himself as the premier Controller, appearing in >62% of matches.
*   **Map Balance**: **Ascent** and **Split** remain historically defender-sided (~52% Def Win Rate), while newer maps like **Abyss** favor attackers (54% Atk Win Rate).
*   **Data Quality**: The data is robust with minimal duplicates. However, ~21% of rows are missing `Rating` and `Kill/Assist/Survive %`, likely due to data collection variances in lower-tier tournaments or earlier years.
*   **Player Performance**: Veterans like `rawfiul` and `gin` show exceptional consistency with high ACS over 300+ maps played.

**Recommended Dashboard Focus:**
Prioritize valid, high-completeness metrics (ACS, K/D, Pick Rates) and allow filtering by Year/Patch to visualize the shifting meta.

---

## 2. Detailed Findings & Data Discovery (Phase 1)

### 2.1 File Structure
The data is organized by year (`vct_2021` to `vct_2025`), ensuring easy temporal segmentation.
*   **Root**: `data/`
*   **Yearly Folders**: `vct_YYYY/` containing subfolders:
    *   `agents/`: Pick rates, map stats.
    *   `matches/`: Detailed match events (kills, eco, scores, overview).
    *   `ids/`: Mappings for players and teams.
    *   `players_stats/`: Aggregated tournament stats.
*   **Global Mappings**: `all_ids/` contains master lists for IDs.

### 2.2 Schema & Key Tables
*   **`matches/overview.csv`**: The "Fact Table" for player performance.
    *   *Key Columns*: `Match ID`, `Player`, `Agent`, `ACS`, `Kills`, `Deaths`, `Headshot %`.
    *   *Grain*: One row per player per map.
*   **`matches/scores.csv`**: Match results.
    *   *Key Columns*: `Match ID`, `Team A`, `Team B`, `Score A`, `Score B`, `Match Result`.
*   **`agents/agents_pick_rates.csv`**: Meta analysis.
    *   *Key Columns*: `Agent`, `Pick Rate`, `Map`.
*   **`matches/eco_rounds.csv`**: Economy deep dives.
    *   *Key Columns*: `Loadout Value`, `Remaining Credits`, `Outcome` (Win/Loss).

### 2.3 Relationships (Conceptual ERD)
*   `Tournaments` (1) --> (N) `Matches`
*   `Matches` (1) --> (N) `Games` (Maps)
*   `Games` (1) --> (N) `Player_Stats_Overview` (10 rows per game)
*   `Games` (1) --> (N) `Kills_Events` (Many rows per game)
*   `Players` and `Teams` act as Dimension tables linking across all Fact tables.

---

## 3. Data Quality Assessment (Phase 2)

*   **Completeness**:
    *   Core stats (`ACS`, `Kills`, `Deaths`) are missing in only ~1.2% of records (Excellent).
    *   Advanced stats (`Rating`, `KAST`) are missing in ~21% of records. these should be treated with caution in historical aggregations.
*   **Consistency**:
    *   `K/D` column perfectly matches the derived `Kills - Deaths` calculation in test samples.
    *   Match Scores generally align with "Winner" declarations, with <0.5% exceptions (likely forfeits).
*   **Anomalies**:
    *   **Extreme Outliers**: Found ~1300 records with ACS > 525 (Max 2372). These are statistical impossibilities in standard play and likely represent bugged data or non-standard matches. **Action**: Filter `ACS > 500` for all analysis.

---

## 4. Exploratory Data Analysis (Phase 3)

### 4.1 Agent Meta Trends
The dataset clearly captures major meta shifts:
*   **2021**: The "Duelist Era". **Jett** (73%) and **Sova** (75%) were nearly mandatory.
*   **2022**: The "Chamber Era". **Chamber** exploded to 46% pick rate.
*   **2023**: The "Lockdown Era". **Killjoy** (63%) became the dominant Sentinel.
*   **2024-2025**: The "Controller Era". **Omen** (>62%) is the most defined agent, followed closely by **Viper**. **Yoru** has seen a surprising surge in 2025 (~35%).

### 4.2 Map Balance
Maps have distinct biases:
*   **Attacker Sided**: `Abyss` (54%), `Lotus` (53%), `Icebox` (52%).
*   **Defender Sided**: `Ascent` (53%), `Split` (52%), `Bind` (50.3%).
*   **Balanced**: `Fracture` (51/49) and `Pearl` (50/50).

### 4.3 Top Performers (ACS)
Top players by Average Combat Score (min 50 maps):
| Player | Avg ACS | Maps Played |
| :--- | :--- | :--- |
| zyad | 300.4 | 58 |
| Roy | 294.6 | 126 |
| g0dciz | 289.5 | 56 |
| rawfiul | 274.0 | 361 |
| gin | 273.5 | 383 |

*Note: `rawfiul` and `gin` stand out for maintaining elite stats over a massive number of games.*

---

## 5. Dashboard Recommendations (Phase 5)

### 5.1 Proposed Pages
1.  **Global Meta Snapshot**:
    *   *Visuals*: Line chart of Agent Pick Rates over time (filtered by Role).
    *   *Filters*: Region, Patch/Year.
2.  **Player Profile**:
    *   *Visuals*: Spider chart (ACS, K/D, KAST, HS%), Trend line of Performance.
    *   *Metrics*: "Clutch %", "First Blood Success".
3.  **Map Analysis**:
    *   *Visuals*: Heatmap of Atk/Def win rates. Bar chart of Top Agents per Map.

### 5.2 Data Modeling Strategy
*   **Pre-Aggregation**: Create a `Player_Career_Stats` table aggregating `overview` by `Player_ID`. Calculating 1.1M rows on the fly will be slow.
*   **Filtering**: Always default to `Stage != 'Qualifiers'` if possible to focus on top-tier play, or provide a "Tier" toggle.
*   **Cleaning**: Exclude rows where `ACS > 500` or `Rounds Played < 13` (surrenders) to avoid skewing averages.
